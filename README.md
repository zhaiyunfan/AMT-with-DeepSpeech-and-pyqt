# AMT-with-DeepSpeech-and-pyqt

## 工作流概述

现在的思路：

### 离线版

1.输入mp3文件，通过deepspeech框架和已经训练好的RNN模型，输出**kern文件，gui使用pyqt5构建

2.通过127本地端口上加载的verovio-humdrum-viewer来打开**kern文件，或者直接使用命令行VHV，并将其渲染成pdf或者svg图片

3.VHV中提供对**kern的修改功能

### 在线版

1.由于deepspeech和VHV很难在win下安装，所以直接将模型部署到服务器上，并在服务器上提供在线的VHV
