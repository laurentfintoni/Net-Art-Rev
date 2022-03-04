import re
import csv
import pandas as pd

path = './MoMA_data/'

import csv
with open(path+'Artworks.csv','r') as fin, open (path+'modern_artworks.csv','w') as modern, open (path+'cont_artworks.csv','w') as cont:

    m_writer = csv.writer(modern, delimiter=',' )
    c_writer = csv.writer(cont, delimiter=',' )
    m_writer.writerow(['Title','Artist','ConstituentID','ArtistBio','Nationality','BeginDate','EndDate','Gender','Date','Medium','Dimensions','CreditLine','AccessionNumber','Classification','Department','DateAcquired','Cataloged','ObjectID','URL','ThumbnailURL','Circumference (cm)','Depth (cm)','Diameter (cm)','Height (cm)','Length (cm)','Weight (kg)','Width (cm)','Seat Height (cm)','Duration (sec.)'])
    c_writer.writerow(['Title','Artist','ConstituentID','ArtistBio','Nationality','BeginDate','EndDate','Gender','Date','Medium','Dimensions','CreditLine','AccessionNumber','Classification','Department','DateAcquired','Cataloged','ObjectID','URL','ThumbnailURL','Circumference (cm)','Depth (cm)','Diameter (cm)','Height (cm)','Length (cm)','Weight (kg)','Width (cm)','Seat Height (cm)','Duration (sec.)'])


    for row in csv.reader(fin, delimiter=','):

        if str(row[8]) != "":
            if  re.match('.*\d\d\d\d.*', row[8]):
                year = re.findall(r'\d\d\d\d', row[8])
                row[8] = year[0],
                if int(year[0]) < 1980:
                    m_writer.writerow(row) 
                else:
                    c_writer.writerow(row)
            
            elif "century" in str(row[8]):
                m_writer.writerow(row) 
            else:
                row[8] = "missing"
                date = row[5]
                if  len(date)>=3 and date[1] == "0":
                    date = "missing"
                    row[6] = "missing"

                    m_writer.writerow(row) #modern has also those artworks by artist having unknown birth-- death date
                
                c_writer.writerow(row)


""" 
path = './MoMA_data/'

import csv
with open(path+'Artworks.csv','r') as fin, open (path+'cleaned_artworks.csv','w') as fout:

    writer = csv.writer(fout, delimiter=',' )
    writer.writerow(['Title','Artist','ConstituentID','ArtistBio','Nationality','BeginDate','EndDate','Gender','Date','Medium','Dimensions','CreditLine','AccessionNumber','Classification','Department','DateAcquired','Cataloged','ObjectID','URL','ThumbnailURL','Circumference (cm)','Depth (cm)','Diameter (cm)','Height (cm)','Length (cm)','Weight (kg)','Width (cm)','Seat Height (cm)','Duration (sec.)'])

    for row in csv.reader(fin, delimiter=','):

        if str(row[8]) != "":
            if  re.match('.*\d\d\d\d.*', row[8]):
                year = re.findall(r'\d\d\d\d', row[8])
                if int(year[0]) >= 1983:

                    if (row[14] =='Media and Performance') or (row[14]=='Photography'):

                        writer.writerow(row) 

 """                
            

                
