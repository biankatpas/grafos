import wx
import wx.lib.scrolledpanel as scrolled
import numpy as np
import PIL
from PIL import Image

app = wx.App()

class Gui(wx.Frame):

    def __init__(self, *args, **kw):
        super(Gui, self).__init__(*args, **kw)
        self.Center()
        self.SetMaxSize(self.GetSize())
        self.SetMinSize(self.GetSize())
        self.SetBackgroundColour(colour=wx.WHITE)
        self.scrolled_panel = scrolled.ScrolledPanel(self, -1, size=(914, 573), pos=(400,0) , style=wx.SUNKEN_BORDER)
        self.scrolled_panel.SetBackgroundColour(wx.WHITE)
        self.bitmap = wx.StaticBitmap(parent=self.scrolled_panel)
        self.text_area = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE | wx.BORDER_SUNKEN | wx.TE_READONLY | wx.TE_RICH2)
        self.text_area.SetPosition((400, 585))
        self.text_area.SetSize((914,260))
        self.text_area.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL))
        self.text_area.AppendText("Nothing have done yet!" + "\n\n")
        self.text_area.SetToolTip('Saída')
        self.factor = 1
        self.button_id = 0
        self.buttons = []

    def add_button(self, text, pos, size=(400, 65), callback=None):
        self.button_id += 1
        bt = wx.Button(self, self.button_id, text, pos=pos, name=text, size=size)
        bt.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL))
        bt.Bind(wx.EVT_BUTTON,  callback)
        self.buttons.append(bt)

    def show_input_dialog(self, title='Text Entry', text='Enter some text', value=""):
        dlg = wx.TextEntryDialog(self, text, title)
        dlg.SetValue(value)
        if dlg.ShowModal() == wx.ID_OK:
            # print('You entered: %s\n' % dlg.GetValue())
            return dlg.GetValue()
        dlg.Destroy()
        return None

    def draw_graph(self, file="graph.gv.png"):
        image = wx.Image(file)
        apil = self.imageToPil(image)
        width, height = apil.size
        apilr = apil.resize((int(width * self.factor), int(height * self.factor)), PIL.Image.NEAREST)
        myWxImage = wx.Image(apilr.size[0], apilr.size[1])
        myWxImage.SetData(apilr.convert('RGB').tobytes())
        self.bitmap = myWxImage.ConvertToBitmap()
        self.scrolled_panel.Bind(wx.EVT_PAINT, self.on_paint)
        self.scrolled_panel.Refresh()

    def imageToPil(self, myWxImage):
        w, h = myWxImage.GetWidth(), myWxImage.GetHeight()
        buf  = myWxImage.GetDataBuffer()
        arr  = np.frombuffer(buf, dtype='uint8')
        myPilImage = PIL.Image.frombytes("RGB", (w, h), arr.tobytes('C'))
        return myPilImage

    def on_paint(self, evt):
        dc = wx.PaintDC(self.scrolled_panel)
        dc.DrawBitmap(self.bitmap, (0, 0))

    def on_zoom_in(self, evt):
        self.factor += 0.25
        self.draw_graph()

    def on_zoom_out(self, evt):
        self.factor -= 0.25
        self.draw_graph()

    def get_buttons(self):
        return self.buttons

    def main_loop(self):
        app.MainLoop()
