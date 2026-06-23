import time 
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('start of our program')
sum=0
for x in range (2,102,+2):#we are going to stop at 100
	sum+=x
	logging.debug('for  x='+str(x)+'sum ='+str(sum))
logging.debug('end of program  ')
logging.debug('sum of even numberfrom 2 to 100 =  '+str(sum)+'!')

