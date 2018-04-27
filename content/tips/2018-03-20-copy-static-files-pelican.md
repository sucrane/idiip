Title: Copy Static Files in Pelican
Date: 2018-03-20

GitHub Pages provide custom URL feature, which will create a `CNAME` file in the HTML root.

Using Pelican `STATIC_PATHS`, we can include this `CNAME` file. Copy the following to your Pelican configuration. (Supposing your `CNAME` file is in your `content/extra` directory.)

```
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}
```
