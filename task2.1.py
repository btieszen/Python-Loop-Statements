#Double Scoop with Nested Loops
#Task 1: Your Mood Tracker 
import random

days_week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
mood =  ["Happy","Sad","Angry", "Tired","Frustrated","Mad","Exausted"]
time = ["Morning", "Afternoon", "Evening"]
random.shuffle(mood)

for i in range(len(days_week)): 
    for x in range(len(time)):
        print("On " + days_week[i] + " " + time[x] + " I was feeling " + mood[x])
            