# chinese-word-segmentation

中文分词。

## 1 数据集

### 1.1 简介

-   主题：第二次国际中文分词 Bakeoff（原谅我不知道怎么翻译这个）
-   数据发布时间：2005-11-18（Release 1）
-   数据集内容：文件夹中包含了训练集、测试集和黄金标准（gold-standard）的数据。
同时还有用于计算分数的脚本以及用于生成 baseline 和 topline 的简单分词程序。

### 1.2 训练集和测试集

训练集和测试集包含了四种不同的数据：

```
--------------------------------------------------------------------------------
Corpus             Encoding         Word        Words     Character   Characters
                                    Types                   Types
--------------------------------------------------------------------------------
Academia Sinica    Big Five Plus   141,340    5,449,698     6,117      8,368,050
CityU              HKSCS Big Five   69,085    1,455,629     4,923      2,403,355
Peking University  CP936            55,303    1,109,947     4,698      1,826,448
Microsoft Research CP936            88,119    2,368,391     5,167      4,050,469
--------------------------------------------------------------------------------
```

其中 `Academia Sinica` 和 `CityU` 为繁体字，我们这里只针对简体字进行分词，所以选取 `Peking University` 和 `Microsoft Research` 进行训练和测试。

另外每种数据集又包含了两种不同的编码格式：

1.  GB2312
2.  UTF-8

我们这里选取 `UTF-8` 编码的语料。

### 1.3 下载地址

[Second International Chinese Word Segmentation Bakeoff](http://sighan.cs.uchicago.edu/bakeoff2005/)
