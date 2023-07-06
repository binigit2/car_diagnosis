# hydrogen_fuel_cell_car.py

from vehicle import Vehicle

class HydrogenFuelCellCar(Vehicle):
    def __init__(self):
        super().__init__("Hydrogen Fuel Cell Car")

    def diagnose(self):
        super().diagnose()
        problem_area = super().get_problem_area()
        symptoms = super().get_symptoms(problem_area)
        self.get_solution(problem_area,symptoms)

    def get_solution(self, problem_area,symptoms):
        if problem_area=="1":    
            if symptoms == '1':
                print(" Expert solution...\n Inspect and replace damaged or degraded fuel cell stack components.")
            elif symptoms == '2':
                print(" Expert solution...\nCheck and adjust the fuel cell stack's voltage regulation system")
            elif symptoms == '3':
                print(" Expert solution...\n Improve the cooling system and ensure proper cooling of the fuel cell stack.")
            elif symptoms == '4':
                print("  Expert solution...\nIdentify and resolve any issues with the shutdown circuitry of the fuel cell stack..")
            else:
                print("Invalid choice. Please try again.")
    
        elif problem_area == '2':
                if symptoms == '1':
                    print("EXpert system solution.....\n:: Inspect the hydrogen storage system for leaks and repair or replace any faulty components.")
                elif symptoms == '2':
                    print("EXpert system solution.....\n Analyze the hydrogen storage system for potential leaks or inefficient usage and address them accordingly.")
                elif symptoms == '3':
                    print("EXpert system solution.....\n   Detect and repair hydrogen leaks in the storage system to prevent any potential safety hazards")
                elif symptoms == '4':
                    print("EXpert system solution.....\n   Optimize the hydrogen storage system to maximize the range by improving storage capacity or efficiency.")
            
        elif problem_area == '3':
                if symptoms == '1':
                    print("EXpert system solution.....\n Check the cooling system for blockages, leaks, or malfunctioning components, and repair or replace them as needed.")
                elif symptoms == '2':
                    print("EXpert system solution.....\n Enhance the cooling system's capacity or efficiency to regulate the fuel cell temperature within optimal limits.")
                elif symptoms == '3':
                    print("EXpert system solution.....\n : Evaluate and calibrate the cooling system's sensors, pumps, and controls to ensure reliable and uniform cooling.")
                elif symptoms == '4':
                    print("EXpert system solution.....\n   Implement a thermal management strategy to maintain proper cooling during extreme operating conditions and prevent power loss.")
        elif problem_area == '3':
                if symptoms == '1':
                    print("EXpert system solution.....\n Check the cooling system for blockages, leaks, or malfunctioning components, and repair or replace them as needed.")
                elif symptoms == '2':
                    print("EXpert system solution.....\n Enhance the cooling system's capacity or efficiency to regulate the fuel cell temperature within optimal limits.")
                elif symptoms == '3':
                    print("EXpert system solution.....\n : Evaluate and calibrate the cooling system's sensors, pumps, and controls to ensure reliable and uniform cooling.")
                elif symptoms == '4':
                    print("EXpert system solution.....\n   Implement a thermal management strategy to maintain proper cooling during extreme operating conditions and prevent power loss.")
            
