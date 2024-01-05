import csv
import sys
from csv import DictWriter

def main():
    check()

def check():
    if len(sys.argv) == 3:
        clean()
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command line arguments")

def clean():
    try:
        with open(sys.argv[1]) as file:
            table = []
            reader = csv.DictReader(file)
            for row in reader:
                lastname, firstname = row["name"].split(", ")
                house = row["house"]
                table.append({"first" : firstname, "last" : lastname, "house" : house})
            output(table)


    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv}")

def output(table):
    with open(sys.argv[2], "w") as csv2:
        writer = csv.DictWriter(csv2, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in table:
            if any(field.strip() for field in row):
                writer.writerow(row)



if __name__ == "__main__":
    main()