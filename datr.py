import requests
from xml.etree import ElementTree
print('hello world')
r = requests.get('http://patcount.fiu.edu/garagecount.xml')
tree = ElementTree.fromstring(r.content)
print(tree[0])

for elem in tree.iter():
    print(elem.tag)
    print(elem.text)


exit = False
while(exit != True):
    chooseActivity = input(
        'Hello, what action would you like to take: \n Add Date  (1) \n Add Food  (2) \n Pick Date (3)\n Exit      (4) \n>>')

    if(chooseActivity == '4'):
        exit = True
    elif(chooseActivity == '1'):
        print('Adding Date')
    elif(chooseActivity == '2'):
        print('Adding Food')
    elif(chooseActivity == '3'):
        print('Selecting Date')
    else:
        print('Incorrect input: Valid input is: \n Add Date  (1) \n Add Food  (2) \n Pick Date (3)\n Exit      (4)')
