import unittest
from Sampling.Sampling import Sampling
import pprint
import scipy.stats
import numpy as np

class MyTestCase2(unittest.TestCase):
    def setUp(self) -> None:
        #random.seed(5)
        self.testData = [0,1,2,3,4,5,6,6]
        self.n = 3
        self.sampling = Sampling()
        self.seed = 0
        self.conf = .95
        self.prop = .5
        self.width = .06

    def test_instantiate_sampling(self):
        self.assertIsInstance(self.sampling, Sampling)

    def test_srs_sampling(self):
        srs = self.sampling.srsseed(self.testData, self.n, self.seed)
        #pprint.pprint(srs)
        self.assertEqual(srs, [6, 3, 5])

    def test_moe_sampling(self):
        moe = self.sampling.moe(self.testData, self.conf)
        self.assertEqual(round(moe,3), round(scipy.stats.stats.sem(self.testData) * 1.96,3))

    def test_ci_sampling(self):
        ci = self.sampling.conf_int(self.testData, self.conf)
        np_mean = np.mean(self.testData)
        scipy_sem = scipy.stats.stats.sem(self.testData)
        np_ci = (round(np_mean,3),round(np_mean-(1.96 * scipy_sem),3),round(np_mean+(1.96 * scipy_sem),3))
        self.assertEqual(ci, np_ci)

    def test_cochrans_sampling(self):
        cochrans_n = self.sampling.cochrans_n(self.testData, self.conf, self.prop)
        self.assertEqual(cochrans_n, 1)

    def test_find_n_sampling(self):
        sample_n = self.sampling.find_n(self.conf,self.width)
        self.assertEqual(1, 1)