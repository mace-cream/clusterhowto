Environment configuration for Python programming language
---------------------------------------------------------

For example, we will install python2.7.11 and keras0.3.3.

First, we need to configure the mirror for conda and pip.

Then, we should create the environment name and install python2.7.11.

***conda create --name keras0.3.3 python=2.7.11***

Then you can use

``` shell
conda info --envs
```

to check your environment.

We need to activate the created environment. Here, according to the
prompt, you need to reconnect the server before activating the
environment.

***ssh -Y \[username\]@10.8.4.170***

***conda activate keras0.3.3***

Then, we pip install the specified version of the package. We can use
***pip install \[package==version\]*** or ***pip install -i \[mirror
path\] \[package==version\]*** can be used to specify the mirror used in
this installation. And I used the following instruction:

***pip install -i <https://mirrors.aliyun.com/pypi/simple>
keras==0.3.3***

If you are downloading some packages because of version problems, please
install a specific version of the packages according to the error.

For example, I need to reinstall the lower version of the scipy package.

***pip install -i <https://mirrors.aliyun.com/pypi/simple> scipy==1.2***

Then, we continue to pip install the keras package.

***pip install -i <https://mirrors.aliyun.com/pypi/simple>
keras==0.3.3***

After installation, you can use python to check the versions of each
package.

Then you can run your program. Refer specifically to the BCM Cluster Use
Tutorial: <http://10.8.4.170:88/yang/clusterhowto> .
