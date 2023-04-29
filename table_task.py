import csv

FILENAME = "users.csv"
FIELDS = ["name", "surname", "age", "occupation", "hobby", "uni"]


def saveCSV(data, filename):
    try:
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(data)
            print(f"Data saved to {filename}.")
    except IOError:
        print(f"Error saving data to {filename}.")

def readCSV(filename):
    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row["name"], "-", row["age"])
    except IOError:
        print(f"Error reading data from {filename}.")

def main():
    us_name=input("enter your name pls-> ")
    us_surname=input("enter your surname pls-> ")
    us_age=input("enter your age pls-> ")
    us_occupation=input("enter your occupation pls-> ")
    us_hobby=input("enter your hobby pls-> ")
    us_uni=input("enter your uni name pls-> ")
    users = [
    {"name": us_name, "surname": us_surname, "age": us_age, "occupation": us_occupation, "hobby": us_hobby, "uni": us_uni}
    ]
    print("User information:")
    print(f"Name: {us_name}")
    print(f"Surname: {us_surname}")
    print(f"Age: {us_age}")
    print(f"Occupation: {us_occupation}")
    print(f"Hobby: {us_hobby}")
    print(f"University: {us_uni}")
    
    while True:
        print('1 - save: 2 - load')
        action = input('action->')
        if action == 'save':
            saveCSV(users, FILENAME)
        elif action == 'load':
            readCSV(FILENAME)
        else:
            print('Action not found!')


if __name__ == "__main__":
    main()
