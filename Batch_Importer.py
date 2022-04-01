# -*- coding:utf-8 -*-
# Author: 张来吃
# Version: 1.0.0
# Contact: laciechang@163.com

# -----------------------------------------------------
# 本工具仅支持在达芬奇内运行
# -----------------------------------------------------

import glob
import time

fu = bmd.scriptapp('Fusion')
resolve = bmd.scriptapp('Resolve')
pj = resolve.GetProjectManager().GetCurrentProject()

ui = fu.UIManager
disp = bmd.UIDispatcher(ui)

ProgressBar = "ProgressBar"
ProgressBarBG = "ProgressBarBG"
input_pattern = "input_pattern"
add_path = "add_path"
clean_path = "clean_path"
start_import = "start_import"
infomation = "infomation"
path_tree = "path_tree"

window_01 = [
        ui.VGroup({"Spacing": 5},
        [
            ui.HGroup({"Spacing": 5, "Weight": 0},
            [
                ui.LineEdit({"ID": input_pattern, "PlaceholderText": "e.g. /Volumes/*/Source"}),
                ui.Button({"ID": add_path, "Text": "添加路径", "Weight": 0}),
            ]),
            ui.Tree({"ID": path_tree, "AlternatingRowColors": True, "HeaderHidden": True, "SelectionMode": "ExtendedSelection", "Weight": 2}),
            ui.HGroup({"Spacing": 5, "Weight": 0},
            [
                ui.Button({"ID": clean_path, "Text": "清除所有", "Weight": 0}),
                ui.Label({"ID": infomation, "Text": "" , "Weight": 1}),
                ui.Button({"ID": start_import, "Text": "导入选中部分", "Weight": 0}),
            ]),
            ui.Stack({"ID": "pg_set", "Weight": 0},[
                        ui.Label({"ID": ProgressBarBG, "Visible":False, "StyleSheet": "max-height: 3px; background-color: rgb(37,37,37)",}),
                        ui.Label({"ID": ProgressBar, "Visible":False, "StyleSheet": "max-height: 1px; background-color: rgb(102, 221, 39);border-width: 1px;border-style: solid;border-color: rgb(37,37,37);",})
            ]),
        ])
]

dlg = disp.AddWindow({ 
                        "WindowTitle": "批量导入媒体池", 
                        "ID": "MyWin", 
                        "Geometry": [ 
                                    600, 300, # position when starting
                                    800, 300 #width, height
                         ], 
                        }, window_01)

itm = dlg.GetItems()

def increase_pgbar(ratio):
    itm[ProgressBar].Visible = True
    total_width = int(itm[ProgressBarBG].GetGeometry()[3])
    width = total_width * ratio
    itm[ProgressBar].Resize([int(width), 3])

itm[ProgressBar].Resize([1, 3])

def _show_all_path(ev):
    file_list = glob.glob(itm[input_pattern].Text)
    toplevelitems = []
    for i in file_list:
        row = itm[path_tree].NewItem()
        row.Text[0] = i
        toplevelitems.append(row)
    itm[path_tree].AddTopLevelItems(toplevelitems)

def _clean_all_path(ev):
    itm[path_tree].Clear()

def _start_import(ev):
    itm[start_import].Enabled = False
    file_list = []
    items = itm[path_tree].SelectedItems()
    for i in items:
        file_list.append(items[i].Text[0])
        
    length = len(file_list)
    ms = resolve.GetMediaStorage()
    for i in range(0, length):
        itm[infomation].Text = " 🔍 " + str(file_list[i])
        ratio = float(i/(length-1)) if length>1 else 1
        increase_pgbar(ratio)
        ms.AddItemListToMediaPool(str(file_list[i]))
        time.sleep(0.2)
    itm[ProgressBar].Visible = False
    itm[start_import].Enabled = True 

def _func(ev):
    disp.ExitLoop()

dlg.On.MyWin.Close = _func
dlg.On[start_import].Clicked = _start_import
dlg.On[add_path].Clicked = _show_all_path
dlg.On[clean_path].Clicked = _clean_all_path

if __name__ == "__main__":
    dlg.Show()
    disp.RunLoop()
    dlg.Hide()