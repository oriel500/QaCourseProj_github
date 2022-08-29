class Test:

    def __init__(self):
        pass

    def main(self, a=""):
        try:
            raise Exception(a)
        except Exception as e:
            print(e)
        finally:
            print("the program is done...")

    def print1(self, a):
        print(a)


test = Test()
# test.main()

exaption1 = BaseException()
str1 = "hello"
exaption1 = str1
test.print1(exaption1)
test.main(exaption1)



