#! python3
# readCensusExcel.py - Tabulates population and number of census tracts for
# each county.
import openpyxl
import pprint

print('Opening workbook...')

wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']

countyData = {}

# TODO: Fill in countyData with each county's population and tracts.

print('Reading rows...')

for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract.
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {'pop': 0, 'tracts': 0})

    countyData[state][county]['pop'] += pop
    countyData[state][county]['tracts'] += 1


# TODO: Open a new text file and write the contents of countyData to it.
f = open('countyData.txt', 'w')
f.write(pprint.pformat(countyData))
f.close()
