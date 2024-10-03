import csv
import requests

url = 'https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv'

with requests.Session() as s:
    download = s.get(url)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    my_list.pop(0)

    a=len(my_list)

    b=set()
    for row in my_list:
        if row[1] not in b:
            b.add(row[1])
    b=sorted(b)

    c=0
    for row in my_list:
        if row[1]=='Brooklyn':
            c=c+1
print(f"Total Number of Records: {a}\n")
print(f"Unique Boroughs: {b}\n")
print(f"Number of Records for Brooklyn Borough: {c}\n")
with open('/root/taxi_zone_output.txt', 'w') as f:
    f.write(f"Total Number of Records: {a}\n")
    f.write(f"Unique Boroughs: {b}\n")
    f.write(f"Number of Records for Brooklyn Borough: {c}\n")