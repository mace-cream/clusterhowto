# Python
## 2.7
This version of python retired in 2020.1.1. Do not develop new codes in this version.
If you need to maintain old codes, consider transfer to Python 3.x.
If you need to run Python2.7 codes of others. Here are some tips:

* `--user` and `--editable` cannot be used simultaneously. 

## 3+
### Sympy
Symoblic Computing

## Use CPUs
For tensorflow, if you need to use cpus on compute node, try the following code
```
import os
os.environ['CUDA_VISIBLE_DEVICES'] = ''
```

# PHP
Sometimes you need to develop a web application or website to make your work accessible by others from browser client. You need to choose a
backend programming language. If you use php, you can use our server as the developing machine since php developing on windows is not the best choice.

Two versions of php are installed on the server. One is the default version 5.4 when you invoke `php` command. The other is version 7.2, 
If you need 7.2 toolchain, run `module load php7` on manage node. Then `php --version` will show you it is 7.2. Also `phpunit` is available.
After your usage, you can run `module unload php7` to quit.

To develop, you can invoke `php -S localhost:8213` in the shell with current working directory as your document root. Then you can access the port to
debug your application.

# C++
## Compiler

I recommend to use higher version of `g++`. You can type `module load gcc/8.2.0`.

## CMake

The version of `cmake` is **2.8**. To use higher version, you can use `module load cmake/3.12.3`.

Our cluster cannot identify loaded module like higher version of `g++`. To use
it in cmake, you need to specify the abosolute path like the following.
```bash
cmake -DCMAKE_CXX_COMPILER=/cm/local/apps/gcc/8.2.0/bin/g++ ..
```
## ABI Version

Some preinstalled libraries (for example `boost-1.53.0`) are built by gcc version <=4.8. Because of [ABI Compatability](https://gcc.gnu.org/onlinedocs/gcc-5.2.0/libstdc++/manual/manual/using_dual_abi.html) you need to add some extra preprocessor flags to `g++` to be able to link your `cpp`. For dual abi problem, add `-D_GLIBCXX_USE_CXX11_ABI=0`.

## Dependencies

A typical C++ project dependends on some other libraries, which is recommended to be
installed system-wide. The installation needs sudo privileges. If you are
common users, you can contact the server admin to install them. For some cases, you can download the prebuilt `rpm` or `deb` package and install them to 
a custom directory. Then in you project you should specify this custom directory to your compiler.

Once installed, many packages can be checked via `pkg-config`.
For example, to see which compile flags are needed to use glib library, you can use:
```shell
pkg-config --cflags glib-2.0
```
To see which link flags are needed to use glib library, use:
```shell
pkg-config --libs glib-2.0
```
## Python Binding

To develop Python binding for your C++ project, Cython is needed. For complex binding, you need to customize your `setup.py` to build the extension.

## Debug
Command line debugger `gdb` can be used on the manager node. On Storage node, you can launch vscode and use the GUI debugging tool, which uses `gdb` internally but provide many convenient functionalities. 

# TeX
On our manage node, full scheme of texlive 2019 is installed.

To use latex on our server. You need to add `/usr/local/texlive/2019/bin/x86_64-linux` to your path.

Then
```shell
mkdir -p build && xelatex -output-directory=build your_file.tex
```

After successful complication, you can view your pdf with:
```shell
xdg-open build/your_file.pdf
```