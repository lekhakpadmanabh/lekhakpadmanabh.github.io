#A static site generator for this blog

Major issues to be fixed before release:

* JSON file is appended for each edit, this should not happen
* Why are posts listed in reverse Chronological Order?

made a chgange..



There a couple of rough edges but the static generator is mostly functional. I have started using it for blogging and publishing inline notes. The aim is not to become a static generator, but rather a lightweight note management system. 

Python and angular.js are the two main technologies used. The static generation happens in python. Notes can be made inline or in markdown files, which are stored in a notes/ folder. Python then asks git for changes in this folder, parses the file, converts it file to html, puts them in a nice json file which is then used by angular on the frontend. For a detailed README visit 

## Supported Markdown Features

* *italics*
* __bold__
* unordered lists

>Block Quotes

```
print "code blocks"
```

__To Do__

1. If user changes title, rename the file
2. Generate standalone html for permalinking
3. Wiki features-- revision history, etc.
4. Add ipython notebook support.

Created on 14-09-2014 05:38:55
Tags:python,angular,github
