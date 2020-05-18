## Python2.7
This version of python retired in 2020.1.1. Do not develop new codes in this version.
If you need to maintain old codes, consider transfer to Python 3.x.
If you need to run Python2.7 codes of others. Here are some tips:

* `--user` and `--editable` cannot be used simultaneously. 

## Use CPUs
For tensorflow, if you need to use cpus on compute node, try the following code
```
import os
os.environ['CUDA_VISIBLE_DEVICES'] = ''
```