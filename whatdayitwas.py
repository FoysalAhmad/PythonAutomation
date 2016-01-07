import time
import datetime

day = raw_input('Enter date (format:mm/dd/yyyy):\n')


dayFormat =datetime. datetime.strptime(day,'%m/%d/%Y')

print(dayFormat.strftime('%A'))
