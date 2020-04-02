# module

## How to add python package as new module
First, use `module load` command to load necessary environment(e.g. anaconda3/py3, cuda, etc.). Then use `pip` command to  install target package at /cm/shared/apps/ rather than default python directory. You need sudo to write in this dir. 

```shell
pip install tensorflow-gpu==1.15 -t /cm/shared/apps/some/directory
```

Then create a modulefile at /cm/shared/modulefile/ to let module system know it. In this file, two terms have to be announced. Add your necessary environment as dependency like:

```
if { [is-loaded cuda10.0/]==0 } {
  module load cuda10.0
}
```

and add the path of new package to PYTHONPATH to let python find it:

```               
prepend-path  PYTHONPATH  /cm/shared/apps/some/directory
```

## Small tips

unload all loaded modules
```shell
module purge
```