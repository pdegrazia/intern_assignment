import os
my_directory=os.getcwd()
path = my_directory
dir_files = os.listdir(path)
counter = 0
for name_of_file in dir_files:
    if name_of_file.startswith("WEB-") or name_of_file[0].isdigit():
        counter += 1
print counter, ":this is the amount of tests that are matching the accepted criteria"
