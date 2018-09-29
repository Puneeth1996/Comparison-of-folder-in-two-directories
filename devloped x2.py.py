# Compare file that are present in two diffrent directories
import os
import time


dir1 = os.listdir("I:\Studies")

dir1_len=len(dir1)

print dir1_len

dir1_path = os.listdir(os.path.realpath("I:\Studies"))


print "\n\n"


dir2 = os.listdir("J:\Course PART 2")

dir2_len=len(dir2)

print dir1_len

dir2_path = os.listdir(os.path.realpath("J:\Course PART 2"))



print '\n'
print time.strftime('%Y - %B - %d')



for i in range(dir1_len):
	for j in range(dir2_len):
		if dir1[i]==dir2[j]:
			print 'match foun----'

			print '\n'
			
			print dir2[j]

			print '\n'

			print dir1[i]
        

    
        
        
        
    
    
        
