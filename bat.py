import csv
import time
import os
from datetime import datetime

def scanbat():
    file = "battery_log.csv" # change csv file with preference
    new_file = not os.path.exists(file)
    with open("/sys/class/power_supply/BAT0/capacity") as f:
        battery = int(f.read().strip())
    with open(file, "a",newline="") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(["timestamp","battery"])
        writer.writerow([datetime.now().isoformat(timespec="minutes"),battery])
      
try:
    i=1
    while True:
        print(f"on iteration {i}",end="\r")
        scanbat()
        time.sleep(60)
        i+=1

except KeyboardInterrupt:
    print("",end="\r") # to get out of iteration line properly
    print(f"\nProgram terminated by user after {i} iterations")
