#Secret Message Decoder
#potential problems - trying to access a non-existent file would return error
#renaming similar files could overwrite files

import os
def rename_files():
    #(1) get file names
    file_list = os.listdir(r"C:\Users\smith526\OneDrive - BYU Office 365\Python\prank")
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir(r"C:\Users\smith526\OneDrive - BYU Office 365\Python\prank")
    #(2) for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
    
rename_files()
