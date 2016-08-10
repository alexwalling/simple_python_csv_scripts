import csv

print 'make sure to use file1.csv and file2.csv'

data = csv.reader(open('file1.csv', 'r'), delimiter = ',')
remove = csv.reader(open('file2.csv', 'r'), delimiter = ',')

writer = csv.writer(open('output.csv', 'w'), delimiter=',')

emails = set()
for row in remove:
	key = row[0].lower()
	emails.add( key )

for row in data:
	key = row[0].lower()
	if key not in emails:
		writer.writerow(row)
		emails.add( key )
