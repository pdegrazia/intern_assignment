import os


# def counting_files_dot():
#     my_directory = os.getcwd()
#     dir_files = os.listdir(my_directory)
#     counter = 0
#     for name_of_file in dir_files:
#         if name_of_file.startswith("WEB-") or name_of_file[0].isdigit():
#             pass
#             counter += 1
#     print counter, ":these are the amount of test files that match the accepted criteria"


def counting_files_user_entry():
    dir_files = os.listdir(entry)
    counter = 0
    for name_of_file in dir_files:
        if name_of_file.startswith("WEB-") or name_of_file[0].isdigit():
            counter += 1
    print counter, ":this is the amount of test files that match the accepted criteria"



if __name__ == '__main__':

    entry = raw_input("Enter the path address here:")

    # try:
    #     if entry==".":
    #         counting_files_dot()
    #
    # except:
    #     pass

    try:
        os.path.isabs(entry)
        counting_files_user_entry()

    except OSError:
        print "This directory does not exist, please try again"

# else:
#     print "Sorry, you have not entered a valid path address"



