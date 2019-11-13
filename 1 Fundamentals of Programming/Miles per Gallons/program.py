import consts

oldMileage = float(input("Enter car mileage at time of last tank refill\n\n> "))
newMileage = float(input("Enter car mileage now\n\n> "))
gallons = float(input("Enter litres taken to fill the tank\n\n> ")) * consts.LITRES_TO_GALLONS()

print((newMileage - oldMileage) / gallons)
