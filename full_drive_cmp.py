import os
import time

print (time.strftime('%Y - %m - %d'))


def HDFolderContents(dir_name):
    dir = os.listdir(dir_name)
    HDFolderContents1 = []
    for d in dir:
        d_sub = dir_name + d
        try:
            d_sub_dir = os.listdir(d_sub) 
            HDFolderContents1 += d_sub_dir               
        except WindowsError :
            print(" ===  Error ===  AT " + d_sub)
    return (HDFolderContents1)


print (HDFolderContents('C:\\'))

# I should say I have evoloved using programming and my brain in syn for particular use case 

# Have implemeted a funtion that spits out the folder in one level deep of your specified root directory 
# this function return a list that  inturn can be used to campare two folder contents.
