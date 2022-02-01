"Calvin Widholm"
"lab3.py"
"Problem: Calculate total vehicles on all roads, average vehicles per road, and average
"vehicles on each road"
"I certify this is my own work and I discussed with nobody- Calvin Widholm"

def traffic():
    num_roads = eval(input("How many roads were surveyed?"))
    total_cars = 0
    for i in range(1, num_roads + 1, 1):
        road_total_cars = 0
        print("How many days was road", i, "surveyed?")
        days = eval(input(""))
        for j in range(1, days + 1, 1):
            print("How many cars traveled on day", j, "?")
            cars = eval(input(""))
            total_cars = total_cars + cars
            road_total_cars = road_total_cars + cars
        avg_road_i = road_total_cars / days
        round_avg_road_i = round(avg_road_i, 2)
        print("Road", i, "average vehicles per day:", round_avg_road_i)
    print("Total number of vehicles traveled on all roads:", total_cars)
    avg_per_road = total_cars / num_roads
    round_avg_per_road = round(avg_per_road, 2)
    print("Average number of vehicles per road:", round_avg_per_road)

