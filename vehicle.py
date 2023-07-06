# vehicle.py
import time
import os
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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Vehicle:
    
    def __init__(self, type):
        self.type = type

    def diagnose(self):
        print(f"Diagnosing {self.type}...\n\n")

    def get_problem_area(self):
       
        if self.type == "Electronic Car":
            problem_areas = ["1.Battery Degradation", "2. Charging Failure", "3. Electric Motor Issues","4. Regenerative Braking Problems","5.Software Glitches",]
        elif self.type == "Hybrid Car":
            problem_areas = ["1.Battery Issues", "2.Regenerative Braking System", "3.Engine and Powertrain","4.Electric Motor and Inverter","5 Hybrid System Integration",]
        elif self.type == "Hydrogen Fuel Cell Car":
            problem_areas = ["1.Hydrogen Fuel Cell Stack Failure", "2. Hydrogen Storage and Leakage", "3.Fuel Cell Cooling System Failure","4. Hydrogen Infrastructure Limitations",]
        elif self.type == "Sport Car":
            problem_areas = ["1.Engine Issues", "2. Transmission Problems", "3.Suspension and Steering Issues","4. Electrical Problems:","5. other"]
        elif self.type == "Luxury Car":
            problem_areas = ["1.Air Suspension Issues:", "2.Electrical System Problems:", "3.Brake System Faults:","4.Engine Performance Issues","5. other"]
       
        else:
            problem_areas = []
      
        print(f"Please choose a problem area for {self.type}:\n")
        for area in problem_areas:
            print(area)
        problem_area = input("Enter your choice : ")
        
        clear_screen()
        welcome_screen()
        return problem_area
  
    def get_symptoms(self, problem_area):
     
        if self.type == "Electronic Car":
            if problem_area == '1':
                symptoms = ["1.Reduced driving range", "2. increased charging time", "3.frequent battery capacity loss" ]
            elif problem_area == '2':
                symptoms = ["1.Charging interruption", "2.  Slow charging speed", "3.  Charging error message", "4. Charging doesn't start"]
            elif problem_area == '3':
                symptoms = ["1.Overheating", "2.Loss of powe", "3. Unusual noise ", "4. Intermittent operation"]
            elif problem_area == '4':
                symptoms = ["1.Decreased regenerative braking efficiency", "2.Regenerative braking failure", "3. Inconsistent regenerative braking engagement ", "4.Excessive noise or vibration during regenerative braking."]
            elif problem_area == '5':
                symptoms = ["1.Screen Freeze", "2. Erratic Acceleration", "3.Bluetooth Connection Failure ", "4.Unresponsive Touchscreen","5 other"]
            else:
                symptoms = []
        elif self.type == "Hybrid Car":
            
            if problem_area == '1':
                symptoms = ["1.  Reduced Electric Range", "2. Frequent Check Hybrid System Warning", "3. Inconsistent Battery Charging", "4.Sudden Power Loss",]
            elif problem_area == '2':
                symptoms = ["1. Brake Pedal Feels Spongy", "2. Ineffective Regenerative Braking", "3.Regenerative Braking Delay", "4.Unexpected Jerking Sensation",]
            elif problem_area == '3':
                symptoms = ["1. Engine Misfires", "2. Loss of Power in Gas Mode", "3. Irregular Gear Shifting","4. Engine Overheating",]
            elif problem_area == '4':
                symptoms = ["1.Whining Noise during Acceleration", "2.Electric Motor Not Engaging", "3.Inverter Overheating","4.Electric Motor Overheating",]
            elif problem_area == '5':
                symptoms = ["1. Hybrid System Warning Light", "2. Powertrain Integration Failure", "3.Unintended Hybrid Mode Changes","4. Erratic Energy Flow Display",]
         
            else:
                symptoms = []
        elif self.type == "Hydrogen Fuel Cell Car":
            if problem_area == '1':
                symptoms = ["1. Decreased Power Output", "2.  Unstable Fuel Cell Voltage", "3Excessive Heat Generation", "4.Irregular Fuel Cell Stack Shutdown"]
            elif problem_area == '2':
                symptoms = ["1.  Reduced Hydrogen Pressure", "2. Increased Hydrogen Consumption", "3. Hydrogen Odor or Smell", "4. Insufficient Hydrogen Range",]
            elif problem_area == '3':
                symptoms = ["1.Overheating Warning or Alarm", "2. Increased Operating Temperature", "3.Inconsistent Cooling Performance", "4. Reduced Power Output during High Temperatures",]
            elif problem_area == '4':
                symptoms = ["1. Limited Refueling Stations", "2.  Inadequate Hydrogen Production", "3. Costly Hydrogen Fuel", "4.  Uneven Regional Availability",]
            else:
                symptoms = []
           
        elif self.type == "Sport Car":
            if problem_area == '1':
                symptoms = ["1. Engine Misfire", "2.Engine Overheating", "3. Loss of Power", "4.  Engine Stalling"]
            elif problem_area == '2':
                symptoms = ["1. Delayed Shifting", "2. Slipping Gears", "3. Transmission Fluid Leaks", "4.Rough Shifting"]
            elif problem_area == '3':
                symptoms = ["1. Excessive Vibrations", "2. Steering Wheel Misalignment", "3.: Noisy Suspension","4. Bumpy Ride"]
            elif problem_area == '3':
                symptoms = ["1. Dead Battery", "2.  Malfunctioning Electronics", "3.Dim or Flickering Lights","4.Power Window Failuree"]
            else:
                symptoms = []
        elif self.type == "Luxury Car":
            if problem_area == '1':
                symptoms = ["1. Car Leaning to One Side", "2.Rough or Unstable Ride", "3. Suspension Warning Light", "4. : Air Suspension Failure"]
            elif problem_area == '2':
                symptoms = ["1.Malfunctioning Infotainment System ","2.Brake Warning Light", "3. Battery Drainage", "4. Electrical Short Circuit"]
            elif problem_area == '3':
                symptoms = ["1. Spongy Brake Pedal", "2.Brake Noise or Vibration", "3. Brake Warning Light","4. ABS System Failure"]
            elif problem_area == '4':
                symptoms = ["1.  Engine Misfire", "2. Rough Idle", "3.  Loss of Power","4.Engine Overheating"]
            else:
                symptoms = []
        else:
            symptoms = []
          
        print(f"Please choose a symptom for {problem_area}:")
        for symptom in symptoms:
            print(symptom)
        selected_symptom = input("Enter your choice : ")
        return selected_symptom
   