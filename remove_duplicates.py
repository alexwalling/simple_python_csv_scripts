import csv

print 'make sure to use input.csv and remove.csv'

data = csv.reader(open('input.csv', 'r'), delimiter = ',')
remove = csv.reader(open('remove.csv', 'r'), delimiter = ',')

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
