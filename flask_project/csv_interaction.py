# Importing relevant modules
import csv

# # Reading from CSV file
# with open("login_detaiils.txt", "r") as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     line_counter = 0
#     for row in csv_reader:
#         if line_counter == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_counter =+ 1
#         print(f'The username is {csv_reader["username"]} and the password is {row["password"]}.')
#         line_counter += 1

with open("login_detaiils.txt", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:

