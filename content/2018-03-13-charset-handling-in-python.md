Title: Charset Handling in Python
Date: 2018-03-13

As we know, Python 3 treats all string using UTF-8, and it is great. Sometimes, we need to unzip some zip files which come from Windows machine.

```python
# Unzip the zipfile to a folder.
zf = zipfile.ZipFile(zipped_file_full_path)

for name in zf.namelist():
    # FIXME: Need to handle path string encoding.
    new_name = name.encode("cp437").decode("utf8")
    if new_name.endswith('/'):
        os.makedirs(os.path.join('.', new_name), exist_ok=True)
    else:
        ext_filename = os.path.join('.', new_name)
        os.makedirs(os.path.dirname(ext_filename), exist_ok=True)
        outfile = open(ext_filename, 'wb')
        outfile.write(zf.read(name))
        outfile.close()
zf.close()
```