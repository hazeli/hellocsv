import csv

with open('config.csv') as f:
    reader = csv.reader(f)
    heading = next(reader)
    columntoname = {}
    nametocolumn = {}
    i = 0
    for name in heading:
        columntoname[i] = name
        nametocolumn[name] = [i] if name not in nametocolumn else nametocolumn[name] + [i]
        i += 1
    print(columntoname)
    print(nametocolumn)
