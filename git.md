# Git

This document instructs you how to install a newer version of git on your local computer.

## Make a temporary working directory (optional)

```sh
$ tmp_dir=$(mktemp -d -t git-XXXXXXXX)
$ cd "$tmp_dir"
```

## Download git

Download the source code tarball of your preferred version (e.g. `2.26.2`)
from [https://mirrors.edge.kernel.org/pub/software/scm/git/](https://mirrors.edge.kernel.org/pub/software/scm/git/)

```sh
$ wget https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.26.2.tar.gz
```

## Build and install

I prefer to install local applications to `~/.local`.
If you do not want to install git to this path,
you can change the `prefix` in the following commands.

```sh
$ tar -xzvf git-2.26.2.tar.gz
$ cd git-2.26.2
$ make configure
$ ./configure --prefix="$HOME/.local"
$ make -j8
$ make install
```

## Test installation

Make sure you have added `~/.local/bin/` to your `PATH` environment variable.

```sh
$ echo 'export PATH=$HOME/.local/bin:$PATH' >> ~/.bashrc
$ . ~/.bashrc
```

Try the following command to test if you install git successfully.

```sh
$ git --version
git version 2.26.2
```

## Clean (optional)

```sh
$ echo "$tmp_dir"  ## Make sure the tmp_dir defined before haven't been modified
$ cd && rm -rf "$tmp_dir"
```
