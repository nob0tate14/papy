'''
Created on 2018/01/13

@author: nob0tate14
'''
import os

from pa import PyPagen, get_secret


if __name__ == '__main__':
    print("  simple sample")
    # simple sample
    os.system('python3 pa.py ')
    print("  module function sample")
    # module function sample
    print(get_secret(10))
    print("  class and method parameters sample")
    # class sample
    pg = PyPagen()
    print("  default")
    print(pg.get_secret())
    print("  use number and alphabet upper length=10")
    print(pg.get_secret(low=False, symbol=False, lenmin=10, lenmax=10))
    print("  use symbol only")
    print(pg.get_secret(up=False, low=False, num=False))
    print("  use alphabet abc only length=20")
    print(pg.get_secret(seq_alw="abc", up=False,
                        num=False, symbol=False, lenmin=20, lenmax=20))

    print("  candicate list")
    pg.set_param(symbol=False, lenmax=4)
    print(pg.get_secret_list(10))

''' end of line
'''
