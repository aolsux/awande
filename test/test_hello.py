import unittest


class HelloWorldTest(unittest.TestCase):
    def test_hello(self):
        self.assertTrue(True, "This test passes")

    @unittest.expectedFailure
    def test_fail(self):
        self.assertTrue(False, msg="This test always fails")
