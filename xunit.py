class WasRun:
    def __init__(self, name):
        self.wasRun = None

    def run(self):
        self.testMethod()

    def testMethod(self):
        self.wasRun = 1    



if __name__ == '__main__':
    test = WasRun("testMethod")
    print(test.wasRun)
    test.run()
    print(test.wasRun)
