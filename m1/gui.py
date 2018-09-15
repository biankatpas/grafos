import wx

app = wx.App()

class Gui(wx.Frame):

    def __init__(self, *args, **kw):
        super(Gui, self).__init__(*args, **kw)
        self.Center()
        self.SetMaxSize(self.GetSize())
        self.SetMinSize(self.GetSize())
        self.SetBackgroundColour(colour=wx.WHITE)
        self.bitmap = wx.StaticBitmap(parent=self)
        self.button_id = 0
        self.buttons = []


    def addButton(self, text, pos, size=(400, 65), callback=None):
        self.button_id += 1
        bt = wx.Button(self, self.button_id, text, pos=pos, name=text, size=size)
        bt.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL))
        bt.Bind(wx.EVT_BUTTON,  callback)
        self.buttons.append(bt)


    def addViewer(self, file="graph.gv.png"):
        self.image = wx.Image(file)
        self.image.Scale(width=925, height=779, quality=wx.IMAGE_QUALITY_HIGH)
        self.bitmap = self.image.ConvertToBitmap()
        self.Bind(wx.EVT_PAINT, self.OnPaint)


    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bitmap, 400, 0)


    def getButtons(self):
        return self.buttons


    def MainLooop(self):
        app.MainLoop()
