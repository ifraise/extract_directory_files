# extract_directory_files
提取目录中的文件。从多个目录中提取文件进行汇总。

递归扫描指定根目录下的所有文件。

按原文件名（重名加 (n) 序号）平铺移动到单一输出文件夹。

默认在原根目录同级创建 _flattened 文件夹，也可命令行自定义。

使用：

```bash
# 把当前目录及子目录所有文件集中到 ../_flattened
python flatten_dirs.py

# 指定目录
python flatten_dirs.py /home/data

# 同时指定输出目录
python flatten_dirs.py /home/data  /tmp/files
```
