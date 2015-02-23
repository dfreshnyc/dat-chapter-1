import csv, operator
from collections import defaultdict

played = 0
top_plays_title = defaultdict(int)


#read the csvfile, if column 3 is 1981 - keep a counter

read_file = csv.reader(open('rock.csv','r'))

for row in read_file:
	if row[2] == '1981':
		played += 1

print "Number of songs released in 1981: %r" % played

#read the rock.csv and create new Dict file with COMBINED and PlayCount columns

with open('rock.csv','rb') as csvfile:
	new_file = csv.DictReader(csvfile, delimiter=',')
	for row in new_file:
		if row["PlayCount"]:
			top_plays_title[row["COMBINED"]] += int(row["PlayCount"])

#sort the new Dict by PlayCount
	
sorted_songs = sorted(top_plays_title.items(), key=operator.itemgetter(1), reverse = True)

#print top 20 of DICT of the COMBINED column

for n in range(0,20):
	print sorted_songs[n][0]

