import time
import os
import zipfile

cur_date = time.strftime("%d/%m/%Y")
date = cur_date.split("/")
compression = zipfile.ZIP_DEFLATED
modes = {zipfile.ZIP_DEFLATED: 'deflated',
          zipfile.ZIP_STORED:   'stored',
        }
location = "\\budgetfy\\upload\\"+date[2]+"\\"+date[1]+"\\"+date[0]
if os.path.isdir(location):
    zf = zipfile.ZipFile(date[2]+"-"+date[1]+"-"+date[0]+'.zip', mode='w')
    for file_ in os.listdir(location):
        zf.write(file_, location+"\\"+file_, compress_type=compression)
    zf.close()