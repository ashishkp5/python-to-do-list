feet_inches = input("Enter feet and inches: ")


def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = parts[0]
    inches = parts[1]

    return {"feet":feet, "inches":inches}


parsed = parse(feet_inches)


def convert(feet, inches):
    meters = float(feet) * 0.3048 + float(inches) * 0.0254
    return meters


result = convert(parsed["feet"], parsed["inches"])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meter")
