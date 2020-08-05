import os
import datetime
path="C:\\Users\\ADMIN\Desktop"
os.chdir(path)
try:
    os.mkdir("automated_directory")
except:
    pass
tm=os.path.getmtime("automated_directory")
size=os.path.getsize("automated_directory")
tm_str=datetime.datetime.fromtimestamp(tm)
print("successfully created")
print("time modified: {}".format(tm_str))
print("directory size: {}".format(size))



