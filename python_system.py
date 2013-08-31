1.下载ipython
http://ipython.org/
2.执行linux命令
import subprocess
subprocess.call(["ls","-l","/tmp"])
3.查看某个模块的源码
psource
4.单引号和双引号，在bash和perl中，单引号原样输出，双引号把变量转换后输出；在pyton中没有区别
5.使用'''使字符串跨越多行
6.字符串前加r，原始字符串不解析
s='\t'
s=r'\t'
7.漂亮的列表解析
some_list=range(10)
','.join([str(i) for i in some_list])
','.join(str(i) for i in some_list)
6.我喜欢的with打开文件方法
with open('/root/test.txt','w') as f:
    f.write("test")


