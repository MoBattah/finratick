import re
import csv
import urllib.request as urllib
import codecs
import json

# If you want to test against the recent changes, use these 3 lines:
#finra = 'http://tsp.finra.org/finra_org/ticksizepilot/TSPilotChanges.txt'
#col_program = 7
#col_symbol = 1

# ...and comment these three out. These three use today's current list
finra = 'http://tsp.finra.org/finra_org/ticksizepilot/TSPilotSecurities.txt'
col_program = 4
col_symbol = 0

#
csvfile = csv.reader(codecs.iterdecode(urllib.urlopen(finra), 'utf-8'),  delimiter='|')
prog = re.compile('G[23]')

x = [] # Temp hold for symbols

# Header/footer don't matter
for line in csvfile:
    if prog.match(line[col_program]):
        x.append(line[col_symbol])

# RobinHood API
rh = urllib.urlopen('https://api.robinhood.com/prices/?delayed=false&source=nls&symbols=' + ",".join(map(str, x)).replace(' ','+'))
jsonfile = json.load(rh)
for i, symbol in enumerate(jsonfile['results']):
    if symbol and float(symbol['price']) <= 2.00:
        print('%s @ $%s' % (x[i], symbol['price']))
        
