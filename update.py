import requests
import json 
import csv
import os

os.remove(r"C:\Users\capnp\Desktop\Projects\Data Science\Covid-19\data\latest_stats.csv")
os.remove(r"C:\Users\capnp\Desktop\Projects\Data Science\Covid-19\data\date_wise_totals.csv")
os.remove(r"C:\Users\capnp\Desktop\Projects\Data Science\Covid-19\data\state_date_wise.csv")

latest_stats = requests.get('https://api.rootnet.in/covid19-in/stats/latest')
date_wise = requests.get('https://api.rootnet.in/covid19-in/stats/history')

x = latest_stats.json()
y = date_wise.json()

f = csv.writer(open(r"C:\Users\capnp\Desktop\Projects\Data Science\Covid-19\data\latest_stats.csv", "a"))
g = csv.writer(open(r"C:\Users\capnp\Desktop\Projects\Data Science\Covid-19\data\date_wise_totals.csv", "a"))
h = csv.writer(open(r"C:\Users\capnp\Desktop\Projects\Data Science\Covid-19\data\state_date_wise.csv", "a"))

f.writerow(["Location", "TotalConfirmed", "Discharged", "Deaths"])
g.writerow(["Day", "TotalConfirmed", "Discharged", "Deaths"])
h.writerow((["Day", "Location", "TotalConfirmed", "Discharged", "Deaths"]))

for ele in x['data']['regional']:
    f.writerow ([ele['loc'], 
                ele['totalConfirmed'],
                ele['discharged'],
                ele['deaths']])

for i in y['data']:
    g.writerow ([i['day'],
                i['summary']['total'],
                i['summary']['discharged'],
                i['summary']['deaths']])
    for j in i['regional']:
        h.writerow([i['day'],
                    j['loc'],
                    j['totalConfirmed'],
                    j['discharged'],
                    j['deaths']])
