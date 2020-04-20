# datr
This project was inspired by my innability to decide on date ideas for my girlfriend and I. As a result
I decided that the best way to fix this problem was to automate it.

# project details
The premise of this software is to create an application that stores potential date ideas and later chooses
a date for you based on price and distance. Additionally it should also provide suggestions for dining.

# learning goals
This project is partly oriented to allow me to learn more about python syntax and libraries. In the past i've worked on smaller projects using python. However, this is my first
time diving into application development with python.

# storing the data locally
One of the first challenges I ran across was how I would store data. I figured I had three choices to choose from: JSON, XML, or CSV. Each of these file types came with
their own disadvantages. 

JSON (JavaScript Object Notation) is used to represent hierarchical data and makes use of commas, curly braces, and brackets. Pro's:
This data format supports hierarchical data and is incredibly useful for web applications due to similar notation to JavaScript objects. Json also tends to be smaller
than XML.

It seems like updating a JSON file you already have is one of the more difficult problems sorrounding JSON

XML (extensible markup language) is a human readable hierarchical data tye introduced in 1996. It's syntax makes use of angle brackets and backslashes
to denote hierarchy. Pro's: This format is very human readable. However, it is probably the largest of the three because of it's syntax.

CSV (Comma Seperated Values) is essentially a list of elements separated by commas. A major advantage of CSV is it's small file size which makes it the most compact of the three. 
However, this format is not very versatile and essentially requires a custom parser to organize your data. Additionally, the data in a CSV isn't hierarchichal. 

For this project I decided that I would use JSON. I like JSON's hierarchical data structure and the fact that I can parse it's data using the json library in python. Additionally,
If i ever choose to extend this project into some kind of web application, JSON is already a great choice.

However, local storage using JSON can be a tricky. To understand this concept better I used the following tutorial: 
https://www.youtube.com/watch?v=9N6a-VLBa2I

https://www.youtube.com/watch?v=QrRcZmDaO_I : Video on how to appends

As per the above video, I was able to the JSON file by storing the context of the JSON file to a
list and appending a new json object to that list before writing the content of the list back to
the JSON file. Having to store the entire JSON file in a list just to append 1 object is fairly
inneficient in terms of space with space complexity being O(N) were N is the number of dates a user has stored. However, for the purpose of this project this is probably okay as the average user is probably not storing hundreds or thousands of date ideas here.

# choosing dates
Randomly picking a date was pretty straight forward. The user enters criteria for the date and the algorithm
searches through the JSON file for dates that meet that given criteria. Elligable dates are stored in a list.
Afterwards, using a random number the algorithm picks one of the elligable dates out of the list and presents it
to the user. Lastly, the user is given the option to pick again.

# deleting dates & foods
Deleting the dates was fairly straight forward. The user enters the name of a date or of a food to delete. The software then calls a helper method which stores the contents of either the food or dates json file in a list. It then searches that list until the value which matches the parameter that the user entered is found. Once found it pops that value from the list and writes the contents of the list back to the JSON file.

# sorting dates & foods
Ideally I would like to provide a function so that the contents of the JSON files are displayed in a sorted manner to the user. I imagine this might be beneficial when I eventually transition this application from a terminal based application to some kind of user interface.

# UI Work
I began working on the UI using the python tkinter library. Below are some mockups of the initial idea
i had for the UI. However, this is subject to change as the project evolves.

# UI Mockups 
![Home Image](/Mockups/Home.png)
![Home Image](/Mockups/Manage_Dates.png)
![Home Image](/Mockups/Manage_Foods.png)

# future goals
The initial scope of this project is limited to a simple command line application that stores date and dining data locally.
However, I am now working to make it a gui application
Ultimately the end goal of this project would be to incorporate some kind of technology or algorithm that identifies date ideas automatically without the user having to enter their own.

https://ezinearticles.com/?CSV-vs-XML-vs-JSON---Which-is-the-Best-Response-Data-Format?&id=4073117