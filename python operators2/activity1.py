# Smart School Day Planner
print("===Smart School Day Planner===")
print("Answer 3 quick questions and I will plan your day!\n")

day = input("what day is it?(Monday to Sunday): ").strip().capitalize()
weather = input("what weather is it?(sunny / rainy / cloudy): ").strip().lower()
homework = input("is your homework done? (yes / no): ").strip().lower()

print()
print(f"===Your Plan for {day}===")
print("-" * 35)
#Topic 1 -- if-elif-else: classify the day
if day in("Saturday" , "Sunday"):
    print("Day type  : Weekend - enjoy your free time!")
elif day == "Monday":
    print("Day type   :Weekend - first day of the week. Pack up your weekly planner.")
elif day == "Friday":
    print("Day type  :Weekend - last day of the school day. Return your libary books.")