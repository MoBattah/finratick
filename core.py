import re
import csv
import urllib.request as urllib
import codecs
import json

# To test against the recent changes, use these 3 lines:   **Should be testing against recent changes** But not during build
# finra = 'http://tsp.finra.org/finra_org/ticksizepilot/TSPilotChanges.txt'
# col_program = 7
# col_symbol = 1

# ...and comment these three out. These three use today's current list
finra = 'http://tsp.finra.org/finra_org/ticksizepilot/TSPilotSecurities.txt'
col_program = 4
col_symbol = 0

#
csvfile = csv.reader(codecs.iterdecode(urllib.urlopen(finra), 'utf-8'), delimiter='|')
prog = re.compile('G[23]')

x = []  # Temp hold for symbols

# Header/footer don't matter
for line in csvfile:
    if prog.match(line[col_program]):
        x.append(line[col_symbol])

# RobinHood API
rh = urllib.urlopen(
    "https://api.robinhood.com/prices/?delayed=false&source=nls&symbols=" + ",".join(map(str, x)).replace(' ', '+'))
s = 1

while s < len(x):

    try:
        print(urllib.urlopen('https://api.robinhood.com/prices/?delayed=false&source=nls&symbols=' + x[s]).read().decode(
        'UTF-8'))
        s += 1
        #exceptions are going to keep getting thrown  here due to the txt file being not uniform
    except urllib.HTTPError:
        s += 5
        print(urllib.urlopen('https://api.robinhood.com/prices/?delayed=false&source=nls&symbols=' + x[s]).read().decode(
            'UTF-8'))
        s += 5
    except:
        break

#filter for $2 price point -- WORKING
for i, symbol in enumerate(jsonfile['results']):
    if symbol and float(symbol['price']) <= 2.00:
        print('%s @ $%s' % (x[i], symbol['price']))
