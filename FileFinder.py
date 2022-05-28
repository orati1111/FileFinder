#Importing python modules.
import glob
import sys
import os


if len(sys.argv) != 3: #Checks if the script was given the correct arguments.
    print("Usage: [Path] [File extention(txt for example)]") #Prints out how to use.
    sys.exit(0)#Closes the script.

#Variables
path = sys.argv[1] #First argument given = the path of dir
ext = sys.argv[2] # Second argument given = the file extenion


#def
def check_if_dir(dir):#Chceks if the given path is valid.
    if(os.path.isdir(dir)): # gets the path given and checks if its a directory.
        return True # returns True if it is.
    else: # Returns false if not.
        return False

def iterate(path,ext): #Main function, given path and file extention, iterates through all files.
    if(check_if_dir(path)):#Sends the path to the dir checker - True? Continue
        glob_path = glob.glob(f"{path}/**/*.{ext}",recursive=True) #Declaring glob - globing the path given for files with the given ext recursivly.
        file_counter = 0 #Files counter.
        for i in range(len(glob_path)):#Goes through all files in glob list.
            file_path = glob_path[i]#Getting the file in a given list position.
            print(file_path)#Prints the file.
            file_counter += 1 #Adding 1 to the file counter.
        
        print(f"\nAmount of file with the given .{ext} file extention: {file_counter}")#Prints the amount of files that was found.
            

    elif(not check_if_dir(path)):#The dir checker returned False.
        if(os.path.isfile(path)):#Checks if the given path is a file.
            print("This is a file.")#Prints to the user that the path given is a file.
        else:
            print("Invalid directory path.")#Couldnt find the directory

#Main
if __name__ == "__main__":#Starts the program.
    iterate(path,ext)#Calls the main function.
