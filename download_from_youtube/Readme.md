## Download videos from Youtube
If you hope to download original videos, extract video frames and compute their own features, please follow below:
```
# install youtube-dl
sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl
# install parallel
sudo apt-get install parallel

# number_of_jobs video_id_file output_dir
./scripts download_parallel.sh 4 video/train_video_ids.txt train_download
```

# error video vid00306 + vid00421