import cv2
import glob
import multiprocessing
import os

min_size = (240, 320)

def doSth((file_name)):
	img = cv2.imread(file_name)
	hh, ww = img.shape[:2]

	if float(hh) / ww < 240./320:
		img = cv2.resize(img, (0, 0), fx=240./hh, fy=240./hh)
		hh, ww = img.shape[:2]
		pad = (ww - 320) / 2
		crop = img[:, pad:pad+320, :]
	else:
		img = cv2.resize(img, (0, 0), fx=320./ww, fy=320./ww)
		hh, ww = img.shape[:2]
		pad = (hh - 240) / 2
		crop = img[pad:pad+240, :, :]
	
	file_name = file_name.replace('505videos_frames/', '505videos_cropped/')
	if not os.path.exists(os.path.dirname(file_name)):
		os.mkdir(os.path.dirname(file_name))

	cv2.imwrite(file_name, crop)
	print file_name

if __name__ == '__main__':
	# folders = glob.glob('vid*/')
	# folders.sort()
	# print len(folders), 'found...'

	# sizes = []
	# for it in folders:
	# 	fn = it + it[:-1] + '_frame_00001.jpg'
	# 	shape = cv2.imread(fn).shape
	# 	if shape not in sizes:
	# 		sizes.append(shape)
	# print sizes
	# exit(0)


	'''
	files = glob.glob('505videos_frames/vid*/*.jpg')
	files.sort()
	print len(files), 'found...'
	'''

	videos = ['vid00043/', 'vid00149/', 'vid00175/', 'vid00186/', 'vid00194/', 'vid00197/', 'vid00202/', 'vid00203/', 'vid00204/', 'vid00205/', 'vid00206/', 'vid00214/', 'vid00218/', 'vid00267/', 'vid00339/']
	files = []
	for it in videos:
		files += glob.glob('505videos_frames/' + it + '*.jpg')
	files.sort()
	print len(files)
	raw_input()

	tasks = [(it) for it in files]
	pool_size = multiprocessing.cpu_count()
	pool = multiprocessing.Pool(processes=pool_size, maxtasksperchild=8)
	pool.map(doSth, tasks)
	pool.close()
	pool.join()