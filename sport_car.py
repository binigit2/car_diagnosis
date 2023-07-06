# sport_car.py

from vehicle import Vehicle

class SportCar(Vehicle):
    def __init__(self):
        super().__init__("Sport Car")

    def diagnose(self):
        super().diagnose()
        problem_area = super().get_problem_area()
        symptoms = super().get_symptoms(problem_area)
        self.get_solution(problem_area, symptoms)

    def get_solution(self, problem_area, symptoms):
       if problem_area=="1":    
            if symptoms == '1':
                print(" Expert solution...\n Replace faulty spark plugs and ignition coils")
            elif symptoms == '2':
                print(" Expert solution...\n Check coolant levels and replace a faulty thermostat if necessary.")
            elif symptoms == '3':
                print(" Expert solution...\n Inspect and clean the fuel injectors, air filters, and throttle body.")
            elif symptoms == '4':
                print("  Expert solution...\nClean the idle control valve and check for any vacuum leaks.")
            else:
                print("Invalid choice. Please try again.")
       elif problem_area=="2":    
            if symptoms == '1':
                print(" Expert solution...\n Replace worn-out transmission fluid and check for any damaged solenoids.")
            elif symptoms == '2':
                print(" Expert solution...\n  Inspect and replace a worn-out clutch or torque converter.")
            elif symptoms == '3':
                print(" Expert solution...\n  Identify and fix any leaks in the transmission system, and refill with the recommended fluid")
            elif symptoms == '4':
                print("  Expert solution...\n: Perform a transmission flush and recalibrate the shift points.")
            else:
                print("Invalid choice. Please try again.")
       elif problem_area=="3":    
            if symptoms == '1':
                print(" Expert solution...\n Inspect and replace worn-out or damaged suspension components such as shocks, struts, and bushings.")
            elif symptoms == '2':
                print(" Expert solution...\n  Perform a wheel alignment to correct steering drift or off-center steering.")
            elif symptoms == '3':
                print(" Expert solution...\n   Inspect and replace worn-out or damaged suspension parts such as control arms, ball joints, or sway bar links.")
            elif symptoms == '4':
                print("  Expert solution...\n: Check tire pressure, balance, and rotate tires regularly, and replace worn-out tires.")
            else:
                print("Invalid choice. Please try again.")
       elif problem_area=="4":    
            if symptoms == '1':
                print(" Expert solution...\nJump-start the car or replace the battery if necessary.")
            elif symptoms == '2':
                print(" Expert solution...\n  : Inspect and replace any faulty fuses, relays, or damaged wiring connections.")
            elif symptoms == '3':
                print(" Expert solution...\n  Replace faulty bulbs or check the alternator for potential issues..")
            elif symptoms == '4':
                print("  Expert solution...\n: Inspect and replace malfunctioning window regulators or switches.")
            else:
                print("Invalid choice. Please try again.")
                
