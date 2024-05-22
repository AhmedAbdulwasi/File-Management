# File Management in Object-Oriented Programming using Python
# I loved Java, or at least OOP. So much so that I wanted to bring that interest to Python and see the similarities between Java and Python.
# One problem about switching from Java back to Python is using; or {} by accident. 


import os
import shutil


class FileManager:
    def __init__(self):
        self.error = "" 


    error = ""
    def gorename(self,old,new):

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

        if os.path.exists(dir):
            with os.scandir(dir) as entries:
                for entry in entries:
                    if (entry.name.endswith(".txt")):
                        new_dir = os.path.join(dir, "Texts")
                        os.makedirs(new_dir, exist_ok=True)
                        shutil.move(entry.path, new_dir)
                    elif (entry.name.endswith(".png") or entry.name.endswith(".jpg") or entry.name.endswith(".jpeg")):
                        new_dir = os.path.join(dir, "Images")
                        os.makedirs(new_dir, exist_ok=True)
                        shutil.move(entry.path, new_dir)
                    elif (entry.name.endswith(".pdf") or entry.name.endswith(".docx")):
                        new_dir = os.path.join(dir, "Documents")
                        os.makedirs(new_dir, exist_ok=True)
                        shutil.move(entry.path, new_dir)
                    elif (entry.name.endswith(".mov") or entry.name.endswith(".mp4") or entry.name.endswith(".wav") or entry.name.endswith(".mp3")):
                        new_dir = os.path.join(dir, "Videos")
                        os.makedirs(new_dir, exist_ok=True)
                        shutil.move(entry.path, new_dir)
                    else:
                        new_dir = os.path.join(dir, "Other")
                        os.makedirs(new_dir, exist_ok=True)
                        shutil.move(entry.path, new_dir)
                return True
        else:
            self.error = "Directory Does Not Exist"
            return False

    def create(self,dir,file,bol):
        if bol:
            if os.path.exists(dir):
                os.makedirs(os.path.join(dir,file))
                return True
            else:
                self.error = "Directory Does Exist"
                return False
        else: 
            if os.path.exists(dir):
                
                path = os.path.join(dir,f"{file}")
                with open(path,"w") as s:
                    s.write("")
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

    def gomove(self,dir,file_name):

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
    print("Note: Q to quit")
    manager = FileManager()
    end = True
    while end:
        action = input(">")
        print("")
        action = str(action).upper()


        if action == "RENAME":
            old = input("Enter Old Name: ")
            new = input("Enter New Name: ")
            if manager.gorename(old,new):
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
            directory = input("Enter Directory (Where?): ")
            file = input("Enter File/Folder: ")
            bol = input("Create a Folder (Y/N)? ")
            if bol.upper() == "Y" or bol.upper == "N" or bol.upper() == "YES" or bol.upper() == "NO":
                if manager.create(directory,file,True):
                    print("")
                    print("Success!")
                else:
                    print(manager.error)
            elif bol.upper() == "N" or bol.upper() == "NO":
                if manager.create(directory,file,False):
                    print("")
                    print("Success!")
                else:
                    print(manager.error)
            else:
                print("Wrong input.")
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
            file = input("Enter File: ")
            if manager.gomove(directory,file):
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

# THE END
