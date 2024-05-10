# File Management in Object-Oriented Programming using Python
# I actually loved Java, or atleast OOP. So much so that I wanted to bring that interest to Python and see the similarities between Java and Python.
# One problem about switching from Java back to Python is using ; or {} by accident. 


import os
import shutil


class FileManager:
    def __init__(self):
        self.error = "" # Something that will stick by me for the rest of my programming journey is handling errors. Initializing an error and changing it based on what the error says is such helpful tool to remember. I gotta thank my Prof for introducing me to Error Handeling.


    error = ""
    def rename(self,old,new):

        oldold = os.path.abspath(old)

        if not os.path.exists(oldold):
            self.error = "Directory Does Not Exist"
            return False

        try:
            
            os.rename(oldold, new)
            return True
        except FileNotFoundError:
            self.error = "File Not Found"
            return False

    def folders(self,dir):
        # Working on it soon...
        if os.path.exists(dir):
            return True
        else:
            self.error = "Directory Does Not Exist"
            return False

    def create(self,dir):

        if not os.path.exists(dir):
            os.makedirs(dir)
            return True
        else:
            self.error = "Directory Does Exist"
            return False

    def delete(self,dir):

        if os.path.exists(dir):
            os.rmdir(dir)
            return True
        else:
            self.error = "Directory Does Exist"
            return False

    def move(self,dir,file_name):

        if os.path.exists(dir):
            if os.path.isfile(os.path.join(dir,file_name)):

                sec_dir = input("Where: ")
                if os.path.exists(sec_dir):
                    file_path = os.path.join(dir, file_name)
                    
                    dest_path = os.path.join(sec_dir, file_name)

                    shutil.move(file_path, dest_path)
                    return True
                            
                            

                else:
                    self.error = "Directory Does Not Exist"
                    return False
            else:
                self.error = "File: " + file_name + "Does Not Exist"        
        else:
            self.error = "Directory Does Not Exist"
            return False


    def list_files(self,dir):
        
        if os.path.exists(dir):
            with os.scandir(dir) as entries:
                for entry in entries:
                    print(entry.name)
                return True
        else:
            self.error = "Directory Does Not Exist"
            return False





if __name__ == "__main__":
    print("Welcome To File Management!\n")
    print("Here are the features: RENAME, FOLDERS, CREATE, DELETE, MOVE, and LIST")
    manager = FileManager()
    end = True
    while end:
        action = input(">")
        print("")
        action = str(action).upper()


        if action == "RENAME":
            old = input("Enter Old Name: ")
            new = input("Enter New Name: ")
            if manager.rename(old,new):
                print("")
                print("Success!")
            else:
                print(manager.error)
            print("")

        elif action == "FOLDERS":
            directory = input("Enter Directory: ")
            if manager.folders(directory):
                print("")
                print("Success!")
            else:
                print(manager.error)
            print("")

        elif action == "CREATE":
            directory = input("Enter Directory: ")
            if manager.create(directory):
                print("")
                print("Success!")
            else:
                print(manager.error)
            print("")

        elif action == "DELETE":
            directory = input("Enter Directory: ")
            if manager.delete(directory):
                print("")
                print("Success!")
            else:
                print(manager.error)
            print("")

        elif action == "MOVE":
            directory = input("Enter Directory: ")
            file = input("Enter File name: ")
            if manager.move(directory,file):
                print("")
                print("Success!")
            else:
                print(manager.error)
            print("")

        elif action == "LIST":
            directory = input("Enter Directory: ")
            if manager.list_files(directory):
                print("")
                print("Success!")
            else:
                print(manager.error)
            print("")

        elif action == "QUIT" or action == "Q":
            print("Have A Good Day!")
            print("")
            end = False

        else:
            continue
