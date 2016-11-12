import time
import schedule
import os
import zipfile
import logging

def compress():
    logging.info("Backing up files "+time.strftime("%Y-%m-%d %H:%M:%S"))
    cur_date = time.strftime("%d/%m/%Y")
    date = cur_date.split("/")
    compression = zipfile.ZIP_DEFLATED
    modes = {zipfile.ZIP_DEFLATED: 'deflated',
            zipfile.ZIP_STORED:   'stored',
            }
    location = "\\budgetfy\\upload\\"+date[2]+"\\"+date[1]+"\\"+date[0]
    
    if os.path.isdir(location):
        logging.info("Zipping "+location)
        zf = zipfile.ZipFile(date[2]+"-"+date[1]+"-"+date[0]+'.zip', mode='w')
        for file_ in os.listdir(location):
            zf.write(file_, location+"\\"+file_, compress_type=compression)
        zf.close()

logging.basicConfig(filename='\\budfget\\python logs\\compressor.log',level=logging.DEBUG)
schedule.every().day.at("17:00").do(compress)

compress()
while True:
    schedule.run_pending()
    time.sleep(1)