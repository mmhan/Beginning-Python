#!usr/bin/python2

import wx

def load(event):
    '''
    This function will receive and load a text file from given src and show on the screen
    '''
    file = open(filename.GetValue())
    contents.SetValue(file.read())
    file.close()

def save(event):
    '''
    This function will use the content of the large text box and save it in given file.
    '''
    file = open(filename.GetValue(), 'w')
    file.write(contents.GetValue())
    file.close()

app = wx.App()
win = wx.Frame(None, title = "Simple Editor", size = (410, 335))

bkg = wx.Panel(win)

loadButton = wx.Button(bkg, label = 'Open')
loadButton.Bind(wx.EVT_BUTTON, load)

saveButton = wx.Button(bkg, label = 'Save')
saveButton.Bind(wx.EVT_BUTTON, save)

filename = wx.TextCtrl(bkg)

contents = wx.TextCtrl(bkg,
                       style = wx.TE_MULTILINE | wx.HSCROLL)

hbox = wx.BoxSizer()
hbox.Add(filename, proportion = 1, flag = wx.EXPAND)
hbox.Add(loadButton, proportion=0, flag = wx.LEFT, border = 5)
hbox.Add(saveButton, proportion=0, flag = wx.LEFT, border = 5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion = 0, flag = wx.EXPAND | wx.ALL, border = 5)
vbox.Add(contents, proportion = 1,
         flag = wx.EXPAND | wx.LEFT | wx.LEFT | wx.LEFT, border = 5)

bkg.SetSizer(vbox)
win.Show()

app.MainLoop()
