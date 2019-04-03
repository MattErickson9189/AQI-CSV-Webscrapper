import os
import pandas as pd

path = "./Data/"

#years = ["1980","1982","1984","1986","1988","1990","1992","1994","1996","1998","2000"]
years = ["1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000"]

# count = 0
#
# colnames = 'N02 Annual Mean'
# data = pd.read_csv(path + years[0] +"/Alabama1980.csv", names=colnames)
#print(data)
    # for i in range(len(years)):
#     for (dirpath,dirnames,filenames) in os.walk(path + years[i] + "/"):
#         for files in filenames:
#

import csv

# open the file in universal line ending mode

# for i in range(1):
#     for(dirname,dirpath,filenames) in os.walk(path + years[i] + "/"):
#         count = 0
#         for files in filenames:
#             try:
#                 with open(path + years[0] + "/" + files, 'rU') as infile:
#                   # read the file as a dictionary for each row ({header : value})
#                   reader = csv.DictReader(infile)
#                   data = {}
#                   for row in reader:
#                     for header, value in row.items():
#                       try:
#                         data[header].append(value)
#                       except KeyError:
#                         data[header] = [value]
#
#                 mean = 0
#
#                 for j in data['NO2 Mean 1-hr']:
#                     try:
#                         mean += float(j)
#                         count += 1
#                     except:
#                         print("Mean Not Counted for: ", files)
#
#                 print("Mean: ",mean)
#             except:
#                 continue

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

