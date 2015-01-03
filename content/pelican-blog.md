Title: 把你的blog从octopress迁移到pelican吧(1)
Slug: pelican-blog
Category: Tech

在很久很久之前有一个用[octopress][1]在github pages上搭建的blog, octopress提供使用markdown的方式来写blog，非常的方便，而且默认提供的功能和模板也足够的强大。
然而唯一的缺陷是是使用Ruby及Rake来配置和部署，简单看了一下，感觉比较不易读, 要自定义以及扩展起来比较麻烦，而且产生blog的目录结构也复杂不够直观。
如果有一个同样支持markdown同时可以提供相同功能，而更易用的Python版本octopress那多好啊。
于是一小心发现到基于Python的[pelican][2]这个项目就马上感觉就是这个了，于是就有了本次的迁移。

<!-- more -->

# pelican的特性

说说我认为pelican的优点：

1. 由Python实现，配置文件简单清晰，主题基于Jinja，扩展方便
2. 官方提供[pelican-plugins][3]及[pelican-themes][4]，提供大量已有的插件和主题, 懒人必备
3. 目录结构清晰，没有复杂的层次结构
4. 默认使用make来自动化提交，更通用，相比rake, 更易于自定义和改进

然而相比于octopress的缺点也不是没有，首先是默认主题就没有octopress功能完整和好用，同时默认安装如果要布置到github pages上还需要自己手动配置。接下来我会说说[官方文档][5]中没有提到的上述的配置。 

# pelican的安装

在官方文档的[安装指南][6]有的东西，我这里就不再重重复。

总的来说安装其实很简单，直接使用`pip install pelican`即可。

然后使用`pelican-quickstart`命令在当前目录下建立一个初始的目录结构，如下


	├── content
	├── develop_server.sh
	├── fabfile.py
	├── Makefile
	├── output
	├── pelicanconf.py
	└── publishconf.py

其中`pelicanconf.py`是本地测试使用的配置, 而`publishconf.py`则是使用`make publish`对外发布时使用的配置。
`content`用于存放markdown和相关静态文件的源目录，所生成的静态网站将会输出到`output`目录中。

# pelican的配置运行

我们可以直接在`content`目录下，建立一个`test.md`文件作为实验，输入如下内容:

	:::markdown
	Title: My First Article
	Date: 2014-12-31 10:20
	Category: Test
	Tags: Hello, Lift

	This is the first article in the blog.

现在就可以使用命令`make devserver`来启动一个本地默认可以访问的http://localhost:8000测试http服务器, 并通过默认测试配置`pelicanconf.py`来生成的blog的静态网页。

Ok，到此为此，pelican就正式配置运行起来啦，下次将会说一下具体`pelicanconf.py`和`publishconf.py`的配置，特有功能，插件以及主题的使用。


[1]: http://octopress.org
[2]: http://blog.getpelican.com/
[3]: https://github.com/getpelican/pelican-plugins
[4]: https://github.com/getpelican/pelican-themes
[5]: http://docs.getpelican.com/en/3.5.0/settings.html
[6]: http://docs.getpelican.com/en/3.5.0/quickstart.html
