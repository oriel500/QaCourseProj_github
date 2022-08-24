from datetime import datetime
local_date = datetime.now()

print(local_date.strftime("%d/%m/%y"))
print(local_date.strftime("%m/%d/%y"))