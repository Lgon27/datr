import json


def chooseDate(priceFilter, distanceFilter):
    with open('dates.txt') as json_file:
        data = json.load(json_file)
        for p in data['dates']:
            print('Name: ' + p['name'])
            print('Cost: ' + p['cost'])
            print('Distance: ' + p['distance'])
            print('')

    print('You are going on a date that costs no more than ' + priceFilter +
          ' dollars ' 'and is a ' + distanceFilter + ' distance away')


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
        priceFilter = input(
            'What is your date budget (NOTE: this excludes the food budget)')
        distanceFilter = input(
            'How far are you willing to travel for this date? \n Close  (1) \n Medium (2)\n Far    (3) \n Epic   (4)')

        chooseDate(priceFilter, distanceFilter)

        # algorithm for randomization: first draf
        # for loop that reads from json should use filters when selecting. Store filtered elements in array.
        # Randomize from 0 - size of array pick date like that.
        # Similar concept for food.

    else:
        print('Incorrect input: Valid input is: \n Add Date  (1) \n Add Food  (2) \n Pick Date (3)\n Exit      (4)')

# Adding dates works now!
