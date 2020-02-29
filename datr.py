import requests
from xml.etree import ElementTree
print('hello world')
r = requests.get('http://patcount.fiu.edu/garagecount.xml')
tree = ElementTree.fromstring(r.content)
print(tree[0])

for elem in tree.iter():
    print(elem.tag)
    print(elem.text)

distanceFilter = input('How far are you willing to drive (in miles): ')
print(distanceFilter)
budgetFilter = input('How much are you willing to spend (in USD): ')
print(budgetFilter)
