# papy  
ordinary password generator


## Overview
 generate password string and any password candicate

## Description
**pa.py**  
password generator  

you can choice password character  
Upper and lower alphabet,numeric and symbols  

when ristriction for character  
then use any characters.  
(see sample_papy.py)  

*class*  
* PyPagen  
generator class  

*method(instance method of PyPagen)*  
* get_secret  
get one password string.  

* get\_secret_list  
get any password candicate list.  

* set\_param  
set parameter  

*module function*  
* get\_secret  
for easy used.  

**sample_papy.py**  
usage sample  

---  

```
parameters for set_param
(same to constractor)
seq_alw
  upper alphabet string sequence. 
  default:SEQ_ALW
seq_aup
  lower alphabet string sequence. 
  default:SEQ_AUP
seq_num
  number string sequence. 
  default:SEQ_NUM
seq_sbl
  symbol string sequence. 
  default:SEQ_SBL
lenmin
  password minimum length. 
  default:8
lenmax
  password max length. 
  default:8
up
  use upper alphabet. 
  default:True
low
  use lower alphabet. 
  default:True
num
  use number. 
  default:True
symbol
  use symbol.
  default:True
strict
  it sure to using char type(if true).  
  this is prior to minimum length.  
  default:True

```

## Requirement

## Usage
```
>>python3 pa.py 
9[jMm,4u

>>python3 sample_papy.py 
H0zdq:sM
U6R2l_)2
}@0NPcw,7u
Eo4F;Q27
ps~2E@
ak7
%RTRuMAmAzB'$pY!%CnE'
['I29k', 'Vu0g', 'c8XQ', 'x0IO', 'XyZ2', 'V96y', 'bqL2', 'oX9v', 'PmT1', '7hNL']

```

## Install

## Contribution

## Licence

there is licensed under the Apache License, Version2.0
(see ./LICENSE.txt)

## Author

Nobuo Tateishi(https://github.com/nob0tate14)