class GardenError(Exception):
    def __init__(self, message="Unknown plant error"):
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


def check_plant(status) -> None:
    if status < 2:
        step = status
    else:
        step = status - 2

    if step == 0:
        raise PlantError("The Tomato is wilting!")
    elif step == 1:
        raise WaterError("Not enough water in the tank")


def test_garden(status=0) -> None:
    if status > 3:
        print("\nAll custom error types work correctly")
        return

    if status == 0:
        print("Testing PlantError...")
    if status == 1:
        print("Testing WaterError...")
    if status == 2:
        print("Testing catching all garden errors...")

    try:
        check_plant(status)
    except PlantError as e:
        if status < 2:
            print(f"Caught PlantError: {e}\n")
        else:
            print(f"Caught GardenError: {e}")

    except WaterError as e:
        if status < 2:
            print(f"Caught WaterError: {e}\n")
        else:
            print(f"Caught GardenError: {e}")

    except GardenError as e:
        print(f"Caught GardenError: {e}")

    test_garden(status + 1)


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    test_garden()
