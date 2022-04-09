from vnaapi import anritsu
import csv

csv_file = open('vnadata.csv', 'w')
mywriter = csv.writer(csv_file)

vna = anritsu("192.168.56.1")

# stop and measure data
datapoint = vna.getData()   # called when positioner stops to meausure data
for idx, tr in enumerate(datapoint):
    csv_file.write(f"{x1},{y1},tr{idx+1},")
    mywriter.writerow(tr)

# move motor

# func move(params)
# for (xdir, ydir):
csv_file.close()    # finished vna data collection