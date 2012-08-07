'''
Created on Aug 7, 2012

@author: moz
'''

from wx import ListCtrl
import sys
import wx

class ListCtrlDb(ListCtrl):
    '''
    classdocs
    '''
        
    def InitFromDb( self, Cursor ):
        ''' init the listctrl with appropriate columns. No rows are added '''
        # remove any existing columns.
        self.DeleteAllColumns()
        self.DeleteAllItems()
        
        # set header stuff
        col_name_list = [desc[0] for desc in Cursor.description]
        
        wx.CallAfter(self._DeferredInit, col_name_list)
            
#        colcount = 0
#        for col_name in col_name_list:
#            print >> sys.stderr, "Adding column %s"%col_name
#            self.InsertColumn(colcount, col_name)
#            colcount += 1
    
    def _DeferredInit(self, col_name_list ):
        print >> sys.stderr, "Deferred init"
        colcount = 0
        for col_name in col_name_list:
            print >> sys.stderr, "Adding column %s"%col_name
            self.InsertColumn(colcount, col_name)
            colcount += 1
    
    def InsertFromDb( self, Cursor ):
        print "inserting %d new entries"%Cursor.rowcount
        
        # adding rows
        Rows = []
        for row in Cursor:
            print "row[0]: %s"%row[0]
            
            #converting all entries to string
            strrow = []
#            print "column count %d"%self.GetColumnCount()
#            for i in range(0, self.GetColumnCount()):
#                strrow.append( str( row[i] ) )
                    
            
            print "column count %d"%len(Cursor.description)
            for i in range(0, len(Cursor.description)):
                strrow.append( str( row[i] ) )
                
            Rows.append( strrow )
        
        wx.CallAfter(self._DeferredInsert, Rows)
         
#            index = self.InsertStringItem(sys.maxint, strrow[0] )
#            for i in range(1, self.GetColumnCount()):
#                self.SetStringItem( index, i, strrow[i] )
        
    def _DeferredInsert(self, Rows ):
        print >> sys.stderr, "Deferred insert"
        for strrow in Rows:
            index = self.InsertStringItem(sys.maxint, strrow[0] )
            for i in range(1, len(strrow)-1):
                self.SetStringItem( index, i, strrow[i] )
        
    
    def UpdateFromDb( self, Cursor ):
        # fixme: Row[0] must be primkey, make it variable
        print "Updating %d new entries"%Cursor.rowcount
        
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
        
#            # using row0 as identifier
#            index = self.FindItem(-1, strrow[0])
#            for i in range(1, self.GetColumnCount()):
#                self.SetStringItem( index, i, strrow[i] )
                
    def _DeferredUpdate(self, Rows):
        print >> sys.stderr, "Deferred update"
        
        for strrow in Rows:
            # using row0 as identifier
            index = self.FindItem(-1, strrow[0])
            for i in range(1, self.GetColumnCount()):
                self.SetStringItem( index, i, strrow[i] )

