
## CMake

The version of `cmake` is **2.8**. To use higher version, you need cmake3.

Our cluster cannot identify loaded module like higher version of `g++`. To use
it in cmake, you need to specify the abosolute path like the following.
```bash
cmake3 -DCMAKE_CXX_COMPILER=/cm/local/apps/gcc/8.2.0/bin/g++ ..
```
## ABI Version

Some preinstalled libraries (for example `boost-1.53.0`) are built by gcc version <=4.8. Because of [ABI Compatability](https://gcc.gnu.org/onlinedocs/gcc-5.2.0/libstdc++/manual/manual/using_dual_abi.html) you need to add some extra preprocessor flags to `g++` to be able to link your `cpp`. For dual abi problem, add `-D_GLIBCXX_USE_CXX11_ABI=0`.

## Dependencies

A typical C++ project dependends on some other libraries, which should be
installed system-wide. The installation needs sudo privileges. If you are
common users, you can contact [zhaofeng-shu33](https://github.com/zhaofeng-shu33).