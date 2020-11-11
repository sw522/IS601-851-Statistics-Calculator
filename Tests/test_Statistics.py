import unittest
import random
from Statistics.Statistics import Statistics
import pprint
import numpy as np
import scipy.stats
from CsvReader.CsvReader import CsvReader

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        random.seed(5)
        #self.testData = [0,1,2,3,4,5,6,6] #randint(0, 10, 20)

        self.statistics = Statistics()
        self.testData = []
        self.zscoredata = []

        dataset_reader = CsvReader('Tests/Dataset.csv').data
        for row in dataset_reader:
            self.testData.append(int(row['DataSet']))

        stat_answers = CsvReader('Tests/UnitTestStatAnswers.csv').data
        for row in stat_answers:
            self.mean = float(row['mean'])
            self.median = float(row['median'])
            self.mode = float(row['mode'])
            self.variance = float(row['variance'])
            self.stddev = float(row['stddev'])

        zscore_reader = CsvReader('Tests/UnitTestZScoreAnswers.csv').data
        for row in zscore_reader:
            self.zscoredata.append(float(row['zscore']))

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean(self.testData)

        self.assertEqual(mean, self.mean)

    def test_median_calculator(self):
        median = self.statistics.median(self.testData)
        self.assertEqual(median, self.median)

    def test_mode_calculator(self):
        mode = self.statistics.mode(self.testData)
        self.assertEqual(mode, self.mode)

    def test_stddev_calculator(self):
        stddev = self.statistics.stddev(self.testData)
        self.assertEqual(stddev, self.stddev)

    def test_variance_calculator(self):
        variance = self.statistics.variance(self.testData)
        self.assertEqual(variance, self.variance)

    def test_zscore_calculator(self):
        ZScore = self.statistics.zscore(self.testData)

        for i in range(0,len(ZScore)-1):
            self.assertEqual(round(ZScore[i],4), round(self.zscoredata[i],4))


if __name__ == '__main__':
    unittest.main()