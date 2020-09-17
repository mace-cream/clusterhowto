=== Startup
Before 2018 May, our lab did not have any server. By the effects of Yang Li, postdoc of our lab at that time,
we had one server machine during May. The initial three administrators also include Mingyang Li and Yue Zhang.
The server is called "ace-cream" since Professor Shao-lun Huang, senior phd student xiangxiangxu and other
promonient students shared research interests on this technique.
Mingyang Li wrote the user documentation [ace_cream](./ace_cream.jemdoc). This documentation can also be
accessible at the personal website of Yang: [web ace_cream](http://yangli-feasibility.com/wiki/doku.php?id=ace-cream).

Student Feng Zhao also wrapped a python package called `ace_cream`, published on [pypi](https://pypi.org/project/ace-cream/).

=== Upgrade
Our old single server only had 4 GPUs and it was not enough when several students are in need. Competition for the occpucation
of GPUs happened now and then inevitable.

After around a year of running, our lab had bought a server cluster. The cluster solution is provided by Amax China, who were
promoting their docker-based GPU cluster solution. Postdoc Yang was cautious enough and was skeptical about their new system.
After detailed discussion with the engineers, Yang finally decided to use the solution of Bright Computing. The installation
was conducted by engineers of Amax China.

The server cluster became fully available from 2019 May. The new cluster uses `slurm` to schedule the computing tasks of users.

