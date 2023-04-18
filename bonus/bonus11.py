def get_tempratures():
    with open("files/temprature.txt", "r") as file_local:
        tempratures_local = file_local.readlines()

    values = tempratures_local[1:]
    values = [float(i) for i in values]
    average_local = sum(values) / len(values)
    return average_local


average = get_tempratures()
print(average)