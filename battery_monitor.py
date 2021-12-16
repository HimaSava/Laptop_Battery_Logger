
#Author - HimaSava
#Date - 16/12/2021

import psutil						
from plyer import notification
import time
import datetime

batHigh = 95	#Battery percentage above which you get a notification
batLow = 20		#Battery percentage below which you get a notification

while(1):
	ct = datetime.datetime.now()
	battery = psutil.sensors_battery()
	plug = battery.power_plugged
	if battery.percent > batHigh and plug == True:
		notification.notify(title="Battery Update",message="Battery fully Charged remove Charger", app_name = "Battery Logger")
	elif battery.percent < batLow and plug == False:
		notification.notify(title="Battery Update",message="Battery Discharged connect Charger", app_name = "Battery Logger")
	
	#Print statement for debugging if needed
	#print("Battery Status:\nPlugged In: " + str(plug) + "\nPercentage: " + str(battery.percent) + "\nTime: " + str(ct.time()))
	
	#Log the data into a CSV file
	data = ''
	with open('Bat_Log.csv','a') as file:
		data = str(ct.date()) + ','
		data = data + str(ct.time()) + ','
		data = data + str(plug) + ','
		data = data + str(battery.percent) + '\n'
		file.writelines(data)

	#Sample taken ever 1min
	time.sleep(60)
