# Importing relevant modules
import csv

# Reading from CSV file
def read_csv():
    with open("login_details.txt", "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            return dict(row)


# Writing to CSV file
def write_csv(new_username, new_password):
    with open("login_details.txt", "w") as csv_file:
       csv_writer = csv.writer(csv_file, delimiter=',')
       csv_writer.writerow(["username", "password"])
       csv_writer.writerow([new_username, new_password])

write_csv("admin", "password123")
read_csv()