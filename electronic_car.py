# electronic_car.py

from vehicle import Vehicle

       
class ElectronicCar(Vehicle):

    def __init__(self):
        super().__init__("Electronic Car")

    def diagnose(self):
        super().diagnose()
        problem_area = super().get_problem_area()
        symptoms = self.get_symptoms(problem_area)  # Update this line
        self.get_solution(problem_area, symptoms)

    def get_symptoms(self, problem_area):  # Add this method
        return super().get_symptoms(problem_area)  # Update this line

    def get_solution(self, problem_area, symptoms):
        if problem_area == '1':
            if symptoms == '1':
                print("Expert solution ....\n Practice efficient driving habits, maintain steady speeds, and consider external factors like temperature and terrain while planning trips")
            elif symptoms == '2':
                print("Expert solution ....\n Use higher-powered charging stations, avoid peak charging hours, and ensure proper charging cable integrity")
            elif symptoms == '3':
                print("Expert solution ....\n Follow proper charging practices, schedule regular battery health checks, and store the vehicle in a cool environment when not in use")
            elif symptoms == '4':
                print("consult an car expert or visit https://www.autozone.com/")
        elif problem_area == '2':
            if symptoms == '1':
                print("Expert solution ....\n Check and replace damaged charging cable or connector.")
            elif symptoms == '2':
                print("Expert solution ....\n Try a different charging station or power outlet.")
            elif symptoms == '3':
                print("Expert solution ....\nConsult charging station manual for troubleshooting.")
            elif symptoms == '4':
                print("Expert solution ....\n Inspect and replace faulty power outlet or charging cable.")
            elif symptoms == '5':
                print("consult an car expert or visit https://www.autozone.com/")
                    
        elif problem_area == '3':
            if symptoms == '1':
                print("Expert solution ....\n Check and clean the motor cooling system")
            elif symptoms == '2':
                print("Expert solution ....\nInspect and replace worn-out motor brushes")
            elif symptoms == '3':
                print("Expert solution ....\n Lubricate or replace faulty bearings in the electric motor.")
            elif symptoms == '4':
                print("Expert solution ....\n  Inspect and repair loose or damaged electrical connections.")
            elif symptoms == '5':
                print("consult an car expert or visit https://www.autozone.com/")
        elif problem_area == '4':
            if symptoms == '1':
                print("Expert solution ....\n  Check and replace worn brake pads or faulty regenerative braking system components.")
            elif symptoms == '2':
                print("Expert solution ....\n Inspect and repair or replace malfunctioning regenerative braking sensors or controllers.")
            elif symptoms == '3':
                print("Expert solution ....\n  Calibrate or reprogram regenerative braking system to ensure proper engagement and responsiveness")
            elif symptoms == '4':
                print("Expert solution ....\n   Inspect and repair or replace damaged brake rotors or regenerative braking system components causing the noise or vibration.")
            elif symptoms == '5':
                print("consult an car expert or visit https://www.autozone.com/")
        elif problem_area == '5':
            if symptoms == '1':
                print("Expert solution ....\n  Perform a system reboot by holding down the power button for 10 seconds")
            elif symptoms == '2':
                print("Expert solution ....\n Reset the electronic control unit (ECU) by disconnecting the car's battery for 15 minutes")
            elif symptoms == '3':
                print("Expert solution ....\n   Clear the device list on both the car and phone, then reconnect and pair them again")
            elif symptoms == '4':
                print("Expert solution ....\n   Clean the screen with a microfiber cloth and restart the car's infotainment system..")
            elif symptoms == '5':
                print("consult an car expert or visit https://www.autozone.com/")      
                                     