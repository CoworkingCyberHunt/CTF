#!/usr/bin/env python3

# SecretoCentrífugo.py

import math

def calculate_velocity(temperature, material_amount, processing_time):
    # Constants based on empirical data
    TEMP_FACTOR = 1.2
    MATERIAL_FACTOR = 0.5
    TIME_FACTOR = 0.7

    # Calculate the effect of each factor on velocity
    temp_effect = TEMP_FACTOR * temperature
    material_effect = MATERIAL_FACTOR * math.log(material_amount)
    time_effect = TIME_FACTOR * math.sqrt(processing_time)

    return temp_effect + material_effect + time_effect

def get_processing_range(min_time, max_time):
    # Ensure max_time is always greater than min_time
    if min_time > max_time:
        min_time, max_time = max_time, min_time

    # Calculate a processing range
    range_values = [calculate_velocity(temp, 100, t) for t in range(min_time, max_time + 1)]
    return range_values

def main():
    temperature = float(input("Enter the temperature (in Celsius): "))
    material_amount = float(input("Enter the material amount (in grams): "))
    min_processing_time = float(input("Enter the minimum processing time (in seconds): "))
    max_processing_time = float(input("Enter the maximum processing time (in seconds): "))

    velocities = get_processing_range(min_processing_time, max_processing_time)

    print("\nVelocities for each second in the processing range:")
    for i, v in enumerate(velocities, start=int(min_processing_time)):
        print(f"At second {i}: {v:.2f} RPM")

# Flag: 4b 49 50 7b 47 69 72 61 45 6c 43 6f 64 69 67 6f 59 45 6e 63 75 65 6e 74 72 61 45 6c 53 65 63 72 65 74 6f 7d
# Remember: Always protect sensitive information and don't leave code unattended!

if __name__ == "__main__":
    main()
