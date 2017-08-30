
'''
read files from directory
loop over list of files
if file name starts with a number or filename starts with "WEB-"
   then increase counter
else
   do nothing

questions:
what type are the filenames?
is there any specific method that does what is written in pseudo code?
what does the "in" operator do in python?
    
'''

import os
path = "/home/raees/internship/intern_assignment/intern_assignment"

dir_files = os.listdir(path)
for file_count in dir_files:
    print file_count
counter = 0
for file_count in dir_files:
    if file_count.startswith("WEB-") or file_count[0].isdigit():
        counter += 1
        print counter