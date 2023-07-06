# luxury_car.py

from vehicle import Vehicle

class LuxuryCar(Vehicle):
    def __init__(self):
        super().__init__("Luxury Car")

    def diagnose(self):
        super().diagnose()
        problem_area = super().get_problem_area()
        symptoms = super().get_symptoms(problem_area)
        self.get_solution(problem_area, symptoms)

    def get_solution(self, problem_area, symptoms):
      if problem_area=="1":    
            if symptoms == '1':
                print(" Expert solution...\n Inspect and replace faulty air springs or struts.")
            elif symptoms == '2':
                print(" Expert solution...\n Check for leaks in the air suspension system and replace any damaged components.")
            elif symptoms == '3':
                print(" Expert solution...\n :Perform a diagnostic scan to identify the specific issue and repair accordingly.")
            elif symptoms == '4':
                print("  Expert solution...\nReset the suspension system by disconnecting the battery for a few minutes or replace a malfunctioning compressor.")
            else:
                print("Invalid choice. Please try again.")
      elif problem_area=="2":    
            if symptoms == '1':
                print(" Expert solution...\n  Update the software or replace a faulty head unit")
            elif symptoms == '2':
                print(" Expert solution...\nCheck and replace damaged seat motors, switches, or wiring.")
            elif symptoms == '3':
                print(" Expert solution...\n Inspect for any parasitic draws and fix the underlying issue causing excessive battery drain.")
            elif symptoms == '4':
                print("  Expert solution...\n: Identify and repair any damaged wiring or faulty electrical components causing the short circuit..")
            else:
                print("Invalid choice. Please try again.")
      elif problem_area=="3":    
            if symptoms == '1':
                print(" Expert solution...\n : Bleed the brake system and check for any leaks or air bubbles.")
            elif symptoms == '2':
                print(" Expert solution...\n   Inspect and replace worn-out brake pads, rotors, or calipers.")
            elif symptoms == '3':
                print(" Expert solution...\n   Check the brake fluid level and pressure, and replace any faulty sensors or switches.")
            elif symptoms == '4':
                print("  Expert solution...\n:  Perform a diagnostic scan to identify the specific ABS component causing the issue and replace it if necessary.")
            else:
                print("Invalid choice. Please try again.")
      elif problem_area=="4":    
            if symptoms == '1':
                print(" Expert solution...\nReplace faulty spark plugs and ignition coils.")
            elif symptoms == '2':
                print(" Expert solution...\n   Clean the throttle body and idle control valve, and check for any vacuum leaks.")
            elif symptoms == '3':
                print(" Expert solution...\n  nspect and clean the fuel injectors, air filters, and throttle body.")
            elif symptoms == '4':
                print("  Expert solution...\n:  Check coolant levels, replace a faulty thermostat, or inspect the radiator for any blockages or leaks.")
            else:
                print("Invalid choice. Please try again.")
                
