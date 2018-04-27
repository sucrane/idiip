Title: Cross Compile Python 3
Data: 2018-03-22

I need to run Python 3 on an ARM board, so I need to cross compile it. To cross compile Python, we need to compile Python and Parser in the host(build) machine.

```
$ cd $HOME
$ mkdir PythonSrc
$ cd PythonSrc
$ wget https://www.python.org/ftp/python/3.5.5/Python-3.5.5.tgz
$ tar zxf Python-3.5.5.tgz
$ mv Python-3.5.5 Python-3.5.5-host
$ cd Python-3.5.5-host
$ ./configure --prefix=$HOME/PythonSrc/PythonHost
$ make python Parser/pgen
$ make install
```

Then cross compile:

```
$ cd $HOME
$ tar zxf Python-3.5.5.tgz
$ cd Python-3.5.5
$ CC=arm-linux-gnueabihf-gcc
$ CXX=arm-linux-gnueabihf-g++
$ AR=arm-linux-gnueabihf-ar
$ RANLIB=arm-linux-gnueabihf-ranlib
$ ac_cv_file__dev_ptmx=no
$ ac_cv_file__dev_ptc=no
$ ac_cv_have_long_long_format=yes
$ ./configure --host=arm-linux-gnueabihf --target=arm-linux-gnueabihf --build=x86_64-linux-gnu --prefix=$HOME/PythonSrc/PythonTarget --disable-ipv6 --enable-shared
$
$ HOSTPYTHON=$HOME/PythonSrc/Python-3.5.5-host/python3
$ HOSTPGEN=$HOME/Python-3.5.5-host/Parser/pgen
$ BLDSHARED="arm-linux-gnueabihf-gcc -shared"
$ CROSS-COMPILE=arm-linux-gnueabihf-
$ CROSS_COMPILE_TARGET=yes
$ HOSTARCH=arm-linux
$ BUILDARCH=arm-linux-gnueabihf
$ make
$ make install
```

Now we get cross-compiled Python in `$HOME/PythonSrc/PythonTarget/`