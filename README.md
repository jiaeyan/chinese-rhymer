# 中文押韵器 Chinese Rhyme
![Build](https://img.shields.io/badge/build-passing-green.svg)
[![PyPI](https://img.shields.io/badge/pypi-v0.1.7.5-blue.svg)](https://pypi.org/project/chrhyme/)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)

## 一、简介
这是一款帮助 _诗歌爱好者_ 和 _说唱爱好者_ 寻找押韵灵感的小工具。  
只要输入一个目标词，和一些限制条件，该工具就能查询词库中所有满足条件的押韵词。  
目前提供 __单押__， __双押__，__三押__ 和 __四押__ 查询功能， 同时支持俗语、科技术语等扩展押韵。  

## 二、安装
系统要求：Python 3 以上。  

    $ pip install chrhyme

## 三、使用

### 1、要求
该工具根据[《汉语拼音方案》](http://www.moe.edu.cn/ewebeditor/uploadfile/2015/03/02/20150302165814246.pdf)对输入词的声母和韵母进行预处理。  
输入词长度要求为`1-4`，任何在该长度以下或以上的输入词视为不合法。该工具会自动去除输入词汉字以外的任何元素。  

### 2、功能：
用例：`长江 (cháng jiāng)`  
* 声母组合：(ch, j)  
* 全韵母组合：(ang, iang)
* 半韵母组合：(ang, ang)  
* 声调组合：目前不支持声调押韵。

默认情况下，为得到最大匹配效果，该工具按照 __半韵母组合__ 进行查找。  
 
#### 条件设置  
* 声母押韵：输入想要押相同声母的字的位置，从左数起，1 为`长`, 2 为`江`，12 为`长江`，顺序任意。任何大于 2 的数字都被视为 2。如果不押声母，输入 `0`。  
* 全韵母押韵：输入想要押全韵母的字的位置，从左数起，1 为`长`, 2 为`江`，12 为`长江`，顺序任意。任何大于 2 的数字都被视为 2。如果不押全韵母，输入 `0`。  

### 3、命令行
    $ chrhyme  

然后，请根据命令行提示进行操作。运行样例如下：  

<img src="https://github.com/jiaeyan/chinese-rhyme/blob/master/chrhyme/data/demo.png" alt="demo" width="450" height="250"/>


## 四、版本更新
* v0.2.0 (05/10/2018)  
1、开放单押功能  
2、支持扩展押韵，如输入词为"报恩"，可以查询到"一朝天子一朝臣"，即长度扩展的匹配词尾部与输入词押韵。  
3、区分 si (思), shi (诗), ji (机) 三类不同发音的 i  
4、扩大词库 (_70万细胞词_)  
5、兼容所有Python 3 版本

* v0.1.5 (05/04/2018)  
1、区分发音不同的 an 和 ian ，以及 e 和 ie 

* v0.1.0 (05/03/2018)  
1、开放双押、三押和四押功能  
2、支持声母及全韵母押韵


## 五、相关项目

本项目使用的汉字转拼音系统来自：  
[汉字拼音转换工具 (Python版)](https://github.com/mozillazg/python-pinyin) 。
