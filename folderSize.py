def folderSize(dirPath):
	import os

	totalSize = 0
	for filename in os.listdir(dirPath):
		totalSize += os.path.getsize(os.path.join('/Users/foahmad/Python',filename))
 
	print(totalSize)

folderSize('/Users/foahmad/Python')