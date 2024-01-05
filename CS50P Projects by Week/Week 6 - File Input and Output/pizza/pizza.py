import csv
import tabulate
import sys

def main():
    read_csv()

def read_csv():
    if len(sys.argv) != 2:
        sys.exit("Too many command line arguments")
    else:
        end = sys.argv[1].split(".")
        if end[1] == "csv":
            try:
                with open(sys.argv[1]) as file:
                    table = []
                    reader = csv.reader(file)
                    for row in reader:
                        table.append(row)
                    print(tabulate.tabulate(table[1:], table[0], tablefmt = "grid"))
            except FileNotFoundError:
                sys.exit("File does not exist")
        else:
            sys.exit("Not a csv file")

if __name__ == "__main__":
    main()

