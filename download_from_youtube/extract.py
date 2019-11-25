#!/usr/bin/env python2.7
# coding: utf-8
import os
import multiprocessing
import glob
import sys

in_dir = '505videos'
out_dir = '505videos_frames'

def doSth((video_name)):
	print video_name, 'extracting...'
	vdname = os.path.splitext(os.path.basename(video_name))[0]
	print vdname
	if not os.path.exists(out_dir + '/' + vdname):
		os.mkdir(out_dir + '/' + vdname)

	os.system('ffmpeg -i %s -frames 100 -vf fps=0.2 %s/%s/%s_frame_%%05d.jpg'%(video_name, out_dir, vdname, vdname))


if __name__ == '__main__':
	files = glob.glob(in_dir + '/*.mp4') + glob.glob(in_dir + '/*.mkv') + glob.glob(in_dir + '/*.webm')
	print len(files)
	raw_input()
	files.sort()
	tasks = [(it) for it in files]
	pool_size = multiprocessing.cpu_count()
	pool = multiprocessing.Pool(processes=pool_size, maxtasksperchild=8)
	pool.map(doSth, tasks)
	pool.close()
	pool.join()