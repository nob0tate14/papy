#  Copyright 2018 Nobuo Tateishi<nob0tate14@gmail.com>
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#       http://www.apache.org/licenses/LICENSE-2.0
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
'''
Created on 2018/01/13

@author: nob0tate14
'''

import argparse
import random
import secrets
import string


class PyPagen(object):
    '''
    ordinary password generator
    '''
    SEQ_FUL = string.ascii_lowercase + string.ascii_uppercase + \
        string.digits + string.punctuation
    SEQ_ALW = "abcdefghijklmnopqrstuvwxyz"
    SEQ_AUP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    SEQ_NUM = "0123456789"
    SEQ_SBL = "\"#$%&'()*+,-./:;<=>?@[]^_`{|}~"

    def __init__(self, *, seq_alw=SEQ_ALW, seq_aup=SEQ_AUP, seq_num=SEQ_NUM,
                 seq_sbl=SEQ_SBL, lenmin=8, lenmax=8,
                 up=True, low=True, num=True, symbol=True, strict=True):
        '''
        Constructor
        '''
        self.set_param(seq_alw=seq_alw, seq_aup=seq_aup, seq_num=seq_num,
                       seq_sbl=seq_sbl, lenmin=lenmin, lenmax=lenmax,
                       up=up, low=low, num=num, symbol=symbol, strict=strict)

    def set_param(self, *, seq_alw=SEQ_ALW, seq_aup=SEQ_AUP, seq_num=SEQ_NUM,
                  seq_sbl=SEQ_SBL, lenmin=8, lenmax=8,
                  up=True, low=True, num=True, symbol=True, strict=True):
        self.seq_alw = seq_alw
        self.seq_aup = seq_aup
        self.seq_num = seq_num
        self.seq_sbl = seq_sbl
        self.lenmin = lenmin
        self.lenmax = lenmax
        self.up = up
        self.low = low
        self.num = num
        self.symbol = symbol
        self.strict = strict

    def get_secret(self, *, seq_alw=None, seq_aup=None, seq_num=None,
                   seq_sbl=None, lenmin=None, lenmax=None,
                   up=None, low=None, num=None, symbol=None, strict=None):
        if seq_alw is None:
            seq_alw = self.seq_alw
        if seq_aup is None:
            seq_aup = self.seq_aup
        if seq_num is None:
            seq_num = self.seq_num
        if seq_sbl is None:
            seq_sbl = self.seq_sbl
        if lenmin is None:
            lenmin = self.lenmin
        if lenmax is None:
            lenmax = self.lenmax
        if up is None:
            up = self.up
        if low is None:
            low = self.low
        if num is None:
            num = self.num
        if symbol is None:
            symbol = self.symbol
        if strict is None:
            strict = self.strict
        secrt = ""
        loopcount = lenmin
        if lenmin >= lenmax:
            loopcount = lenmax
        if lenmin < lenmax:
            loopcount = random.randrange(lenmin, lenmax, 1)

        seq_list = []
        if low is True:
            seq_list.append(seq_alw)
            if strict is True:
                secrt += secrets.choice(seq_alw)
        if up is True:
            seq_list.append(seq_aup)
            if strict is True:
                secrt += secrets.choice(seq_aup)
        if num is True:
            seq_list.append(seq_num)
            if strict is True:
                secrt += secrets.choice(seq_num)
        if symbol is True:
            seq_list.append(seq_sbl)
            if strict is True:
                secrt += secrets.choice(seq_sbl)

        for dummy in range(len(secrt), loopcount):
            ii = secrets.randbelow(len(seq_list))
            # print(seq_list[ii - 1])
            secrt += secrets.choice(seq_list[ii - 1])
        secrt = "".join(random.sample(secrt, len(secrt)))
        return secrt

    def get_secret_list(self, count=1):
        ret_list = []
        for dummy in range(count):
            ret_list.append(self.get_secret())
        return ret_list


def get_secret(lenmax=8):
    pg = PyPagen(lenmin=lenmax, lenmax=lenmax)
    return(pg.get_secret())


def do_parse_args():
    parser = argparse.ArgumentParser(
        prog="pa.py",
        usage="python3 pa.py 8",
        description="ordinary password generator",
        add_help=True)

    parser.add_argument("length", nargs="?", action="store", type=int,
                        default=8, help="password length")

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = do_parse_args()
    pg = PyPagen(lenmax=args.length)
    print(pg.get_secret())


''' end of line
'''
