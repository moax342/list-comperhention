#Exercise 26.1 create a new list ad double the numbers

numbers = [1,1,2,3,5,8,13,21,34,55]
squared_numbers = [n*n for n in numbers]
print(squared_numbers)

#Exercise 26.2 create a new list that has only even numbers

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [n for n in numbers if n % 2 == 0]
print(result)

#Exercise 26.3 create a dictionary from a sentence
sentence = "what is the airspeed velocity of on unladen swallow?"
words=sentence.split(" ")

result={n:len(n) for n in words}

print(result)

#Exercise 26.4 create a dictionary from a dictionary by converting a degree from celcius to farenheight

weather = {
    "Monday":12,
    "Tuesday":14,
    "Wednesday":15,
    "Thursday":14,
    "Friday":21,
    "Saturday":22,
    "Sunday":24
}

weather_f = {key:(value*9/5)+32 for (key,value) in weather.items()}
print(weather_f)

