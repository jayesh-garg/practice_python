import os

def copy_file(file1,file2):
    with open(file1, "r") as rf:
        with open(file2, "w") as wf:
            wf.write(rf.read())

def move_file(file1,file2):
    copy_file(file1,file2)
    os.remove(file1)

def replace_word(file1):
    with open(file1, 'r+') as f:
        string1=raw_input("Enter the string to be replaced")
        string2=raw_input("Enter the string to be replaced with")
        for line in f.readlines():
            f.write(line.replace(string1,string2))

def count_string(file1):
    count = 0
    with open(file1, 'r') as f:
        string=raw_input("Enter the string to be counted: ")  # type:
        for line in f.readlines():
            if string in line:
                count += 1
    print ("number of time string came= {}".format(count))
try:
    task=True
    while task == True :
        switcher={
            "1":"copy",
            "2":"move",
            "3":"replace",
            "4":"count string "
        }
        print("Select the operation to perform with file")
        for no,options in switcher.items():
            print ("{}:{}").format(no,options)
        option=int(input("Enter which option to perform: "))
        if option == 1 :
            file1=raw_input("Enter the path for the file: ")
            file2=raw_input("Enter the path to copy: ")
            copy_file(file1,file2)
        elif option == 2 :
            file1 = raw_input("Enter the path for the file: ")
            file2 = raw_input("Enter the path to move: ")
            move_file(file1, file2)
        elif option == 3 :
            file1 = raw_input("Enter the path for the file: ")
            replace_word(file1)
        elif option == 4:
            file1 = raw_input("Enter the path of the file: ")  # type:
            count_string(file1)
        else:
            print ("Invalid Entry!!!")

        tasks=raw_input("Do you want to perform more task(y/n): ")
        if tasks == 'y':
            pass
        else:
            task=False
except IOError:
    print ("the path entered is invalid!!! ")
print ("Your job is done")