#!/bin/bash

set -e

if [ $# -ne 3 ]; then
    echo "Usage: $0 n_jobs video_ids out_dir"
    exit 1
fi

n_jobs=$1
video_ids=$2
dest=$3

url_base="https://www.youtube.com/watch?v="

# Stop script if youtube-dl or parallel is not found
youtube-dl --version \
    >/dev/null 2>&1 || { echo "youtube-dl not found"; exit 1; }
parallel --version \
    >/dev/null 2>&1 || { echo "parallel not found"; exit 1; }

[ -d $dest ] && { echo "$dest exists!"; exit 1; }
mkdir -p $dest

# Download Youtube videos on the list in parallel
#parallel -a $video_ids --colsep '\t' -j $n_jobs \
#    youtube-dl ${url_base}{1} --ignore-errors -o $dest/${2}
cat $video_ids | parallel -j $n_jobs --colsep '\t' \
    youtube-dl ${url_base}{1} --ignore-errors -o $dest/{2}

[ -f downloaded.txt ] && rm downloaded.txt
[ -f not_available.txt ] && rm not_available.txt

# Check missing IDs in dest from complete_id_list
while read -r yt_id video_id; do
    if [ ! -f $dest/$video_id ]; then
        full_url=${url_base}${yt_id}
        code=$(curl -o /dev/null --silent --head \
            --write-out '%{http_code}\n' $full_url)
        # Try to download files which actually return 200 status
        if [ $code -eq "200" ]; then
            youtube-dl $full_url --ignore-errors -o $dest/$video_id
            echo "$video_id" >> downloaded.txt
        # Otherwise, videos are no longer available
        else
           echo "$video_id $code" >> not_available.txt
        fi
    else
        echo "$video_id" >> downloaded.txt
    fi
done < $video_ids
