#Part 1 ask how much many minutes of homework
homework= int(input("enter homework time: "))
free_time = input("do have free time?")

#Part 2 decide if it is a long or a short session
if homework > 60:

    plan = "That is a long homework session."
else:
    plan = "That is a short homework session."

#Part 3 ask if you have a free time
if free_time == "yes":
    print("enjoy your free time!")

#Part 4 Print the homework time
print("homework time in minutes:", homework)
print("plan:", plan)


