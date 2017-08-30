file_list = ["123.txt", "Bob.txt", "ex1.txt", "WEB-tty.txt", "web-fdgd.txt", "*asjd.txt"]

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

counter = 0
for file_name in file_list:
    if file_name.startswith("WEB-") or file_name[0].isdigit():
        counter += 1
        print counter






# for file_name in file_list:
#     print file_name
#     if file_name.startswith("WEB-"):
#         counter=counter + 1
#         print counter
#     elif file_name[0].isdigit():
#         counter=counter + 1
#         print counter


