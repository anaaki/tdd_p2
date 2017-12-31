
class TestCase:
    def __init__(self, name):
        print(name)
        self.name = name

    def setUp(self):
        pass
    def tearDown(self):
        pass
    def run(self):
        result = TestResult()
        result.testStargted()
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        return result

class WasRun(TestCase):
    def testMethod(self):
        self.log = self.log + "testMethod " 

    def setUp(self):
        self.log = "setUp "

    def tearDown(self):
        self.log = self.log + "tearDown "

    def testBrokenMethod(self):
        raise Exception

class TestResult:
    def __init__(self):
        self.runCount = 0
    
    def testStargted(self):
        self.runCount += 1

    def summary(self):
        return '{} run, 0 failed'.format(self.runCount)

class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun('testMethod')
        test.run()
        assert("setUp testMethod tearDown " == test.log)

    def testResult(self):
        test = WasRun('testMethod')
        result = test.run()
        assert("1 run, 0 failed" == result.summary())

    def testFailResult(self):
        test = WasRun('testBrokenMethod')
        result = test.run()
        assert("1 run, 1 failed" == result.summary())

TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()
# TestCaseTest("testFailResult").run()
