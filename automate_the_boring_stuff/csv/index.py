#   CSV - Comma separated values
#   tsv - Tabs separated values
import csv
fileObj = open('example.csv')
csvReader = csv.reader(fileObj)

result = list(csvReader)  # Easiest way to see the returned object


for n, row in enumerate(result):
    print(f'Row #{str(n)} {str(row)}')
    ...

#   WRITER
outputFile = open('output.csv', 'w', newline='')
# ARGUMENTS->  (delimiter='\t', lineterminator='\n\n') -> Instead of commas, seperate with tabs and double lines
outputWriter = csv.writer(outputFile),
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1, 2, 3.141592, 4])
outputFile.close()
