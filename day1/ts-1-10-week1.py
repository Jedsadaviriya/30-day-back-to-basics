# min to hour and min calculator
minutes = int(input("How many minutes do you want to convert to hours?: "))
mth = minutes / 60
# mthwhole = min // 60 # directly does the rounding, so if this were in use, the int in int(mth) wouldn't have been needed 
mtm = minutes % 60
print(f"{minutes} Minutes converts to {int(mth)} hour/s and {mtm} Minutes")
