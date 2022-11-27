import requests
res = requests.get('https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json')
data = res.json()
list = ['Hulk', 'Thanos', 'Captain America']
dict = {}
for heroe in data:
    if heroe['name'] in list:
        heroe_dict = {heroe['name']: heroe['powerstats']['intelligence']}
        intelligence_dict ={v: k for k, v in heroe_dict.items()}
        dict.update(intelligence_dict)
print(dict[max(dict)])
