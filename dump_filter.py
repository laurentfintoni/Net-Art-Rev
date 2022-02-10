
import re
import csv

artists_list = set()

path = './MoMA_data/'

with open(path+'cleaned_artworks.csv','r') as myfile:
    for row in csv.reader(myfile, delimiter=','):
        if row[1] not in artists_list:
           artists_list.add(row[1])
    print(len(artists_list))



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
            

                
