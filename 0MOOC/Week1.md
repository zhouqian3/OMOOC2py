#第二周 （2015-10-17）
###本周任务  
* 完成一个极简交互式日记系统，需求如下：
	*  一次接收输入一行日记
	*  保存为本地文件
	*  再次运行系统时,能打印出过往的所有日记
*  发布到各自仓库的`_src/om2py0w/0wex1/`目录中
*  指标：
	*  包含软件使用说明书:｀README.md｀
	*  能令其它学员根据说明书,运行系统,完成所有功

###完成过程
已经w2了，w1的任务仍没有头绪，只好——抄！！！！  
一开始觉得抄袭这个事情貌似挺不应该的，要自己探索，但是在C2T2的[顿悟](OMOOC/week1_C2T2)后，发现这是我唯一赶上课程进度的比较实际的方法了。

1. 先无耻地挑抄袭对象，在[[1w]学员任务 提交处](https://github.com/OpenMindClub/OMOOC2py/issues/41)这个贴子观摩多久，决定抄[@zoejane](https://github.com/OpenMindClub/OMOOC2py/issues/32)这位同学的作业！！因为比较喜欢这位同学干净整洁的风格～ （对的，我是傲娇的处女座）——后继发现这名初当妈妈的zoe同学太值得学习啦！！！
2. 先试跑zoe同学的[代码](https://github.com/zoejane/OMOOC2py/blob/master/_src/om2py0w/0wex1/diary.py)，成功！
3. 通读一遍他写的[纪录](https://zoejane.gitbooks.io/omooc2py/content/1sTry/love-of-programming.html)，决定还是直接看代码吧，代码里看到以下函数，并查阅(温习)了相关用法
	- import time: [官方文档](https://docs.python.org/2/library/time.html)，但官方文档一直都挺难读的，有个比较好的sample教程在[这里](https://pymotw.com/2/time/)。代码中的time.striftime即为转换为string的时间展示方法，`('%Y/%m/%d') `对应的格式为`2015/11/01`
	- raw_input: [官方文档](https://docs.python.org/2/library/functions.html#raw_input)，温习了下括号里放prompt(提示语)的用法，并换成了颜文字 `ε=ε=ε=ε=ε=ε=┌(;￣◇￣)┘`额，成功
	- if statement: [官方文档](https://docs.python.org/2/tutorial/controlflow.html)比较简单直接
	- while loop: 一个比较简单的[介绍](http://www.tutorialspoint.com/python/python_while_loop.htm)，另外break语句是用来 终止 循环语句的，即哪怕循环条件没有称为False或序列还没有被完全递归，也停止执行循环语句。
	- open & read: [官方文档](https://docs.python.org/2/library/functions.html#open)不太好懂。基本上，是要建立一个File Object: `file object = open(file_name [, access_mode][, buffering]) `，比如：`fo = open("foo.txt", "wb")`。buffering暂时貌似用不到，至于acesss_mode
		- r是只读，也是不填时候的默认模式
		- r+是读和写
		- w是只写，如果文件已经存在的话就覆盖现有内容
		- a是appending，也就是写在文档的末尾，是任务需要用到的模式
		- a+是又附加又读  
		说实话我搞不清为何需要这么多mode，[这里](http://www.tutorialspoint.com/python/python_files_io.htm)有关于mode的一个比较全的介绍。另外笨方法的第[15](http://learnpythonthehardway.org/book/ex15.html)和[16](http://learnpythonthehardway.org/book/ex16.html)题有比较详细讲到文档的读写
		以及fileobject的close，我不太明白为何要去close file，官方文档的解释是说`When you’re done with a file, call f.close() to close it and free up any system resources taken up by the open file. After calling f.close(), attempts to use the file object will automatically fail.`

4. 修改了问候语，zoe的风格实在太过于妹纸
5. 修改了syntax
	- print 后面为啥要用`( )` ？不太理解，故把括号删了
	- 修改了一下后面的while loop，让用户可以持续写入，而不是在第二次写完后就结束了。
6. 总结一下这个任务实现的逻辑：将input设为一个variable，通过一个if statement判断输入内容，若输入为空，则打开日记文档，转为一个file object，再转为string，若输入不为空则将输入内容已a+模式写入文档， 同时用一个while loop来实现询问是否要继续输入，继续输入则重复上一步骤，不继续输入则停止的过程。  
  
最后上传这个作业已经是w4了，这几个礼拜略忙，心中一万匹草泥马飘过，希望还有机会能赶上课程进度。哎～～