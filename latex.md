To use latex on our server. You have two options.

1. On Storage node, full version of texlive 2019 is installed, you can invoke LaTeX command from shell directory to compile the source.

1. On Manage node, a docker container for LaTex is installed. It is called [latexdockercmd](https://github.com/blang/latex-docker). See [docker.md](./docker.md) for prerequisite. Then all you need to do is to prepend your command with `latexdockercmd`. For example:
```shell
mkdir -p build && latexdockercmd xelatex -output-directory=build your_file.tex
```

After successful complication, you can view your pdf with:
```shell
xdg-open build/your_file.pdf
```