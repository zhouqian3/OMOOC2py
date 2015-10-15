# 第一周（2015-10-10）
## 任务   
1. fork [模板仓库](https://github.com/OpenMindClub/OMOOC2py) 将个人仓库提交到[学员分支仓库报到处](https://github.com/OpenMindClub/OMOOC2py/issues/4)
2. 配置个人教程编写环境
 - 配置好个人仓库和 gitbook 的绑定
 - 形成自动私人教程的发布  
 	- 向 github 个人仓库提交文档  
 	- gitbook 自动完成编译
 - 将发布地址提交到[学员教程报到处](https://github.com/OpenMindClub/OMOOC2py/issues/5) 
3. 立即开始编程：
 - 根据[极简Python上手导念](https://github.com/OpenMindClub/OMOOC2py/issues/5)中的一页解说Python代码录入为个人仓库中的`_src/om2py0w/0wex0/main.py`
 - 并将其功能化，即，基于现有42行代码涉及的能力设计一个可用的小功能并完成对应的开发教程,包含:
	- 功能设计
    - 技术要点
    - 实现难点
    - 涉及知识  
确保每一个可运行版本,都及时 push 到个人仓库中

## 完成情况
1. 这个比较简单，点一下fork就好
2. 在Gitbook里折腾了好不会儿，但其实也只是把刚刚fork的github仓库import到gitbook里来，授权一下账户什么的，就自动绑定好了。
	Gitbook和Github都有线上的编辑器，但是其实这里的意思应该是让你把repository clone到自己的电脑上，在电脑上编辑文档，再commit到github里，最终同步到gitbook。
	关于Gitbook中Disqus评论框plugin的配置方法，我自己研究了好久都没成功，还装了一堆node.js之类的东西，还是我朋友谷溪比较牛逼，看了他写的[教程](https://zjuguxi.gitbooks.io/hard-way-to-python/content/week/disqus.html)瞬间搞定。
3. 未完成