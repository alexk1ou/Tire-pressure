import os
import platform

def clear_terminal():
    
    operating_system = platform.system()
    if operating_system == "Windows":
        os.system("cls")
    else:
        os.system("clear")

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

class Car:
    def __init__(self, style, fuel_type):
       
        self.style = style
        self.fuel_type = fuel_type
        
    def get_details(self):
       
        return f"This is a {self.style} car that runs on {self.fuel_type}."

class Bike:
    def __init__(self, style):
       
        self.style = style
        
    def get_details(self):
       
        return f"This is a {self.style} bike."

# Clear the terminal
clear_terminal()

# Get user input
tire_type = input("Enter the tire type (road, mountain, or gravel): ")
rider_weight = float(input("Enter your vehicules weight in kilograms: "))
vehicle_type = input(" Car or Bike : ").lower()
if vehicle_type == "car":
    style = input("What do you drive? (e.g., sedan, 4x4, coupe): ")
    fuel_type = input("What fuel type you use ? (e.g., diesel, petrol): ")
    vehicle = Car(style, fuel_type)
elif vehicle_type == "bike":
    style = input("What is your bike style ? (e.g., lowrider, sport, racing): ")
    vehicle = Bike(style)
else:
    print("Invalid vehicle type.")
    exit()

# Calculate and print the recommended tire pressure
recommended_pressure = calculate_tire_pressure(tire_type, rider_weight)
if isinstance(recommended_pressure, str):
    print(recommended_pressure)
else:
    print(f"The recommended tire pressure is {recommended_pressure} psi.")

# Print vehicle details
print(vehicle.get_details())
