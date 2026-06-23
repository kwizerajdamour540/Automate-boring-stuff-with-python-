import time
import logging
# im gonna create debugging file
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG,
format=' %(asctime)s -  %(levelname)s -  %(message)s')
sum=0
x=1
duration=5
end_time=time.time()+duration

logging.debug('start of addind add')

while time.time()<end_time:
 
  sum+=x
  x=x+1
  logging.debug('sum of add numberfrom 1 to '+str(x)+' ='+str(sum))

logging.debug('end of program after 5 secomd of looping sum of add number ='+str(sum))

print (f"after  five count of add number is {x} and  second sum = {sum}")
