'''
Created on Aug 7, 2012

@author: moz
'''

from wx import ListCtrl
import sys
import wx

class ListCtrlDb(ListCtrl):
    '''
    This class is a wx.listctrl class with the addition of sql connectivity
    
    The idea is to have a simple way of shoing data from the data base.
    The listctrl is initialized with the columns from the cursor object.
    
    Inserting and updating is implemented using wx.CallAfter to resolve the 
    issue of Sqlite only what to be called by the thread that created the instance
    and wxython gives funny X errors when widgets are updated from other threads.
    
    In summary, this class is usable if you have a thread and want to give it a 
    visitor for callbacks to enable GUI updates initiated by the thread
    '''
        
    def InitFromDb( self, Cursor ):
        ''' init the listctrl with appropriate columns. No rows are added 
        @param Cursor: the database cursor to use
        '''
        
        # set header stuff
        col_name_list = [desc[0] for desc in Cursor.description]
        
        wx.CallAfter(self._DeferredInit, col_name_list)
    
    def _DeferredInit(self, col_name_list ):
        ''' Does the actual init of the listctrl. Called from the GUI thread
        @param col_name_list: the list of column names to use in the listctrl
        '''
        # remove any existing columns.
        self.DeleteAllColumns()
        self.DeleteAllItems()

        # add new ones
        colcount = 0
        for col_name in col_name_list:
            self.InsertColumn(colcount, col_name)
            colcount += 1
    
    def InsertFromDb( self, Cursor ):
        ''' Inserts data from the cursor as rows int the listctrl
        @param Cursor: the database cursor to use
        '''
        
        # adding rows
        Rows = []
        for row in Cursor:
            
            #converting all entries to string
            strrow = []            
            for i in range(0, len(Cursor.description)):
                strrow.append( str( row[i] ) )
                
            Rows.append( strrow )
        
        wx.CallAfter(self._DeferredInsert, Rows)
         
        
    def _DeferredInsert(self, Rows ):
        ''' Does the actual inserting into the listctrl. Called from the GUI thread
        @param Rows: Rows to insert all converted to text.
        '''
        for strrow in Rows:
            index = self.InsertStringItem(sys.maxint, strrow[0] )
            for i in range(1, len(strrow)-1):
                self.SetStringItem( index, i, strrow[i] )
        
    
    def UpdateFromDb( self, Cursor ):
        ''' Updates data in the listctrl from the cursor rows
        @param Cursor: the database cursor to use
        '''
        
        Rows = []
        # adding rows
        for row in Cursor:
            print "row[0]: %s"%row[0]
    
            #converting all entries to string
            strrow = []
            for i in range(0, self.GetColumnCount()):
                strrow.append( str( row[i] ) )
            Rows.append( strrow )
             
        wx.CallAfter(self._DeferredUpdate, Rows)               
                        
    def _DeferredUpdate(self, Rows):
        ''' Does the actual update of the listctrl. Called from the GUI thread
        @param Rows: new rowdata. First item in each row is used as primkey
        '''
        for strrow in Rows:
            # using row0 as identifier
            index = self.FindItem(-1, strrow[0])
            for i in range(1, self.GetColumnCount()):
                self.SetStringItem( index, i, strrow[i] )

