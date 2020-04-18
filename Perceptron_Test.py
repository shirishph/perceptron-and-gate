import unittest
import Perceptron


class Perceptron_Test(unittest.TestCase):

    def setUp(self):
        self.perceptron = Perceptron.Perceptron()

    def test_run(self):
        response = self.perceptron.train()
        self.assertTrue(response)

        for test in [[1, 1], [-1, 1], [1, -1], [-1, -1]]:
            result = self.perceptron.predict(test[0], test[1])
            print("evaluate ", str(test[0]).rjust(3, " "), str(test[1]).rjust(3, " "), ", result: ", result)


if __name__ == '__main__':
    unittest.main()
