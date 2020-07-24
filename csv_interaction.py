# Importing relevant modules
import csv
from passlib import *
import hashlib

# Reading from CSV file
def read_csv():
    # Using with open to file so it is automatically closed
    with open("login_details.txt", "r") as csv_file:
        # Opening CSV file as a dictionary
        csv_reader = csv.DictReader(csv_file)
        # Getting the first row of dictionary values and returning them
        for row in csv_reader:
            return dict(row)


# Writing to CSV file
def write_csv(new_username, new_password):
    # Using with open to file so it is automatically closed
    with open("login_details.txt", "w") as csv_file:
        # Writing to file created previously
        csv_writer = csv.writer(csv_file, delimiter=',')
        # Inserting dictionary keys
        csv_writer.writerow(["username", "password"])
        # Encrypting password using function
        new_password = encrypt_input(new_password)
        # Inserting dictionary values
        csv_writer.writerow([new_username, new_password])


# Encrypting password with passlib module
def encrypt_input(password):
    # Encoding initial variable
    password = password.encode('utf-8')
    # Hashing password
    hash_object = hashlib.sha256(password)
    password_encrypted = hash_object.hexdigest()
    return password_encrypted


# Decrypting password with passlib module
def password_decrypt():
    pass

# Calling functions to test
write_csv("admin", "password123")
read_csv()
