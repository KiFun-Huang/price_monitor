# price_monitor


## TODO
- 优化代码
- [x] SelenThief爬取方法 未实现商品名等字段的保存
- Sendter 未实现发送至邮箱的方法
- 定时执行，配合发送邮件

## 使用说明
终端运行main.py后，输入读取Url的文件名，以及保存结果的文件名。

- 读取文件支持格式: .xlsx .txt .csv

- 保存文件格式支持: .xlsx .txt


```
# 运行后会提示输入两个文件名
$ python3 main.py 

# filename1 是获取url的文件  filename2是保存结果的文件
# option 只支持 lsdj gwd
$ python3 commandline.py option filename1 filename2
```
