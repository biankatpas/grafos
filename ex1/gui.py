import wx
import wx.lib.sized_controls as sc
from wx.lib.pdfviewer import pdfViewer

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

    def addViewer(self, file="hello.gv.pdf"):
        self.viewer = pdfViewer(self.panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL | wx.VSCROLL | wx.SUNKEN_BORDER)
        self.viewer.SetSize(483, 800)
        self.viewer.SetPosition((400, 0))
        self.viewer.LoadFile(file)
        self.viewer.Show()

    def getButtons(self):
        return self.buttons

    def MainLooop(self):
        app.MainLoop()
