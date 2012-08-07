#!/usr/bin/env python
# -*- coding: ansi_x3.4-1968 -*-
# generated by wxGlade 0.6.5 on Tue Aug  7 20:55:43 2012

import wx

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.label_1 = wx.StaticText(self, -1, "Use insert to insert a new entry and update to update.\nBoth generates random data.")
        self.button_Init = wx.Button(self, -1, "Init")
        self.button_insert = wx.Button(self, -1, "Insert")
        self.button_update = wx.Button(self, -1, "Update")
        self.static_line_1 = wx.StaticLine(self, -1)
        self.button_Quit = wx.Button(self, -1, "Quit")
        self.list_ctrl_1 = wx.ListCtrl(self, -1, style=wx.LC_REPORT | wx.SUNKEN_BORDER)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.OnClickInit, self.button_Init)
        self.Bind(wx.EVT_BUTTON, self.OnClickInsert, self.button_insert)
        self.Bind(wx.EVT_BUTTON, self.OnClickUpdate, self.button_update)
        self.Bind(wx.EVT_BUTTON, self.OnClickQuit, self.button_Quit)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("frame_1")
        self.SetSize((569, 380))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(self.label_1, 1, 0, 0)
        sizer_5.Add(self.button_Init, 0, 0, 0)
        sizer_5.Add(self.button_insert, 0, 0, 0)
        sizer_5.Add(self.button_update, 0, 0, 0)
        sizer_3.Add(sizer_5, 1, wx.EXPAND, 0)
        sizer_3.Add(self.static_line_1, 0, wx.EXPAND, 0)
        sizer_4.Add((20, 20), 1, wx.EXPAND, 0)
        sizer_4.Add(self.button_Quit, 0, 0, 0)
        sizer_3.Add(sizer_4, 0, wx.EXPAND, 0)
        sizer_2.Add(sizer_3, 0, 0, 0)
        sizer_2.Add(self.list_ctrl_1, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def OnClickQuit(self, event):  # wxGlade: MyFrame.<event_handler>
        print "Event handler `OnClickQuit' not implemented!"
        event.Skip()

    def OnClickInit(self, event):  # wxGlade: MyFrame.<event_handler>
        print "Event handler `OnClickInit' not implemented"
        event.Skip()

    def OnClickInsert(self, event):  # wxGlade: MyFrame.<event_handler>
        print "Event handler `OnClickInsert' not implemented"
        event.Skip()

    def OnClickUpdate(self, event):  # wxGlade: MyFrame.<event_handler>
        print "Event handler `OnClickUpdate' not implemented"
        event.Skip()

# end of class MyFrame
if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = MyFrame(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()