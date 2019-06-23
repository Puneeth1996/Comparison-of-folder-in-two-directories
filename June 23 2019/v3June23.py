import os
import time

print (time.strftime('%Y - %m - %d'))
dir_name = 'D:\\'
dir = os.listdir(dir_name)
print ('\n\n\n')
print(50*"-")
print("The Directory {0} has {1} number of folder in it.".format(dir_name,len(dir)))
print(dir)
print(50*"-")
print ('\n\n\n')


# https://stackoverflow.com/questions/2104080/how-to-check-file-size-in-python?rq=1
def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
            # This below line show the mb value of size
            # total_size += os.path.getsize(fp)  >> 20
    return convert_bytes(total_size)






for d in dir:
    d_sub = dir_name + d
    try:
        d_sub_dir = os.listdir(d_sub)        
        print ('\n\n\n')
        print(50*" - ")
        print("The Directory \t\t {0} has {1} \t\t number of folder in it. With {2}".format(d_sub, len(d_sub_dir),get_size(d_sub) ) )
        
        
        for sub_folders in d_sub_dir:
            sub_folders_dir =  d_sub + "\\" + sub_folders 
            print(sub_folders_dir + '\t\t' + get_size(sub_folders_dir) + '\n\n\n')

            
    except WindowsError :
        print(" ===  Error === ")




print ('\n')
print (time.strftime('%Y - %m - %d'))