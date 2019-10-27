# Matlab
This software is disabled by default. If you want to use, contact the cluster admin.

## GUI
If you connect the server via X11 or vnc desktop, you can start matlab by `proxychains4 matlab`.
![](./images/server_matlab.png)

## Non-GUI
Under nornal SSH login, you can invoke matlab by `proxychains4 matlab -nodesktop`. Notice this software is experimental supported by lab2c web admin.
Matlab may not start as you want.
![](./images/matlab_terminal.png)

## Script Mode
```shell
proxychains4 matlab -nodesktop -nosplash -nodisplay -r "run('path/to/your/script.m');exit;"
```