# module

## How to load different Tensorflow Version?
We have two versions of Tensorflow available on our sever: a very old version 1.8.0 and the last version of TF1 1.15.0.

TF version 1.8.0 is combined with anaconda3/py3. Beside this, you also need following modules:
```bash
module load anaconda3 cuda90 cudnn openmpi/cuda 
```

TF version 1.15.0 is a seperate module based on anaconda3/py3, you have to load it explicitly:
```bash
module load tensorflow/1.15.0
```

TF2.x is not supported globally on server now.
## Small tips

unload all loaded modules
```shell
module purge
```