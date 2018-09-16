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
        self.text_area = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE | wx.BORDER_SUNKEN | wx.TE_READONLY | wx.TE_RICH2)
        self.text_area.SetPosition((400, 585))
        self.text_area.SetSize((914,195))
        self.text_area.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL))
        self.text_area.AppendText("Nothing have done yet!" + "\n\n")
        self.text_area.SetToolTip('Saída')

    def add_button(self, text, pos, size=(400, 65), callback=None):
        self.button_id += 1
        bt = wx.Button(self, self.button_id, text, pos=pos, name=text, size=size)
        bt.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL))
        bt.Bind(wx.EVT_BUTTON,  callback)
        self.buttons.append(bt)

    def render_graph(self, file="graph.gv.png"):
        image = wx.Image(file)
        # TODO: rezise image
        # don't know why this doesn't work
        # self.image.Scale(width=925, height=779, quality=wx.IMAGE_QUALITY_HIGH)
        self.bitmap = image.ConvertToBitmap()
        self.Bind(wx.EVT_PAINT, self.on_paint)

    def on_paint(self):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bitmap, 400, 0)

    def get_buttons(self):
        return self.buttons

    @staticmethod
    def main_loop():
        app.MainLoop()
