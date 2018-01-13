'''
Created on 2018/01/13

@author: u16
'''
import os

from pa import PyPagen, get_secret


if __name__ == '__main__':

    # simple sample
    os.system('python3 pa.py ')

    # module function sample
    print(get_secret())
    print(get_secret(10))

    # class sample
    pg = PyPagen()
    print(pg.get_secret())
    print(pg.get_secret(lenmax=6))
    print(pg.get_secret(symbol=False, lenmin=3, lenmax=16))
    print(pg.get_secret(seq_sbl="!%$&'", num=False, lenmin=16, lenmax=24))

    pg.set_param(symbol=False, lenmax=4)
    print(pg.get_secret_list(10))

''' end of line
'''
