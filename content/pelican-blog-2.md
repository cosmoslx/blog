Title: 把你的blog从octopress迁移到pelican吧(2)
Slug: pelican-blog-2
Category: Tech
Tags: python, pelican, blog, google, baidu
Series: 把你的blog从octopress迁移到pelican吧

[上篇blog]({filename}pelican-blog-1.md)说明了pelican的安装以及最简单的配置和测试使用，然而只是开始的第一步，在正式开始将octopress迁移过来前，我们还需要搞定几件事：

* 配置github pages的自动部署的配置
* 配置可以使用&lt;!-- more &gt;标签来设置文章摘要
* 配置生成rss或atom
* 配置disqus评论功能支持
* 配置google analytics及baidu站长平台

<!-- more -->

# 配置自动部署到github pages

不像octopress般做到的全自动化, pelican对github pages的自动部署还是需要手动配置的。
而pelican的[官方文档][1]对如何部署到github pages确没有太多的说明。
这节我们就来搞定它。

pelican其实在`makefile`中已经设置了一个`github`的target，只要使用`make github`就可以推送到设置的github pages中。

	:::makefile
	github: publish
		ghp-import -m "Generate Pelican site" -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
		git push origin $(GITHUB_PAGES_BRANCH)

然而如果你直接运行，则会发现会`make`命令运行失败。pelican并没有全自动化的搞定所有配置，因此我们需要手动进行配置。

首先，因为pelican使用`ghp-import`工具来协助将内容推送到对应的github pages的master代码库中(具体的原理，参考`ghp-import`的介绍[页面][2])，所以需要安装它

	:::bash
	pip install ghp-import

然后，需要配置你保存blog原始markdown信息的代码库, 我这里在github中创建的代码库为`github.com/cosmoslx/blog.git`，使用如下命令添加到代码库：

	:::bash
	# 设置对应代码库
	git remote set-url source git@github.com:cosmoslx/blog.git

	# 设置对应代码库为source, 并向它推送
	git push -u source master

接着，配置你想推送的github pages对应的代码库, 我的github page代码库为`github.com/cosmoslx/cosmoslx.github.io.git`。

	:::bash
	# 添加以下内容到.gitignore, 不需要代码管理自动生成的内容
		# pelican 
		*.pid
		cache
		output

	# 设置对应代码库
	git remote set-url origin git@github.com:cosmoslx/cosmoslx.github.io.git

	# 设置对应代码库为source, 并向它推送
	git push -u origin master

最后，这就大功告成，试着提交吧，初次提交github pages官方说明是30分钟以后才完全同步：

	:::bash
	make github

半个小时一下就过去了，今天就到这里，下次我们接着搞定余下的配置，然后就可以尽情地玩耍了:-P

[1]: http://docs.getpelican.com/en/3.5.0/publish.html
[2]: https://github.com/davisp/ghp-import
