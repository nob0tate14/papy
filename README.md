# papy  
ordinary password generator


## Overview
 generate password string and any password candicate

## Description
**pa.py**  
password generator  

you can choice password character  
Upper and lower alphabet,numeric and symbols  

when ristriction for symbol character  
then use any symbol character.  
(see sample_papy.py)  

*class*  
* PyPagen  
generator class  

*method(instance method of PyPagen)*  
* get_secret  
one password string.  

* get\_secret_list  
any password candicate list.  

* set_param  
<dl>
<dt>seq\_sbl</dt><dd>symbol string sequence default:SEQ_SBL</dd>
<dt>lenmin</dt><dd>password minimum length default:8</dd>
<dt>lenmax</dt><dd>password max length default:8</dd>
<dt>up</dt><dd>use upper alphabet default:True</dd>
<dt>low</dt><dd>use lower alphabet default:True</dd>
<dt>num</dt><dd>use number default:True</dd>
<dt>symbol</dt><dd>use symbol default:True</dd>
<dt>strict</dt><dd>it sure to using char type(if true). this is prior to minimum length.</dd>
</dl>

*module function*  
* get_secret  
for easy used.  

---  
**sample_papy.py**  
usage sample  

## Requirement

## Usage
```
>>python3 pa.py 
9[jMm,4u

>>python3 sample_papy.py 
00Yd-Yvg
:wR_R1AT
%Vn6O$0s3a
]yvUI$7L
:9qoP)
2OzkrTYo35lo235
u!ClIwt&WOwM!dVylnU
['N63y', '86Ij', '5WHx', 'jVE4', 'Qf79', 'wPM2', 'eSK1', 'ySJ7', '3OWj', 'wVw6']

```

## Install

## Contribution

## Licence

there is licensed under the Apache License, Version2.0
(see ./LICENSE.txt)

## Author

Nobuo Tateishi(https://github.com/nob0tate14)