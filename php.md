Sometimes you need to develop a web application or website to make your work accessible by others from browser client. You need to choose a
backend programming language. If you use php, you can use our server as the developing machine since php developing on windows is not the best choice.

Two versions of php are installed on the server. One is the default version 5.4 when you invoke `php` command. The other is version 7.2, 
If you need 7.2 toolchain, run `module load php7` on manage node. Then `php --version` will show you it is 7.2. Also `phpunit` is available.
After your usage, you can run `module unload php7` to quit.

To develop, you can invoke `php -S localhost:8213` in the shell with current working directory as your document root. Then you can access the port to
debug your application.