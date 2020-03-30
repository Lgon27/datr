import json
import random

# algorithm for randomization: first draf
# for loop that reads from json should use filters when selecting. Store filtered elements in array.
# Randomize from 0 - size of array pick date like that.
# Similar concept for food.


def chooseDate(priceFilter, distanceFilter, foodCostFilter):
    acceptedDates = []
    acceptedFoods = []
    with open('dates.json') as json_file:
        data = json.load(json_file)

        for p in data['dates']:
            print('Name: ' + p['event'])
            print('Cost: ' + str(p['cost']))
            print('Distance: ' + str(p['distance']))
            print('')

            if(p['cost'] <= int(priceFilter) and p['distance'] <= int(distanceFilter)):
                acceptedDates.append(p)

        for p in acceptedDates:
            print(p)

    with open('food.json') as json_file:
        data = json.load(json_file)

        for p in data['foods']:
            print('Name: ' + p['food'])
            print('Cost: ' + str(p['costPerPerson']))

            if(p['costPerPerson'] <= int(foodCostFilter)):
                acceptedFoods.append(p)

        for p in acceptedFoods:
            print(p)

        dateRange = len(acceptedDates)
        foodRange = len(acceptedFoods)
        exit = False
        while(True):
            date = acceptedDates[random.randrange(dateRange)]
            food = acceptedFoods[random.randrange(foodRange)]
            print('Chosen Date: ' + date['event'] +
                  ' Chosen Food: ' + food['food'])
            choice = input('Choose Again? Yes(1) No(2)')
            if(int(choice) == 2):
                break


# Helper methods to Write back to the file
def write_jsonDate(data, filename="dates.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def write_jsonFood(data, filename="food.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def addDate(name, cost, distance):  # Helper method that appends a JSON object to the date file
    with open("dates.json") as json_file:
        data = json.load(json_file)
        temp = data["dates"]
        y = {"event": name, "cost": int(cost), "distance": int(distance)}
        temp.append(y)

    write_jsonDate(data)


def deleteDate(name):
    with open("dates.json") as json_file:
        datat = json.load(json_file)
        data = datat["dates"]

        for i in range(len(data)):
            if data[i]["event"] == name:
                data.pop(i)
                break

    write_jsonDate(datat)


def deleteFood(food):  # TODO: finish this method
    with open("food.json") as json_file:
        datat = json.load(json_file)
        data = datat["foods"]

        for i in range(len(data)):
            if data[i]["food"] == food:
                data.pop(i)
                break

    write_jsonFood(datat)


def addFood(name, cost):  # Helper method that appends a JSON object to the food file
    with open("food.json") as json_file:
        data = json.load(json_file)
        temp = data["foods"]
        y = {"food": name, "costPerPerson": int(
            cost)}
        temp.append(y)

    write_jsonFood(data)


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
        foodName = input('What is the name of this meal?')
        foodCost = input(
            'What do you estimate the cost of this meal to be per person? ')
        print('Adding Food')

        addFood(foodName, foodCost)
    elif(chooseActivity == '3'):  # Select a random date TODO: pretty much all of this method
        print('Selecting Date')
        priceFilter = input(
            'What is your date budget (NOTE: this excludes the food budget)')
        distanceFilter = input(
            'How far are you willing to travel for this date? \n Close  (1) \n Medium (2)\n Far    (3) \n Epic   (4)')
        foodCostFilter = input('How much are you willing to spend on food?')
        chooseDate(priceFilter, distanceFilter, foodCostFilter)
    elif(chooseActivity == '4'):
        deleteChoice = input(
            "What would you like to delete? \n Date  (1) \n Food  (2)")

        if(deleteChoice == '1'):
            datetodelete = input("What date would you like to delete?")
            deleteDate(datetodelete)
        elif(deleteChoice == '2'):
            foodtodelete = input("What food would you like to delete")
            deleteFood(foodtodelete)
        else:
            print('Invalid input. Must be (1) or (2)')
    else:
        print('Incorrect input: Valid input is: \n Add Date  (1) \n Add Food  (2) \n Pick Date (3)\n Exit      (4)')

# TODO: Learn how to make this application a GUI application
# TODO: Delete Date & Delete Food
