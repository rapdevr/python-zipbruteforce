from ast import Pass
import zipfile
from tqdm import tqdm

#file names
pwd_filename = '/Users/rishi/Documents/Github/zipbruteforce-python/passwords_list.txt'
zip_filename = '/Users/rishi/Documents/Github/zipbruteforce-python/b2b.zip'

#read passeords file in binary mode
with open(pwd_filename, "rb") as passwords:

    #convert asll the pwds into list
    passwords_list = passwords.readlines()

    #total no of pwds
    total_passwords = len(passwords_list)

    #load thr xip
    my_zip_file = zipfile.ZipFile(zip_filename)
    for index, password in enumerate(passwords_list):
        try:
            my_zip_file.extractall(path="Extracted Folder", pwd=password.strip())
            print("\n +++++ SUCCESS +++++")
            print("Password Found: ", password.decode().strip())
            break

    # but if it fails
        except:
            print(f".........Scan complete {round((index/total_passwords)*100, 2)}%")
            print(f"Trying password {password.decode().strip()} ")
            continue