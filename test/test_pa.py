'''
Created on 2018/01/28

@author: nob0tate14
'''
import unittest
from pa import PyPagen


class TestPyPagen(unittest.TestCase):

    def test_pwchar_alw(self):
        print("test_pwchar_alw")
        pg = PyPagen()
        pw = pg.get_secret(up=False, num=False, symbol=False)
        print(pw)
        self.assertTrue(pw.islower())
        for s in pw:
            if s not in pg.seq_alw:
                self.assertTrue(False, "no seq char in pw string")

    def test_pwchar_aup(self):
        print("test_pwchar_aup")
        pg = PyPagen()
        pw = pg.get_secret(low=False, num=False, symbol=False)
        print(pw)
        self.assertTrue(pw.isupper())
        for s in pw:
            if s not in pg.seq_aup:
                self.assertTrue(False, "no seq char in pw string")

    def test_pwchar_num(self):
        print("test_pwchar_num")
        pg = PyPagen()
        pw = pg.get_secret(low=False, up=False, symbol=False)
        print(pw)
        self.assertTrue(pw.isnumeric())
        for s in pw:
            if s not in pg.seq_num:
                self.assertTrue(False, "no seq char in pw string")

    def test_pwchar_sbl(self):
        print("test_pwchar_sbl")
        pg = PyPagen()
        pw = pg.get_secret(low=False, up=False, num=False)
        print(pw)
        for s in pw:
            if s not in pg.seq_sbl:
                self.assertTrue(False, "no seq char in pw string")

    def test_pwlength_min(self):
        print("test_pwlength_min")
        pg = PyPagen()
        pg.set_param(lenmin=3)
        pw = pg.get_secret()
        print(pw)
        self.assertGreaterEqual(len(pw), 3)
        pw = pg.get_secret(lenmax=3, strict=False)
        print(pw)
        self.assertEqual(len(pw), 3)
        pw = pg.get_secret(lenmin=6, lenmax=6)
        print(pw)
        self.assertEqual(len(pw), 6)

    def test_pwlength_max(self):
        print("test_pwlength_max")
        pg = PyPagen()
        pg.set_param(lenmax=30)
        pw = pg.get_secret()
        print(pw)
        self.assertLessEqual(len(pw), 30)
        pw = pg.get_secret(lenmax=1, strict=False)
        print(pw)
        self.assertEqual(len(pw), 1)
        # lenmax prior to lenmin...
        pw = pg.get_secret(lenmin=5, lenmax=3, strict=False)
        print(pw)
        self.assertEqual(len(pw), 3)

    def test_pwchar_strict(self):
        print("test_pwchar_strict")
        pg = PyPagen()
        pw = pg.get_secret(lenmin=3, lenmax=3, strict=True)
        print(pw)
        self.assertEqual(len(pw), 4)
        pw = pg.get_secret(lenmin=3, lenmax=3, strict=False)
        print(pw)
        self.assertEqual(len(pw), 3)
        pw = pg.get_secret(low=False, lenmin=3, lenmax=3, strict=True)
        print(pw)
        self.assertEqual(len(pw), 3)

    def test_pwchar_mix(self):
        print("test_pwchar_mix")
        pg = PyPagen()
        pw = pg.get_secret(num=False, symbol=False)
        print(pw)
        expect = pg.seq_alw + pg.seq_aup
        b1 = False
        b2 = False
        for s in pw:
            if s not in expect:
                self.assertTrue(False, "no seq char in pw string")
            if s in pg.seq_alw:
                b1 = True
            if s in pg.seq_aup:
                b2 = True
        self.assertTrue(b1, "no seq char in pw string")
        self.assertTrue(b2, "no seq char in pw string")

    def test_pwchar_mix2(self):
        print("test_pwchar_mix2")
        pg = PyPagen()
        pw = pg.get_secret(low=False, up=False)
        print(pw)
        expect = pg.seq_num + pg.seq_sbl
        b1 = False
        b2 = False
        for s in pw:
            if s not in expect:
                self.assertTrue(False, "no seq char in pw string")
            if s in pg.seq_num:
                b1 = True
            if s in pg.seq_sbl:
                b2 = True
        self.assertTrue(b1, "no seq char in pw string")
        self.assertTrue(b2, "no seq char in pw string")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testPyPagen']
    unittest.main()
