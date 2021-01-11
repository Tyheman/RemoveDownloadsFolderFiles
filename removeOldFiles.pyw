import os, shutil
import os.path, time
import getpass
from datetime import datetime, timedelta

days = 7
username = getpass.getuser()
currTime = datetime.now()

folder = 'C:/Users/' + username + '/Downloads'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    fileTime = os.path.getmtime(file_path)
    modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(fileTime))
    print(modificationTime)
    try:
        if (os.path.isfile(file_path) or os.path.islink(file_path)) and fileTime < (currTime- timedelta(days)).timestamp():
            os.unlink(file_path)
        elif os.path.isdir(file_path) and fileTime < (currTime - timedelta(days)).timestamp():
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))