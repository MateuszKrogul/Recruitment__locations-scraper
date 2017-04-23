import requests
from Geographic_transformation import G_transform
import os.path
import json
import csv

class Entity_scraper:
    def __init__(self,category,name, url):
        self.category = category
        self.name = name
        self.url=url

        if not os.path.exists("%s.txt"%name):
            response = requests.get(self.url).text
            print("Receiving %s data"%self.name)
            with open("%s.txt"%name, "w") as f:
                f.write(response)
        else:
            with open("%s.txt"%name, "r") as f:
                response = f.read()
        self.js_data = json.loads(response)

    def prepare_data(self):
        self.data = []
        for entity in self.js_data['features']:
            if "NAZWA" in entity['properties']:
                name = entity['properties']['NAZWA']
            elif 'NR_PRZYST' in entity['properties']:
                name = entity['properties']['NR_PRZYST']
            else:
                name = "brak"
            x = entity['properties']['X']
            y = entity['properties']['Y']
            x,y = map(lambda x: float(x.replace(",",".")),[x,y])
            x,y = G_transform(x,y)

            self.data.append([name,x,y])

    def save_data_to_csv(self,filename):
        if os.path.exists("%s.csv" % filename):
            mode = 'a'
        else:
            mode = 'w'
        with open(filename+".csv", mode, newline='') as f:
            writer = csv.writer(f, delimiter=';', quotechar='',
                                quoting=csv.QUOTE_NONE,
                                dialect='excel')
            for i in self.data:
                writer.writerow([self.category,self.name,*i])

