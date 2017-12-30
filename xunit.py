
class TestCase:
    def __init__(self, name):
        print(name)
        self.name = name

    def setUp(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def testMethod(self):
        self.log = self.log + "testMethod " 

    def setUp(self):
        self.log = "setUp "


class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun('testMethod')
        test.run()
        assert("setUp testMethod " == test.log)

TestCaseTest("testTemplateMethod").run()
