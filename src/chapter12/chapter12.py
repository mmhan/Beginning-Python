#!usr/bin/python2

import wx

app = wx.App()

win = wx.Frame(None, title = "Simple Editor")
win.Show()

loadButton = wx.Button(win, label = 'Open',
                       pos=(225,5), size=(80, 25))
saveButton = wx.Button(win, label = 'Save',
                       pos=(315,5), size=(80,25))

filename = wx.TextCtrl(win, pos=(5,5), size = (210,25))

contents = wx.TextCtrl(win, pos = (5, 35), size = (390,260),
                       style = wx.TE_MULTILINE | wx.HSCROLL)



win = app.MainLoop()