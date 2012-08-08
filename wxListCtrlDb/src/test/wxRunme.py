'''
Created on Aug 7, 2012

@author: moz

references:
* http://wiki.wxpython.org/ListControls
'''

from Gui import MyFrame
import wx
from test.SimpleDb import SimpleDb
import threading
import time

class wxListCtrlTestFrame(MyFrame):
    def __init__(self, *args, **kwds):
        MyFrame.__init__(self, *args, **kwds)
        self._AutoUpdateLoopThread = threading.Thread(target=self._AutoUpdate )        
            
    def OnClickQuit(self, event):
        self.Destroy()

    def OnClickInit(self, event):
        self._sql = SimpleDb()
        for i in range(0, 10): #@UnusedVariable
            self._sql.InsertData()

        self.list_ctrl_1.InitFromDb(self._sql.GetAllData())
        self.list_ctrl_1.InsertFromDb(self._sql.GetAllData())
    
    def OnClickInsert(self, event):
        EntryId = self._sql.InsertData()
        self.list_ctrl_1.InsertFromDb(self._sql.GetData( EntryId ))


    def OnClickUpdate(self, event):
        EntryId = 5
        self._sql.UpdateData( EntryId )
        self.list_ctrl_1.UpdateFromDb(self._sql.GetData( EntryId ))

    def OnClickAuto(self, event):
        self._AutoUpdateLoopThread.start()

    def _AutoUpdate(self):
        ## --------
        # this breaks because sqlite only will work in the same thread that created it
        # EntryId = 5
        # self._sql.UpdateData( EntryId )
        # self.list_ctrl_1.UpdateFromDb(self._sql.GetData( EntryId ))
        ## --------

        # this would break if ListCtrlDb were not thread safe.
        # you are not allowed to update wxWidgets outside the thread the GUI runs in
        sql = SimpleDb()
        for i in range(0, 10): #@UnusedVariable
            sql.InsertData()

        self.list_ctrl_1.InitFromDb(sql.GetAllData())
        self.list_ctrl_1.InsertFromDb(sql.GetAllData())        
        
        while( True ):
            time.sleep( 2 )
            EntryId = 5
            sql.UpdateData( EntryId )
            self.list_ctrl_1.UpdateFromDb(sql.GetData( EntryId ))        
        

if __name__ == '__main__':
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = wxListCtrlTestFrame(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()