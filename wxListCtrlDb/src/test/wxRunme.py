'''
Created on Aug 7, 2012

@author: moz

references:
* http://wiki.wxpython.org/ListControls
'''

from Gui import MyFrame
import wx
from test.SimpleDb import SimpleDb
#from ListCtrlDb import InitListCtrl, ListCtrlInsert, ListCtrlUpdate

class wxListCtrlTestFrame(MyFrame):
    def OnClickQuit(self, event):
        self.Destroy()

    def OnClickInit(self, event):
        self._sql = SimpleDb()
        for i in range(0, 10): #@UnusedVariable
            self._sql.InsertData()

#        InitListCtrl( self._sql.GetAllData(), self.list_ctrl_1)
#        ListCtrlInsert( self._sql.GetAllData(), self.list_ctrl_1)
        self.list_ctrl_1.InitFromDb(self._sql.GetAllData())
        self.list_ctrl_1.InsertFromDb(self._sql.GetAllData())
    
    def OnClickInsert(self, event):
        EntryId = self._sql.InsertData()
#        ListCtrlInsert( self._sql.GetData( EntryId ), self.list_ctrl_1)
        self.list_ctrl_1.InsertFromDb(self._sql.GetData( EntryId ))


    def OnClickUpdate(self, event):
        EntryId = 5
        self._sql.UpdateData( EntryId )
#        ListCtrlUpdate( self._sql.GetData( EntryId ), self.list_ctrl_1)
        self.list_ctrl_1.UpdateFromDb(self._sql.GetData( EntryId ))


if __name__ == '__main__':
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = wxListCtrlTestFrame(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()