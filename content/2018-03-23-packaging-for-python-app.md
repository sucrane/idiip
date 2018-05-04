Title: Packaging for Python App
Date: 2018-03-23

It is not quite convenient for our customer to setup Python environment on Windows or other platforms to run our Python app. So we need to pack our Python app into stand-alone .exe file. Fortunately, there are quite a few tools to help us. And among these, PyInstaller is my favorite.

[PyInstaller](http://www.pyinstaller.org/) is a program that freezes (packages) Python programs into stand-alone executables, under Windows, Linux, Mac OS X, FreeBSD, Solaris and AIX. Its main advantages over similar tools are that PyInstaller works with Python 2.7 and 3.3—3.6, it builds smaller executables thanks to transparent compression, it is fully multi-platform, and use the OS support to load the dynamic libraries, thus ensuring full compatibility.

We can install PyInstaller using `pip`:

```
pip install pyinstaller
```

Then go to your project's directory, and run:

```
pyinstaller your-app.py
```

It will generate the bundle in a subdirectory called `dist`.
