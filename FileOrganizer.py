import os
import shutil


# Main Function

def main():

    # Initial prompt

    print("This script will arrange files into new folders according to their"\
          " file type.\n")

    # Asking user for the target folder

    targetFolder = input("Enter the directory for the target folder:\n")


    # Getting list of the files in the target folder

    filesList = os.listdir(targetFolder)


    # Looping through the list of files

    for file in filesList:

        if os.path.isfile(targetFolder + "\\" + file):
            # Getting file extension and directory

            fileSplit = os.path.splitext(file)
            extension = fileSplit[1]
            currentFileLocation = targetFolder + "\\" + file


            # Naming organized folder

            newFolderDir = targetFolder + "\\" + extension[1:]
            newFileDir = newFolderDir + "\\" + file

            # Creating organized folder if it does not exist

            if not os.path.exists(newFolderDir):
                os.makedirs(newFolderDir)

                # Putting file into newly made directory

                shutil.move(currentFileLocation, newFileDir)

            # Putting file into previously made directory

            else:
                shutil.move(currentFileLocation, newFileDir)


# When the scipt is run

if __name__ == "__main__":
    main()
