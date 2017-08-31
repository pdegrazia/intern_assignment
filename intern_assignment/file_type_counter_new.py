import os
my_directory=os.getcwd()
dir_files = os.listdir(my_directory)
counter = 0
for name_of_file in dir_files:
    if name_of_file.startswith("WEB-") or name_of_file[0].isdigit():
        counter += 1
print counter, ":this is the amount of test files that match the accepted criteria"
