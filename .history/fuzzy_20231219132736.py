# Import necessary libraries
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define fuzzy system
occupancy_level = ctrl.Antecedent(np.arange(0, 101, 1), 'occupancy_level')
time_of_day = ctrl.Antecedent(np.arange(0, 24, 1), 'time_of_day')
parking_availability = ctrl.Consequent(np.arange(0, 101, 1), 'parking_availability')

# Define membership functions
occupancy_level['low'] = fuzz.trimf(occupancy_level.universe, [0, 0, 50])
occupancy_level['medium'] = fuzz.trimf(occupancy_level.universe, [0, 50, 100])
occupancy_level['high'] = fuzz.trimf(occupancy_level.universe, [50, 100, 100])

time_of_day['off_peak'] = fuzz.trimf(time_of_day.universe, [0, 7, 24])
time_of_day['peak'] = fuzz.trimf(time_of_day.universe, [7, 12, 19])

parking_availability['low'] = fuzz.trimf(parking_availability.universe, [0, 0, 50])
parking_availability['medium'] = fuzz.trimf(parking_availability.universe, [0, 50, 100])
parking_availability['high'] = fuzz.trimf(parking_availability.universe, [50, 100, 100])

# Define fuzzy rules
rule1 = ctrl.Rule(occupancy_level['low'] & time_of_day['off_peak'], parking_availability['high'])
rule2 = ctrl.Rule(occupancy_level['medium'] & time_of_day['off_peak'], parking_availability['medium'])
rule3 = ctrl.Rule(occupancy_level['high'] & time_of_day['off_peak'], parking_availability['low'])
# Add more rules as needed

# Create control system
parking_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
parking_sim = ctrl.ControlSystemSimulation(parking_ctrl)

# Set input values
input_occupancy = 75
input_time_of_day = 15
parking_sim.input['occupancy_level'] = input_occupancy
parking_sim.input['time_of_day'] = input_time_of_day

# Compute the result
parking_sim.compute()
result = parking_sim.output['parking_availability']

# Print the result
print("Parking Availability:", result)
