import wx

app = wx.App()

class Gui(wx.Frame):

    def __init__(self, *args, **kw):
        super(Gui, self).__init__(*args, **kw)
        self.button_id = 0;
        self.text_edit_id = 0;
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.buttons = []
        self.text_editors = []
        self.panel = wx.Panel(self)
        self.Maximize(False)
        self.Center()


    def addButton(self, text, pos, size=(400, 50), callback=None):
        self.button_id += 1
        bt = wx.Button(self.panel, self.button_id, text, pos=pos, name=text, size=size)
        bt.Bind(wx.EVT_BUTTON,  callback)
        self.buttons.append(bt)

    def getButtons(self):
        return self.buttons

    def MainLooop(self):
        app.MainLoop()
