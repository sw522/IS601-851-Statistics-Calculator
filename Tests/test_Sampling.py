import unittest
from Sampling.Sampling import Sampling
import pprint
import scipy.stats
import numpy as np
import random
from CsvReader.CsvReader import CsvReader

class MyTestCase2(unittest.TestCase):
    def setUp(self) -> None:
        #random.seed(5)
        self.testData = []
        dataset_reader = CsvReader('Tests/Dataset.csv').data
        for row in dataset_reader:
            self.testData.append(int(row['DataSet']))

        self.srs = []

        srs_reader = CsvReader('Tests/UnitTestSrsAnswers.csv').data
        for row in srs_reader:
            self.srs.append(int(row['srs']))

        stat_answers = CsvReader('Tests/UnitTestSamplingInputs.csv').data
        for row in stat_answers:
            self.n = int(row['n'])
            self.seed = int(row['seed'])
            self.conf = float(row['conf'])
            self.prop = float(row['prop'])
            self.width = float(row['width'])

        stat_answers = CsvReader('Tests/UnitTestSamplingAnswers.csv').data
        for row in stat_answers:
            self.mean = float(row['mean'])
            self.moe = float(row['moe'])
            self.cochrans_n = float(row['cochrans'])
            self.sample_n = float(row['find_n'])

        self.sampling = Sampling()

    def test_instantiate_sampling(self):
        self.assertIsInstance(self.sampling, Sampling)

    def test_srs_sampling(self):
        srs = self.sampling.srsseed(self.testData, self.n, self.seed)
        self.assertEqual(srs, self.srs)

    def test_moe_sampling(self):
        moe = self.sampling.moe(self.testData, self.conf)
        self.assertEqual(round(moe,3), self.moe)

    def test_ci_sampling(self):
        ci = self.sampling.conf_int(self.testData, self.conf)
        self.assertEqual(ci, (self.mean, self.mean - self.moe, round(self.mean + self.moe,2) ))

    def test_cochrans_sampling(self):
        cochrans_n = self.sampling.cochrans_n(self.conf, self.prop)
        self.assertEqual(cochrans_n, self.cochrans_n)

    def test_find_n_sampling(self):
        sample_n = self.sampling.find_n(self.conf,self.width)
        self.assertEqual(sample_n, self.sample_n)