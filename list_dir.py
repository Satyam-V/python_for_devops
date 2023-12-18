####This program will ask for input as directory name once provided
####it will list the files if provided folder is present
####
# import os
# folders = input("Enter folder name or list of folders").split()
# for folder in folders:
#     try:
#         files = os.listdir(folder)
#     except FileNotFoundError:
#         print("Please provide a valid folder name, looks like this folder does not exist")
#         break
#     except PermissionError:
#         print("No access for this folder -" + folder)
#         break
#     print("Listing files for the folder -" + folder)
#     for file in files:
#         print(file)
####Writting above function in reusable way########
        #################
import os
####Exceptional handling part####
def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "Folder Not Found"
    except PermissionError:
        return None, "Permission denied"
    #######calling above function in main function to get desired output####
def main():
    folder_paths = input("Enter a list of folder paths seperated by spaces:").split()
    for folder_path in folder_paths:
        files, error_message = list_files_in_folder(folder_path)
        if files:
            print(f"Files in {folder_path}:")
            for file in  files:
                print(file)
        else:
            print(f"Error in{folder_path}:{error_message}")
if __name__ == "__main__":
    main()




        
