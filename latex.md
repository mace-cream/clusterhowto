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