import pandas as pd
calories={"day1":420,"day2":500,"day3":510}
myvar=pd.Series(calories)
print(myvar)
myvar1=pd.Series(calories,index=["day1","day2"])
print(myvar1)