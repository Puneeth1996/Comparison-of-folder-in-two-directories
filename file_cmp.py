# Compare file that are present in two different directories
import os
import time


dir1 = os.listdir("J:\Courses 06 mar 2019")
dir1_len=len(dir1)
dir1_path = os.listdir(os.path.realpath("J:\Courses 06 mar 2019"))


dir2 = os.listdir("J:\Courses 15 mar 2019")
dir2_len=len(dir2)
dir2_path = os.listdir(os.path.realpath("J:\Courses 15 mar 2019"))



print '\n'
print time.strftime('%Y - %m - %d')



for i in range(3):
	for j in range(1):
		if dir1[i]==dir2[j]:
			print 'match foun----'
			print '\n'
			print dir2[j]
			print '\n'
			print dir1[i]
        

    
        
        
