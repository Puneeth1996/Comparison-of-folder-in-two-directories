import os
import time


print '\n'
print time.strftime('%Y - %m - %d')

dir_name = 'J:\\'
dir = os.listdir(dir_name)
print(len(dir))
# print(dir)
print(50*"-")




for d in dir:
    # print (d)
    d_sub = dir_name + d
    # print (d_sub)
    try:
        d_sub_dir = os.listdir(d_sub)
        # print(d_sub_dir)
        print(len(d_sub_dir))
        print(50*" - ")
        for sub_folders in d_sub_dir:
            # print(len(sub_folders))
            print(sub_folders)

            
    except WindowsError :
        print(" ===  Error === ")




print '\n'
print time.strftime('%Y - %m - %d')
