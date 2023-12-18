import os
def update_file(filepath, key, value):

    filepath = '/home/satyam/Python_projects/read_write_file.py'
    with open(filepath, "r") as file:
        lines = file.readlines()
    with open(filepath, "w") as file:  
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)
update_file("filepath", "putkey", "putvalue")
    
