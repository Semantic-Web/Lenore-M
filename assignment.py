import csv
from collections import defaultdict
reader = csv.DictReader(open('C:\Users\Lenore\Desktop\School\MSITM\Python\datagovdatasetsviewmetrics.csv'))
organizations = defaultdict(int)
for row in reader:
    organizations[row["Organization Name"]] += int(row["Views per Month"])
    
for organization, views in sorted(organizations.iteritems(), key=lambda (k, v): (-v, k))[:10]:
    print organization, views