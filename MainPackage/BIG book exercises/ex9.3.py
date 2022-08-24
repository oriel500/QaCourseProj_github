from datetime import datetime

born_date = input("Enter born date ([Name Month] [day] [year]):")
list_date = born_date.split()  # split m d and y to different strings
names_month = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8,
               'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}  # number to month

y = int(list_date[2])
m = names_month[list_date[0]]
d = int(list_date[1])
new_date = datetime(y, m, d)
print(new_date.strftime("%Y-%m-%d"))
