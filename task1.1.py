#Your Mood Today
import random

days_week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
mood =  ["Happy","Sad","Angry", "Tired","Frustrated","Mad","Exausted"]

random.shuffle(mood)
for i in range(len(days_week)): 
    print("On " + days_week[i] + " I was feeling " + mood[i])
    