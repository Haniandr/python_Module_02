class GardenError(Exception):
    def __init__(self, message="Unknown plant error"):
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name.capitalize()}: [OK]")


def test_watering_system(plants):
    i = 0
    print("Opening watering system")

    try:
        for plants in plants:
            water_plant(plants)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n"
              ".. ending tests and returning to main")
        i = 1
    finally:
        print("Closing watering system\n")

    if i == 1:
        print("Cleanup always happens, even with errors!")
    return


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    plants = ["Tomate", "Lettuce", "Carots"]
    test_watering_system(plants)

    print("\nTesting invalid plants")
    plants_two = ["Tomato", "lettuce"]
    test_watering_system(plants_two)
