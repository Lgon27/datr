import requests
from xml.etree import ElementTree
print('hello world')
r = requests.get('http://patcount.fiu.edu/garagecount.xml')
tree = ElementTree.fromstring(r.content)
print(tree[0])

for elem in tree.iter():
    print(elem.tag)
    print(elem.text)
