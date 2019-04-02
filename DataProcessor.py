import os
import pandas as pd

path = "./Data/"

years = ["1980","1982","1984","1986","1988","1990","1992","1994","1996","1998","2000"]
#
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

for i in range(len(years)):
    for(dirname,dirpath,filenames) in os.walk(path + years[i] + "/"):
        count = 0
        for files in filenames:
            try:
                with open(path + years[0] + "/" + files, 'rU') as infile:
                  # read the file as a dictionary for each row ({header : value})
                  reader = csv.DictReader(infile)
                  data = {}
                  for row in reader:
                    for header, value in row.items():
                      try:
                        data[header].append(value)
                      except KeyError:
                        data[header] = [value]

                mean = 0

                for j in data['NO2 Mean 1-hr']:
                    try:
                        mean += float(j)
                    except:
                        continue

                print(mean)
            except:
                continue
