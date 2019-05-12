
## CMake

The version of `cmake` is **2.8**. To use higher version, you need cmake3.

Our cluster cannot identify loaded module like higher version of `g++`. To use
it in cmake, you need to specify the abosolute path like the following.
```bash
cmake3 -DCMAKE_CXX_COMPILER=/cm/local/apps/gcc/8.2.0/bin/g++ ..
```

## Dependencies

A typical C++ project dependends on some other libraries, which should be
installed system-wide. The installation needs sudo privileges. If you are
common users, you can contact [zhaofeng-shu33](https://github.com/zhaofeng-shu33).