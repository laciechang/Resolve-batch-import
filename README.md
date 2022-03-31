# Resolve-batch-import
同时从多个位置中导入媒体至媒体池

# 🔧 安装

- 请将 *Batch_Importer.py* 拷贝至达芬奇指定的脚本存放目录下

- macOS: /Users/{你的用户名}/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Edit

- Windows: C:\Users\{你的用户名}\AppData\Roaming\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts\Edit

- 使用 v17.3 及以上版本

- 在菜单：工作区(Workspace) > 脚本(Scripts) 中即可找到

- 仅支持在达芬奇内使用，不支持在外部运行

  

# 🎛 用法

- 在地址栏中输入路径，并配合“星号 *”进行模糊匹配，例如 /Documents/A* 即表示Documents路径下，以Test开头的多个文件或文件夹

- 点击【添加路径】即可讲匹配到的所有路径添加到下方待定区域，可以看到匹配的结果

- 匹配有误则可以【清除所有】

- 在待定列表中选择所需的部分路径，或者直接全选，点击【导入选中部分】即可开始执行导入（到当前媒体夹）



# 🧷 TIPS 

一次性导入多块素材盘的素材

将位于多个不同位置、符合特定规则的文件夹、文件导入媒体池中


# ☝️ 需要

- Python 3.6 64-bit 
- 其他版本的 Python 达芬奇并不支持