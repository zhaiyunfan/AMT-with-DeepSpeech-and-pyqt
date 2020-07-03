# AMT-with-DeepSpeech-and-pyqt

## 项目概述

一个基于用Pytorch实现的DeepSpeech2框架的，自动的打谱软件

乐谱的输出方式为kern文件，并使用[VerovioHumdrumViewer](https://verovio.humdrum.org/)提供修改和预览功能，客户端GUI使用PyQt5实现

## 工作流概述

现在的思路：

### 离线版

~~1.输入mp3文件，通过deepspeech框架和已经训练好的RNN模型，输出**kern文件，gui使用pyqt5构建~~

>由于这套框架只能在Ubuntu下使用，此处作罢

2.通过127本地端口上加载的verovio-humdrum-viewer来打开**kern文件，或者直接使用命令行VHV，并将其渲染成pdf或者svg图片

>这一条可以接受

3.VHV中提供对**kern的修改功能

>这一条可以很好的实现，可以试试能不能把浏览器页面内嵌到自己的gui程序里，如果不行就拉个线程自动运行VHV服务

### 在线版

1.由于deepspeech和VHV很难在win下安装，所以直接将模型部署到服务器上，并在服务器上提供在线的VHV

>这条可以部分接受，再起个docker并买个能跑动预测的服务器成本太高了，所以直接在我自己的电脑上架个服务器，向客户端提供上传MP3文件和下载生成的kern文件的端口，服务端接受到MP3文件后自动执行单样本预测的命令，直接生成对应kern文件并传回给gui

### 最终流程

-服务端

在Ubuntu下架设一个服务器，接收来自客户端的MP3文件上传，上传完成后执行single transcription脚本，并把输出的kern文件返回给客户端

-客户端

用PyQt5写的GUI，提供MP3上传的功能，并在上传完成后自动下载生成的kern文件，下载完成后自动启动本机的VHV服务，依次提供kern文件的预览、修改和试听功能~~这一部分已经完成了，需要研究下VHV能不能直接嵌入到PyQt5的GUI里面~~
