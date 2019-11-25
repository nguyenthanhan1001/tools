import sys
import os

from icrawler.examples import GoogleImageCrawler

kw_file = sys.argv[1]
out_dir = sys.argv[2]

for line in open(kw_file):
	kw = line.strip()
	print (kw, '...')
	out_fd = out_dir + '/' + kw
	if not os.path.exists(out_fd):
		os.makedirs(out_fd)
	else:
		os.system('rm -rf %s/*'%(out_fd))

	google_crawler = GoogleImageCrawler(out_fd)
	google_crawler.crawl(keyword=kw, offset=0, max_num=100,
	                     date_min=None, date_max=None, feeder_thr_num=1,
	                     parser_thr_num=1, downloader_thr_num=4,
	                     min_size=(200,200), max_size=(800, 800))
