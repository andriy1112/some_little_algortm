import os
import time

sourse = ["E:\\Sublime Text 3"]
target_dir = 'E:\\Backup'
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
zip_comand = "zip -qr {0} {1}".format(target, ' '.join(sourse))
if os.system(zip_comand) == 0:
    print('Good , backup in ', target)
else:
    print('Bad')


