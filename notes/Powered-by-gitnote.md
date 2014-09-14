#Powered by gitnote

This blog is "powered" by [GitNote](lekhakpadmanabh.github.io) - a command line note management utility I wrote up quickly to cater specifically to my requirements. There are a couple of rough edges but it is mostly functional. At this point I cannot recommend anyone to use it, mainly because it is being built and tested on github pages, which forbids angular's routing-- which means no permalinking to individual articles. When I was writing it this wasn't a concern for me, but I will probably write its own cusotm backend one of these days.

##Usage

Notes can be made inline or in markdown files, which are stored in a notes/ folder. Python then asks git for changes in this folder, parses the file, converts it file to html, puts them in a nice json file which is then used by angular on the frontend. For a detailed README visit 

Source code: 
Technologies: git, python, javascript (Angular), css (bootstrap), html

### New note default

```
gitnote new -t "Powered by gitnote" -g "python,angular,github, git"

```

You can also use the verbose flags,`--title` and  `--tags`. The above command creates a opens a new file in your default text-editor. Enter your note in markdown, save it, close and run 

```
gitnote build
```

If it is your first time it'll ask for some adidtional info, then your note is tracked and committed. Now you just push to whatever is your remote static file server and you're done. In my case, I am using the free github pages.

```
git push origin master
```

### New note inline

For short notes, 

```
gitnote inline -b "hello world" -t "this is the title" -g "hello,world"
```

and that's all.






## Supported Markdown Features

* *italics*
* __bold__
* unordered lists

1. Ordered
2. List

>Block Quotes

```python
print "code blocks"
```

Images: ![wwgd](/images/wwgd.png)



## To Do

1. If user changes title, rename the file
2. Generate standalone html for permalinking
3. Wiki features-- revision history, etc.
4. Add ipython notebook support.

Created on 14-09-2014 23:20:18
Tags:python,angular,github, git
