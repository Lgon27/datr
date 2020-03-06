import requests
import json
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
        dateName = input('What is the name of this date?')
        dateCost = input('What do you estimate the cost of this date to be?')
        dateDistance = input(
            'Is this date close(1) medium(2) far(3) epic(4) in distance?')
        print('Adding Date')
        data = {}
        data['dates'] = []
        data['dates'].append({
            'name': dateName,
            'cost': dateCost,
            'distance': dateDistance
        })
        with open('dates.txt', 'w') as outfile:
            json.dump(data, outfile)
    elif(chooseActivity == '2'):
        print('Adding Food')
    elif(chooseActivity == '3'):
        print('Selecting Date')
        with open('dates.txt') as json_file:
            data = json.load(json_file)
            for p in data['dates']:
                print('Name: ' + p['name'])
                print('Cost: ' + p['cost'])
                print('Distance: ' + p['distance'])
                print('')
    else:
        print('Incorrect input: Valid input is: \n Add Date  (1) \n Add Food  (2) \n Pick Date (3)\n Exit      (4)')

# Adding dates works now!
