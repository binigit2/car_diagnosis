# hybrid_car.py

from vehicle import Vehicle

class HybridCar(Vehicle):
    def __init__(self):
        super().__init__("Hybrid Car")

    def diagnose(self):
        super().diagnose()
        problem_area = super().get_problem_area()
        symptoms = super().get_symptoms(problem_area)
        self.get_solution(problem_area, symptoms)

    def get_solution(self, problem_area, symptoms):
        if problem_area == '1':
            if symptoms == '1':
                print("EXpert system solution.....\n  Replace or recondition the battery pack as needed.")
            elif symptoms == '2':
                print("EXpert system solution.....\n  : Perform a diagnostic scan to identify the specific issue and address it accordingly.")
            elif symptoms == '3':
                print("EXpert system solution.....\n   Check and repair the charging system components, including the charging port and cables..")
            elif symptoms == '4':
                print("EXpert system solution.....\n  Inspect and repair the battery connections and contactors.")
            elif symptoms == '5':
                print("consult an expert or visit.........")
       
        elif problem_area == '2':
            if symptoms == '1':
                print("EXpert system solution.....\n: Bleed the brake system to remove any air bubbles and restore pedal feel.")
            elif symptoms == '2':
                print("EXpert system solution.....\n Check and replace worn brake pads, calipers, or brake discs")
            elif symptoms == '3':
                print("EXpert system solution.....\n  Inspect and maintain the regenerative braking system components to ensure optimal performance.")
            elif symptoms == '4':
                print("EXpert system solution.....\n  Calibrate the regenerative braking system to prevent abrupt deceleration.")
        elif problem_area == '3':
            if symptoms == '1':
                print("EXpert system solution.....\n   Diagnose and repair faulty ignition coils or spark plugs.")
            elif symptoms == '2':
                print("EXpert system solution.....\n  :  Inspect and maintain the engine components, including the air filter and fuel injectors.")
            elif symptoms == '3':
                print("EXpert system solution.....\n   Check and, if necessary, replace the transmission fluid and filters..")
            elif symptoms == '4':
                print("EXpert system solution.....\n   Inspect the cooling system for leaks and ensure the proper functioning of the cooling fans..")
            elif symptoms == '5':
                print("consult an expert or visit.........")
        elif problem_area == '4':
            if symptoms == '1':
                print("Expert system solution.....\n Check the electric motor and lubricate or replace components as required")
            elif symptoms == '2':
                print("Expert system solution.....\n  :   Inspect and repair the electric motor's connections and wiring")
            elif symptoms == '3':
                print("Expert system solution.....\n  Clean the inverter cooling system and ensure proper airflow.")
            elif symptoms == '4':
                print("Expert system solution.....\n   Reduce the load on the motor and ensure proper cooling by maintaining the cooling system.")
            elif symptoms == '5':
                print("consult an expert or visit.........")
        elif problem_area == '5':
            if symptoms == '1':
                print("Expert system solution.....\n  Perform a diagnostic scan to identify the issue and address it accordingly")
            elif symptoms == '2':
                print("Expert system solution.....\n  :Update the hybrid system software or replace faulty integration modules.")
            elif symptoms == '3':
                print("Expert system solution.....\n  Check and repair the hybrid system's sensors and switches.")
            elif symptoms == '4':
                print("Expert system solution.....\n   Calibrate the hybrid system and update the energy flow display software..")
            elif symptoms == '5':
                print("consult an expert or visit.........")