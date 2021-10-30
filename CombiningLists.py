import pandas as pd

June = pd.read_csv("2015JuneHCD.csv")
July = pd.read_csv("2015JulyHCD.csv")
August = pd.read_csv("2015AugustHCD.csv")
September = pd.read_csv("2015SeptemberHCD.csv")
October = pd.read_csv("2015OctoberHCD.csv")

pd.concat([June, July, August, September, October]
          ).to_csv("2015June-OctoberHCD.csv", index=False)
