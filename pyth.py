import os
import platform

def clear_terminal():
    os.system("cls")
 
def calculate_tire_pressure(tire_type, rider_weight):
  

    if tire_type.lower() == "road":
        if rider_weight <= 60:
            return 90
        elif rider_weight <= 80:
            return 100
        else:
            return 110
    elif tire_type.lower() == "mountain":
        if rider_weight <= 60:
            return 25
        elif rider_weight <= 80:
            return 30
        else:
            return 35
    elif tire_type.lower() == "gravel":
        if rider_weight <= 60:
            return 40
        elif rider_weight <= 80:
            return 45
        else:
            return 50
    else:
        return "Invalid tire type"

# Clear the terminal
clear_terminal()

# Get user input
tire_type = input("Enter the tire type (road, mountain, or gravel): ")
rider_weight = float(input("Enter your weight in kilograms: "))

# Calculate and print the recommended tire pressure
recommended_pressure = calculate_tire_pressure(tire_type, rider_weight)
if isinstance(recommended_pressure, str):
    print(recommended_pressure)
else:
    print(f"The recommended tire pressure is {recommended_pressure} psi.")
