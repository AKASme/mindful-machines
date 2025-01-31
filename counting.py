import csv
counter = 0
with open("results.csv", "r+") as res:
    reader = csv.reader(res)
    for i in reader:
        if i[1] == i[2]:
            counter += 1
print(counter)

#17/20 correct