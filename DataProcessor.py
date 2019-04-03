import os
import csv

path = "./Data/"

years = ["1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000"]

desiredStates = ["North Dakota", "South Dakota", "Minnesota", "Wisconsin", "Iowa"]

for i in range(len(years)):
    MNname = "Minnesota" + years[i] + ".csv"
    for (dirname,dirpath,filenames) in os.walk(path + years[i] + "/"):
        for files in filenames:
            if files == MNname:
                with open(path + years[i] + "/" + MNname, 'rU') as infile:
                    reader = csv.DictReader(infile)
                    data = {}
                    for row in reader:
                        for header, value in row.items():
                            try:
                                data[header].append(value)
                            except:
                                data[header] = [value]
                mean = 0
                count = 0
                for j in data['SO2 Mean 1-hr']:
                    try:
                        mean += float(j)
                        count += 1
                    except:
                        continue
                mean = mean/count
                print(files, " mean: ", mean)

