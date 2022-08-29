from MainPackage.OBJECTS.Hard_Disk import Hard_disk
from MainPackage.OBJECTS.Person import Person
from MainPackage.OBJECTS.Student import Student


# === main program ===
try:  # check if you have error
    a = 5.5
    print(a/"2")
    print(a / 1)
except:
    print("run if have error")
else:
    print("run if  have no errors")
finally:
    print("always happen")