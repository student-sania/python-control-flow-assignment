# Logical Problems
# Problem no: 1
num = int(input("Enter a number:"))
if num > 0:
    print("number is positive")
elif num < 0:
    print("number is negative")
else:
    print("number is zero")
    
# Problem no: 2
age = int(input("Enter your age:"))
if age <= 12:
    print("you are a chid")
elif  13 <=age <=19:
    print("you are a teenager")
elif 20 <= age <= 50:
    print("you are an adult")
elif age >= 51:
    print("you are a senior citizen")
else:
    print("invalid number")
    
# Problem no: 3
num1= int(input("Enter a number:"))
num2=int(input("Enter a number:"))
if num1 > num2:
    print(num1, "is a greater number")
elif num1 < num2:
    print(num2, "is a greater number")
else:
    print(f"{num1} and {num2} both are equal")

# Problem no:4
year = int(input("Enter a year:"))
if (year % 4 ==0 and year %100 !=0) or (year % 400 ==0):
    print(f"{year} is a leap year")
else:
     print(f'{year} is not a leap year') 
      
# Problem no: 5
n1=int(input("Enter a number:"))
n2=int(input("Enter a number:"))
n3=int(input("Enter a number:"))
max_number=max(n1,n2,n3)
print("max number is:", max_number)
min_number=min(n1,n2,n3)
print("min number is:", min_number)

# Problem no:6
score=int(input("Enter your exam score:"))
if 90 <= score <= 100:
    print("A Grade")
elif 80 <= score <=89:
    print("B Grade")
elif 70 <= score <= 79:
    print("C Grade")
elif 60 <= score <=69:
    print("D Grade")    
elif score < 60:
    print("F Grade")
else:
    print("invalid number")   
    
# Simple Practical Problem
# Problem no: 1 
for i in range(1):
    quantity=int(input("Enter quanity:"))
    price=int(input("Enter price:"))
    total_cost=quantity*price

    if total_cost >1000:
        discount=total_cost*0.1
        final_total_cost=total_cost-discount
        print(f"total cost of item with disscount is: {final_total_cost}")
    elif total_cost <=1000:
        print("total_cost of item is:",total_cost)
        print("no disscount")
    else:
        print("invalid number")

#  Problem no: 2
temperature= int(input("Enter temperature:"))
if temperature < 20:
    print("you should wear a jacket") 
else:
    print("don't need to wear a jacket")

#  Problem no: 3
side1= int(input("Enter side1 length of triangle:"))
side2= int(input("Enter side2 length of triangle:"))
side3= int(input("Enter side3 length of triangle:"))
if side1 == side2 == side3:
  print("equilateral")
elif side1==side2 or side1==side3 or side2==side3:
  print("isosceles")
elif side1 != side2 !=side3 and side1!=side3:
  print("scalene")
  
# Problem no:4
Balance= 20000
PIN_Code= 3056
User_PIN = int(input("Enter a PIN:")) 
User_Balance=int(input("Enter your balance:"))
if User_PIN == PIN_Code:
    if User_Balance <= Balance:
        print("PIN is Verify")
        print("you are allowed to withdraw money")
else:
    print("please try again")  
  
# Problem  no: 5
month= int(input("Enter a month:"))
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12 :
    print("number of days in this month is 31")
elif month == 4 or month==6 or month==9 or month==11:
    print("number of days in this month is 30")
elif month == 2:
    print("number of days in this month is 28")
else:
    print("invalid number! please try again")
    
#  Problem no:6
month = int(input("enter a month:"))
year = int(input("Enter a year:"))
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12 :
    print("number of days in this month is 31")
elif month == 4 or month==6 or month==9 or month==11:
    print("number of days in this month is 30")
elif month == 2:
    print("number of days in this month is 28")
else:
    print("invalid number")  
if (year % 4 ==0 and year %100 !=0) or (year % 400 ==0):
    print(f"{year} is a leap year")
else:
     print(f'{year} is not a leap year')

# Healthy Lifestyle
# problem no: 1
age = int(input("What is your age? "))
weight = int(input("What is your weight in kilograms? "))
activity_level = input("What is your activity level? (sedentary, lightly active, moderately active, very active): ")

if activity_level == "sedentary":
    calorie_goal = weight * 22
elif activity_level == "lightly active":
    calorie_goal = weight * 25
elif activity_level == "moderately active":
    calorie_goal = weight * 28
elif activity_level == "very active":
    calorie_goal = weight * 30
else:
    print("Invalid activity level entered. Please try again.")
    exit()

if age < 18:
    calorie_goal += 300
elif age >= 18 and age <= 30:
    calorie_goal += 200
elif age > 30 and age <= 50:
    calorie_goal += 100
else:
    calorie_goal += 50
print("Your daily calorie goal is:", calorie_goal)    

# Problem no: 3
weight = int(input("What is your weight in kilograms? "))
hydration_level = input("What is your desired level of hydration? (light, moderate, intense) ")

if hydration_level.lower() == "light":
    water_intake = weight * 0.03
elif hydration_level.lower() == "moderate":
    water_intake = weight * 0.04
elif hydration_level.lower() == "intense":
    water_intake = weight * 0.05
else:
    print("Invalid input. Please choose from light, moderate, or intense.")
    exit()

print("you should drink approximately", water_intake, "liters of water throughout the day.")

# Time Management
# Problem no: 1
todo_list = []
# function
def add_task(task, due_date, priority):
    task_details = {
        "task": task,
        "due_date": due_date,
        "priority": priority
    }
    todo_list.append(task_details)

task = input("Enter the task: ")
due_date = input("Enter the due date: ")
priority = input("Enter the priority (urgent, important, less important): ")

add_task(task, due_date, priority)
print("To-Do List:")
for task_details in todo_list:
    if task_details["priority"].lower() == "urgent":
        print("Urgent:", task_details["task"], "- Due Date:", task_details["due_date"])
    elif task_details["priority"].lower() == "important":
        print("Important:", task_details["task"], "- Due Date:", task_details["due_date"])
    elif task_details["priority"].lower() == "less important":
        print("Less Important:", task_details["task"], "- Due Date:", task_details["due_date"])
    else:
        print("Invalid priority:", task_details["task"], "- Due Date:", task_details["due_date"])

# Problem no: 2
import time
# Function
def start_pomodoro():
    print("Pomodoro started!")
    for i in range(4):
        print("Work for 25 minutes.")
        time.sleep(1500)  
        print("Take a 5-minute break.")
        time.sleep(300)  
    print("Pomodoro completed!")

start = input("Are you ready to start the Pomodoro timer? (yes/no): ")

if start.lower() == "yes":
    start_pomodoro()
else:
    print("Okay, try next time!")

# Problem n0: 3
def find_common_time(users):
    available_time_slots = []
    for user in users:
        available_time_slots.append(get_available_time_slots(user))

    common_time_slots = set(available_time_slots[0])
    for slots in available_time_slots[1:]:
        common_time_slots = common_time_slots.intersection(slots)
    if common_time_slots:
        print("The common meeting time(s) are:")
        for time_slot in common_time_slots:
            print(time_slot)
    else:
        print("No common meeting time found.")

def get_available_time_slots(user):
    if user == "User1":
        return ["9:00 AM - 10:00 AM", "1:00 PM - 2:00 PM", "4:00 PM - 5:00 PM"]
    elif user == "User2":
        return ["11:00 AM - 12:00 PM", "2:00 PM - 3:00 PM", "4:00 PM - 5:00 PM"]
    elif user == "User3":
        return ["9:00 AM - 10:00 AM", "12:00 PM - 1:00 PM", "3:00 PM - 4:00 PM"]
    else:
        return []

users = ["User1", "User2", "User3"]
find_common_time(users)
   