#!usr/bin/env
# stopwatch.py - A simple stopwatch program.

import time

#Display the program's instructions.

print('Press ENTER to begin. Afterwards, press ENTER to \'click\' the watch. press Ctrl-C to quit.')
raw_input()			  #press enter to begin
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1

#start tracking the lap times
try:
	while True:
		raw_input()
		lapTime = round(time.time()-lastTime,2)
		totalTime = round(time.time()-startTime,2)
		print('Lap #%s: %s (%s)'%(lapNum,totalTime,lapTime))
		lapNum +=1
		lastTime = time.time()
except KeyboardInterrupt: 
	#Handle the Ctrl-C exception to keep its error message from displaying.
	print('\nDone')
