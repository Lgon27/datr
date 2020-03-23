import json
import random

# algorithm for randomization: first draf
# for loop that reads from json should use filters when selecting. Store filtered elements in array.
# Randomize from 0 - size of array pick date like that.
# Similar concept for food.


def chooseDate(priceFilter, distanceFilter):
    with open('dates.json') as json_file:
        data = json.load(json_file)
        acceptedDates = []
        for p in data['dates']:
            print('Name: ' + p['event'])
            print('Cost: ' + str(p['cost']))
            print('Distance: ' + str(p['distance']))
            print('')

            if(p['cost'] <= int(priceFilter) and p['distance'] <= int(distanceFilter)):
                acceptedDates.append(p)

        for p in acceptedDates:  # TODO, randomly pick from one of these elligable dates
            print(p)

        range = len(acceptedDates)
        exit = False
        while(True):
            date = acceptedDates[random.randrange(range)]
            print('Chosen Date: ' + date['event'])
            choice = input('Choose Again? Yes(1) No(2)')
            if(int(choice) == 2):
                break


def write_json(data, filename="dates.json"):  # Helper method to Write back to the file
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def addDate(name, cost, distance):  # Helper method that appends a JSON object to the date file
    with open("dates.json") as json_file:
        data = json.load(json_file)
        temp = data["dates"]
        y = {"event": name, "cost": int(cost), "distance": int(distance)}
        temp.append(y)

    write_json(data)


exit = False
while(exit != True):

    chooseActivity = input(
        'Hello, what action would you like to take: \n Add Date  (1) \n Add Food  (2) \n Pick Date (3)\n Delete    (4) \n Exit      (5)\n>>')

    if(chooseActivity == '5'):  # Exit
        exit = True
    elif(chooseActivity == '1'):  # Add Date
        dateName = input('What is the name of this date?')
        dateCost = input('What do you estimate the cost of this date to be?')
        dateDistance = input(
            'Is this date close(1) medium(2) far(3) epic(4) in distance?')
        print('Adding Date')

        addDate(dateName, dateCost, dateDistance)
    elif(chooseActivity == '2'):  # Add Food
        print('Adding Food')
    elif(chooseActivity == '3'):  # Select a random date TODO: pretty much all of this method
        print('Selecting Date')
        priceFilter = input(
            'What is your date budget (NOTE: this excludes the food budget)')
        distanceFilter = input(
            'How far are you willing to travel for this date? \n Close  (1) \n Medium (2)\n Far    (3) \n Epic   (4)')
        chooseDate(priceFilter, distanceFilter)
    elif(chooseActivity == '4'):
        print('Deleting ')
    else:
        print('Incorrect input: Valid input is: \n Add Date  (1) \n Add Food  (2) \n Pick Date (3)\n Exit      (4)')

# TODO: Learn how to make this application a GUI application
