import threading,time

print('start of program.')

def takeANap(str):
	time.sleep(10)
	print(str)
	print('Wake up!')


threadObj = threading.Thread(target=takeANap,args=['test'])
threadObj.start()

print('End of program')
