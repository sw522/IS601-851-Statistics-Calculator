import unittest
import random
from Statistics.Statistics import Statistics
import pprint
import numpy as np
import scipy.stats

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        random.seed(5)
        self.testData = [0,1,2,3,4,5,6,6] #randint(0, 10, 20)

        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        np_mean = round(np.mean(self.testData), 9)
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, np_mean)

    def test_median_calculator(self):
        np_median = round(np.median(self.testData), 9)
        median = self.statistics.median(self.testData)
        self.assertEqual(median, 3.5)

    def test_mode_calculator(self):
        np_mode = scipy.stats.mode(self.testData)
        np_mode_value = np_mode[0][0]
        mode = self.statistics.mode(self.testData)
        self.assertEqual(mode, np_mode_value)

    def test_stddev_calculator(self):
        np_stddev = round(np.std(np.array(self.testData)), 5)
        stddev = self.statistics.stddev(self.testData)
        self.assertEqual(stddev, np_stddev)

    def test_variance_calculator(self):
        np_variance = round(np.var(np.array(self.testData)), 9)
        variance = self.statistics.variance(self.testData)
        self.assertEqual(variance, np_variance)

    def test_zscore_calculator(self):
        np_zscore = scipy.stats.zscore(self.testData)
        ZScore = self.statistics.zscore(self.testData)

        for i in range(0,len(np_zscore)-1):
            self.assertEqual(round(ZScore[i],4), round(np_zscore[i],4))


if __name__ == '__main__':
    unittest.main()