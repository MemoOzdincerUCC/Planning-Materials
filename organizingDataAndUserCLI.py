import library
import pandas as pd

fileSelectionIndex = {
    "2015JuneHCD": 1,
    "2015JulyHCD.csv": 2,
    "2015AugustHCD.csv": 3,
    "2015SeptemberHCD.csv": 4,
    "2015OctoberHCD.csv": 5,
}

intialDialogue = "Which file would you like to use?: \nJune, 2015 (1)\nJuly, 2015 (2)\nAugust, 2015 (3)\nSeptember, 2015 (4) \nOctober, 2015 (5)\nEnter a number: "
fileName = int(input(intialDialogue))


if fileName == 1:
    fileName = "2015JuneHCD.csv"
elif fileName == 2:
    fileName = "2015JulyHCD.csv"
elif fileName == 3:
    fileName = "2015AugustHCD.csv"
elif fileName == 4:
    fileName = "2015SeptemberHCD.csv"
elif fileName == 5:
    fileName = "2015OctoberHCD.csv"
else:
    print("Invalid input. Exiting program.")

    filename = input(intialDialogue)
raw = library.loadList(fileName)

mainInput = input("Type 1 to see Dictionaries Demonstration, 2 for Pandas: ")

if mainInput == "1":
    # Option 1: I can index the data using a dictionary.
    index = {
        "Longitude (x)": 0,
        "Latitude (y)": 1,
        "Station Name": 2,
        "Climate ID": 3,
        "Date/Time (LST)": 4,
        "Year": 5,
        "Month": 6,
        "Day": 7,
        "Time": 8,
        "Temp": 9,
        "Dew Point": 11,
        "Rel Hum (%)": 13,
        "Precip. Amount (mm)": 14,
        "Wind Dir (10s deg)": 15,
        "Wind Speed (km/h)": 17,
        "Stn Press": 21,
    }

    inputIndex = input("Enter the index of the data you want to use: ")
    while inputIndex not in index:
        print("That is not a valid index.\n", "The indexes available are:")
        inputIndex = input("Enter the index of the data you want to use: ")
    print(raw[index[inputIndex]])

elif mainInput == "2":
    # Option 2: I can use Pandas to index the data.
    # Option 2 is preferred because many ML libraries such as TensorFlow and SKL accept pandas dataframes

    df = pd.DataFrame(raw)
    print(df.head())
