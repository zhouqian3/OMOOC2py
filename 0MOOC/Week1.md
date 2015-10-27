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
3. 通读一遍他写的[纪录](https://zoejane.gitbooks.io/omooc2py/content/1sTry/love-of-programming.html)，决定还是直接看代码吧
	- sys.argv：这个在笨方法[第13题](http://learnpythonthehardway.org/book/ex13.html)有介绍

4. 代码里看到以下函数，并查阅(温习)了相关用法
	- import time: [官方文档](https://docs.python.org/2/library/time.html)，但官方文档一直都挺难读的，有个比较好的sample教程在[这里](https://pymotw.com/2/time/)
	- raw_input: [官方文档](https://docs.python.org/2/library/functions.html#raw_input)，温习了下括号里放prompt(提示语)的用法，并换成了颜文字 `ε=ε=ε=ε=ε=ε=┌(;￣◇￣)┘`额，成功
5. 修改了问候语，zoe的风格实在太过于妹纸
6. 修改了syntax
	- print 后面为啥要用`( )` ？不太理解，故把括号删了
<至oct 27 晚，待续>