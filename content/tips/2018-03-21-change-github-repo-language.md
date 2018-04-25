Title: Change Your Github Repository's Language
Date: 2018-03-21

Github uses [Linguist library](https://github.com/github/linguist) to determine your repository's language. If you find that Github has done something wrong, you may fix by adding a `.gitattributes` file with the following content:

```
* linguist-vendored
*.py linguist-vendored=false
```

The above will let Github detect your repository's language as `Python`.