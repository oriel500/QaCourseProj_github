try:
    list1 = [1, 2]
    list1[2] = 3
    # list1[0] / ""
except IndexError as e:
    print(e, " #ERROR INDEX#")
except Exception:
    print("#ERROR OTHER#")
finally:
    print("Done...")