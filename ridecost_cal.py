dist_travel = float(input("Enter distance you travelled a day in kilometers: "))
cost_diesel = float(input("Enter cost of diesel or petrol: "))
fuel_avg = float(input("Enter average of vehicle: "))
fuel_consume = dist_travel/fuel_avg
print("fuel consumed in a day= ",fuel_consume,"litres")
cost_day = cost_diesel * fuel_consume
print("Cost of driving per day to office= ",cost_day,"INR")