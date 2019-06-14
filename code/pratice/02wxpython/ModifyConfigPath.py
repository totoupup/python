# encoding:utf-8
import wx


# 直接用idea打开会提示“no module named XX”，1.设置project structure -- proejct SDK  会在misc.xml中生成component
# 2. add configuration 选择start script和sdk
# 参考 https://www.cnblogs.com/morries123/p/8568666.html

class ModifyConfigPath(wx.Frame):
    def __init__(self):
        # frame = wx.Frame(None, title='Modify Config Path', pos=(400, 400), size=(400, 400))
        frame = wx.Frame(None, title='Modify Config Path', pos=(400, 300), size=(600, 500))
        panel = wx.Panel(frame)
        path_text = wx.TextCtrl(panel)
        open_button = wx.Button(panel, label="打开")
        save_button = wx.Button(panel, label="保存")
        # wx.TE_MULTILINE多行显示
        content_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        box = wx.BoxSizer(wx.HORIZONTAL)  # 不带参数默认实例化一个水平的尺寸器
        box.Add(path_text, proportion=5, flag=wx.EXPAND|wx.ALL, border=3)
        box.Add(open_button, proportion=2, flag=wx.EXPAND|wx.ALL, border=3)
        box.Add(save_button, proportion=2, flag=wx.EXPAND|wx.ALL, border=3)

        v_box = wx.BoxSizer(wx.VERTICAL)
        v_box.Add(box, proportion=1, flag=wx.EXPAND|wx.ALL, border=3)
        v_box.Add(content_text, proportion=3,flag=wx.EXPAND|wx.ALL, border=3)
        panel.SetSizer(v_box)

        def openfile(event):  # 参数必须为event，其他参数如何添加？
            filesFilter = "Txt (*.txt)|*.txt|All files (*.*)|*.*"  # 文件格式过滤器
            fileDialog = wx.FileDialog(None, defaultDir='E:\\code\\00test\\Python\\Basic\\VisitBolg', message="选择单个文件", wildcard=filesFilter, style=wx.FD_OPEN)
            dialogResult = fileDialog.ShowModal()
            if dialogResult != wx.ID_OK:
                return
            path = fileDialog.GetPath()
            path_text.SetValue(path)
            path = path_text.GetValue()
            with open(path, 'r', encoding='utf-8') as f:
                content_text.SetValue(f.read())
        open_button.Bind(wx.EVT_BUTTON, openfile)
        frame.Show()


def main():
    app = wx.App()
    ModifyConfigPath()
    app.MainLoop()


if __name__ == '__main__':
    main()
