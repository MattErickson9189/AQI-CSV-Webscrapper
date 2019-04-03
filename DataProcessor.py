import os
import csv

path = "./Data/"

years = ["1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000"]

desiredStates = ["North Dakota", "South Dakota", "Minnesota", "Wisconsin", "Iowa"]

for i in range(len(years)):

    for j in range(len(desiredStates)):
        #Defines what file we are looking for
        name = desiredStates[j] + years[i] + ".csv"
        #Loops through all the files in the data directory
        for (dirname,dirpath,filenames) in os.walk(path + years[i] + "/"):

            #Looks at the files themselves and not a list of files
            for files in filenames:
                #Opens the chosen file
                if files == name:
                    with open(path + years[i] + "/" + name, 'rU') as infile:
                        reader = csv.DictReader(infile)
                        data = {}

                        for row in reader:

                            for header, value in row.items():
                                #Trys to convert the csv file into a dictionary
                                try:
                                    data[header].append(value)
                                except:
                                    data[header] = [value]
                    mean = 0
                    count = 1
                    #Looks for data in the SO2 Mean header
                    for j in data['SO2 Mean 1-hr']:
                        try:
                            mean += float(j)
                            count += 1
                        except:
                            continue
                    #Calculates the average mean of all the counties with data
                    mean = mean/count

                    #Gets a tuple of the data collected and formats the mean to two decimal points
                    tuple = files, " mean: ", "{0:.2f}".format(mean)

                    #Converts the tuple to a string
                    message = ''.join(tuple)
                    print(message)
                    #Writes the data to its respective file
                    f = open(years[i]+".txt","a+")
                    f.write(message + "\n")

