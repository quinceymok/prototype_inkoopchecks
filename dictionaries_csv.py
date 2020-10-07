import csv

# Read csv
with open('csv/Dataexcelcsv.csv' , 'r') as Dataexcelcsv_csv:
    reader = csv.DictReader(Dataexcelcsv_csv, delimiter= ';')

    for row in reader:
        print(row['Inkoopvolume'])

# Parse csv

# write new csv

