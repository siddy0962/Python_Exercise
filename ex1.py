# Exercise #1:  A Basic Aircraft

# Exercise 1, part 1
print("# Exercise 1, part 1")
aircrafts = {"x": 10, "y": 20}

print(aircrafts["x"])
print(aircrafts["y"])


# Exercise 1, part 2
print("\n# Exercise 1, part 2")
Aircrafts = ["aircraft_1", "aircraft_2", "aircraft_3", "aircraft_4", "aircraft_5"]
coordinates = [20,25, 10,22, 55,66, 77,78, 71,80]

var = 0
for aircraft in Aircrafts:
        print(aircraft, "coordinates are: ", coordinates[var], coordinates[var+1])
        var+= 2
