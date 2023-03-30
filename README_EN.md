[中文](README.md) | English

# Intro
Import media to DaVinci Resolve media pool from multiple location at one time.

# 🔧 Installation

- Please move *Batch_Importer.py* to Resolve script folder:
  - macOS: /Users/{USER}/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Edit
  - Windows: C:\Users\{USER}\AppData\Roaming\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts\Edit

- then you can find scripts in menu under *Workspace* > *Scripts*.
- Note that the script only runs inside Resolve.


# 🎛 Usage

1. Enter or paste path into *Address Bar*. You can use wildcards for fuzzy matching. For full matching rules, please refer to [glob(programming) - Wikipedia](https://en.wikipedia.org/wiki/Glob_(programming)) or [Python Official Website](https://docs.python.org/3/library/glob.html).

2. Click *Append path* to get all results in the *Pending List* below.

3. Don't mind any unexpected results, select the required part of the path in the pending list, or select all directly, and click *Import selected* to start importing (to the current media pool folder)

4. To clean the pending list, click *Clean all*.

5. You can see a progress bar during the import process (depending on the number of paths you have selected).

# 🧷 E.g. 

|  Entered Path  |  Matched Path  | Unmatched Path |
| --- | --- | --- |
|  /Volumes/A0*  | /Volumes/A01<br>/Volumes/A02<br>/Volumes/A03<br>...  | /Volumes/B01<br>/Volumes/B02<br>/Volumes/A12<br>... |
|  /Volumes/Project/202303*/ARRIRAW |  /Volumes/Project/20230301/ARRIRAW<br>/Volumes/Project/20230302/ARRIRAW<br>/Volumes/Project/20230303/ARRIRAW<br>/Volumes/Project/20230304/ARRIRAW<br>...  |  /Volumes/Project/20230401/ARRIRAW<br>... |
|  /Sample_Footage/[AR]* | /Sample_Footage/ARRIRAW<br>/Sample_Footage/RED | /Sample_Footage/DJI |

# ℹ️ TIPS
If the folder you’re importing contains a large number of files, the waiting time will be too long and DaVinci Resolve will become unresponsive. 
In this case, you can use this script to import the contents of this folder separately. 
Although it may take a little longer (determined by the principle of the file system), at least you can see the progress bar and the *Live save* function of Resolve can prevent the software from crashing unexpectedly(without any loss🥲).


# ☝️ Requirements

- DaVinci Resolve 17 or higher version.
- Python 3.6 64-bit.
- Higher versions of Python are not supported before DaVinci Resolve 18.
- No additional third-party libraries are required.

# Support our projects:

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/zhanglaichi)
[!["小黄灯杂货铺"](https://github.com/laciechang/img/blob/master/spotlight_img/mianbaoduo_button.png)](https://mbd.pub/o/works/240920)