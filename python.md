## Python2.7
`--user` and `--editable` cannot be used simultaneously. 

## Use CPUs
For tensorflow, if you need to use cpus on compute node, try the following code
```
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
```