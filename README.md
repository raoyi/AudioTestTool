# AudioTestTool
[![LICENSE](https://img.shields.io/github/license/raoyi/AudioTestTool.svg)](https://github.com/raoyi/AudioTestTool/blob/master/LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)]()
[![platform](https://img.shields.io/badge/platform-Windows-blue.svg)]()

windows平台音频测试工具

使用说明：

1、考虑到兼容性问题，使用英文提示信息

2、听到播放的数字后点击相应的按键

3、左右声道分别测试，依据提示点击听到的数字完成测试

4、测试前检查是否存在pass.flg文件，如果存在，删除pass.flg文件

5、测试pass后，自动生成pass.flg文件作为标记

已知bug：v1.0版在PyInstaller打包成exe后弹出GUI速度慢
