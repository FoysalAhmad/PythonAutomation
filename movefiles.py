import shutil,os

src = '/Users/foahmad/Python/'
des = '/Users/foahmad/Python/PythonAutomation'

src_files = os.listdir(src)

for files_txt in src_files:
	#os.path.basename(files_txt))
	if files_txt.endswith('.py'):
		shutil.move(files_txt,des)
		#path = os.path.join(src,files_txt)
		#os.unlink(path)
print('\n')