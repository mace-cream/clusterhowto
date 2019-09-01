Sometimes you need to develop a web application or website to make your work accessible by others from browser client. You need to choose a
backend programming language. If you use php, you can use our server as the developing machine since php developing on windows is not the best choice.

Two versions of php are installed on the server. One is the default version 5.4 when you invoke `php` command. The other is version 7.2, also
the version used to serve our lab wiki. The command line client is located at `/opt/rh/rh-php72/root/usr/bin/php`, not added to path.

To develop, you can invoke `php -S localhost:8213` in the shell with current working directory as your document root. Then you can access the port to
debug your application.