import ConfigParser
import os
import time
import logging
import schedule

def backup():
    logging.info("Running MySQL Dumping process at :"+ time.strftime("%Y-%m-%d %H:%M:%S"))
    filestamp = time.strftime('%Y-%m-%d')
    os.popen("mysqldump -u root -ppassword -h localhost -e --opt -c ohf_budgetfy | gzip -c > \\budgetfy\\backup\\dump\\ohf_budgetfy_"+filestamp+".gz")
    #os.popen("mysqldump -u root -ppassword -h localhost -e --opt -c ohf_budgetfy | gzip -c > ohf_budgetfy_"+filestamp+".gz")
    logging.info("Dump file \\budgetfy\\backup\\dump\\ohf_budgetfy_"+filestamp+".gz")

schedule.every().day.at("17:00").do(backup)

logging.basicConfig(filename='\\budgetfy\\python logs\\backup.log',level=logging.DEBUG)
schedule.every().day.at("17:00").do(backup)

backup()
while True:
    schedule.run_pending()
    time.sleep(1)