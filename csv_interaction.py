# Importing relevant modules
import csv


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
        # Inserting dictionary values
        csv_writer.writerow([new_username, new_password])

# Calling functions to test
write_csv("admin", "password123")
read_csv()
