#AI写诗模型训练（只部署请跳过）
1.在对应的train.py文件训练唐诗、宋词、元曲相应的模型
2.对应的dataHandler.py用于获取训练用数据集
3.数据集来源：https://github.com/chinese-poetry/chinese-poetry
请下载，并将文件夹对应命名为"tangshi""songci""yuanqu"，位置与训练代码同层。
4.训练后将得到3个模型和3个wordDic.
5.sample.py用于测试模型效果，可以在其中切换模型，以及输入你想写诗的字。

#网站和本地部署（模型已准备好）
    1.static中包含4个静态网页。templates包含用于ai写诗的动态网页。
    2.首先确保你的电脑有GPU，然后下载"网站和本地部署"整个文件夹。
    3.在命令提示符中，进入该文件夹，输入python generate_poetry.py运行模型。
    4.将出现的链接复制到浏览器，即可在网页上进行AI写诗。
