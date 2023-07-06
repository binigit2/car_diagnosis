# main.py

import os
from vehicle import Vehicle 
from electronic_car import ElectronicCar
from Hybrid_car import HybridCar
from Hydrogen_fuel_cell_car import HydrogenFuelCellCar
from sport_car import SportCar
from Luxury_car import LuxuryCar
def display_car():
    car = '''''
                    .------.
   " WELL COME TO   :|||"""`.`.
    CAR DIAGNOSIS " :|||     7.`.
.===+===+===+===+===||`----L7'-`7`---.._
[]  "EXPERT SYSTEM" || ==       |       """-.
[]...._____.........||........../ _____ ____|
c\____/,---.\_       ||_________/ /,---.\_  _/
    /_,-,-. \ `._____|__________||  ,-. \ \_[
     /\ `-' /                    /\ `-' /
       `---'                       `---'
    '''''''''
    print(car)
def welcome_screen():
    display_car()
    print("Enjoy your time here!")


# Main program


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        
        welcome_screen()
        print("Please choose a type of car:\n")
        print("1. Electronic Car")
        print("2. Hybrid Car")
        print("3. Hydrogen Fuel Cell Car")
        print("4. Sport Car")
        print("5. Luxury Car")
        choice = input("Enter your choice (1-5): ")
        clear_screen()
        welcome_screen()
        if choice == '1':
            electronic_car = ElectronicCar()
            electronic_car.diagnose()
        elif choice == '2':
            hybrid_car = HybridCar()
            hybrid_car.diagnose()
        elif choice == '3':
            hydrogen_fuel_cell_car = HydrogenFuelCellCar()
            hydrogen_fuel_cell_car.diagnose()
        elif choice == '4':
            sport_car = SportCar()
            sport_car.diagnose()
        elif choice == '5':
            luxury_car = LuxuryCar()
            luxury_car.diagnose()
        else:
            print("Invalid choice. Please try again.")
        
        continue_choice = input("Do you want to continue? (y/n): ")
        if continue_choice.lower() != 'y':
            break
        clear_screen()
        welcome_screen()
if __name__ == "__main__":
 main()
