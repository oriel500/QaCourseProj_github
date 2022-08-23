import datetime

local_date = datetime.datetime.now() # Localtime Date
num_day = int(input("Enter number 1-7: ")) # Choose number day
num_day_local = int(datetime.datetime.now().strftime("%w")) # save the number day local
delta_days = num_day - num_day_local
new_date = local_date + datetime.timedelta(days=delta_days-1)

print(new_date)