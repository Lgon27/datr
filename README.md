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

XML (extensible markup language) is a human readable hierarchical data tye introduced in 1996. It's syntax makes use of angle brackets and backslashes
to denote hierarchy. Pro's: This format is very human readable. However, it is probably the largest of the three because of it's syntax.

CSV (Comma Seperated Values) is essentially a list of elements separated by commas. A major advantage of CSV is it's small file size which makes it the most compact of the three. 
However, this format is not very versatile and essentially requires a custom parser to organize your data. Additionally, the data in a CSV isn't hierarchichal. 

For this project I decided that I would use JSON. I like JSON's hierarchical data structure and the fact that I can parse it's data using the json library in python. Additionally,
If i ever choose to extend this project into some kind of web application, JSON is already a great choice.

However, local storage using JSON can be a tricky. To understand this concept better I used the following tutorial: 
https://www.youtube.com/watch?v=9N6a-VLBa2I



# future goals
The initial scope of this project is limited to a simple command line application that stores date and dining data locally.
In the future it might be expanded to allow online storage and backup of this data. 
Ultimately the end goal of this project would be to incorporate some kind of technology or algorithm that identifies date ideas
automatically without the user having to enter their own.

https://ezinearticles.com/?CSV-vs-XML-vs-JSON---Which-is-the-Best-Response-Data-Format?&id=4073117