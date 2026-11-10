# Part 1 ask today temperature
temperature = int(input("enter the temperature in celius: "))

 # Part 2 decide between a jacket or a t-shirt
if temperature > 20:
    outfit = "jacket"
    print("It is a cold day today")
    print("wear a", outfit)

# Part 3 ask is it is raining today
is_raining = input("is it raining today? (yes/no): ")

# Part 3 add an umbrella if it is raining
if is_raining == "yes":
    print("Bring an umbrella!")

# Part 4 ask for the wind speed
wind_speed = int(input("enter the wind speed in km/h: "))

#Part 5 decide whether the windbreaker is needed
if wind_speed > 30:
    need_windbreaker = "yes"
    print("It is windy today")
    print("wear a windbreaker over your", outfit)
else:
    need_windbreaker = "no"
    print("It is calm today")
    print("no needed to wear a windbreaker over your", outfit)
    