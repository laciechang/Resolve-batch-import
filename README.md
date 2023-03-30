中文 | [English](README_EN.md)

# 📖 简介
同时从多个位置中导入媒体至 DaVinci Resolve 媒体池

# 🔧 安装

- 请将 *Batch_Importer.py* 拷贝至DaVinci Resolve指定的脚本存放目录下

- macOS: /Users/{你的用户名}/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Edit

- Windows: C:\Users\{你的用户名}\AppData\Roaming\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts\Edit

- 在菜单：工作区(Workspace) > 脚本(Scripts) 中即可找到

- 仅支持在DaVinci Resolve内使用，不支持在外部运行

  

# 🎛 用法

1. 在地址栏中输入或粘贴路径，使用通配符来进行模糊匹配。完整的匹配规则请参见[glob(programming) - Wikipedia](https://en.wikipedia.org/wiki/Glob_(programming)) 或 [Python 官网](https://docs.python.org/3/library/glob.html)。

2. 点击 *Append path* 即可获取匹配的结果，并在下方的*待选列表*中展示。

3. 不必介意匹配出的额外选项，请在列表中选择所需的路径（也可以直接全选），然后点击*Import selected*即可开始导入所选部分到当前媒体池的媒体夹。

4. 点击*Clean all*清除列表。

5. 导入过程中可以看到一个进度条，具体取决于你选择的路径数量。

# 🧷 例如

|  输入的路径  |  匹配到的路径  | 不会匹配的路径 |
| --- | --- | --- |
|  /Volumes/A0*  | /Volumes/A01<br>/Volumes/A02<br>/Volumes/A03<br>...  | /Volumes/B01<br>/Volumes/B02<br>/Volumes/A12<br>... |
|  /Volumes/Project/202303*/ARRIRAW |  /Volumes/Project/20230301/ARRIRAW<br>/Volumes/Project/20230302/ARRIRAW<br>/Volumes/Project/20230303/ARRIRAW<br>/Volumes/Project/20230304/ARRIRAW<br>...  |  /Volumes/Project/20230401/ARRIRAW<br>... |
|  /Sample_Footage/[AR]* | /Sample_Footage/ARRIRAW<br>/Sample_Footage/RED | /Sample_Footage/DJI |

# ℹ️ TIPS
如果你导入的文件夹包含了海量的文件会导致等候时间过长，并且软件会失去响应，此时你可以通过这个工具分开导入这个文件夹中的内容。
虽然结果一致，并且可能花费的时间更长一点（由文件系统的原理决定），但起码你能看见进度条，并配合*自动保存*功能也可以防止软件意外崩溃。

# ☝️ 需要

- DaVinci Resolve 17 或更高版本
- Python 3.6 64-bit 
- 其他版本的 Python 在达芬奇18之前并不支持
- 无需额外的库

# Support our projects:

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/zhanglaichi)

[!["小黄灯杂货铺"](https://github.com/laciechang/img/blob/master/spotlight_img/mianbaoduo_button.png)](https://mbd.pub/o/works/240920)