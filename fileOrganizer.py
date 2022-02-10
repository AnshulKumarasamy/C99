import os
import shutil

#To write the name of the directory here that needs to be organized
path = input("Enter the name of the directory to be organized: ")

#To list all the files inside the path
list_of_files = os.listdir(path)

#This will go through each and every file 
for file in list_of_files:
    name, ext = os.path.splitext(file)

    #this is going to store the extention type
    ext = ext[1:]


    if ext == '':
        continue

    #this will move the file to the directory where the name ext already exists
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)
    
    #this will create a new directory if the directory does not exist
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)

