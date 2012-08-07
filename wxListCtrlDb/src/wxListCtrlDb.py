'''
Created on Aug 7, 2012

@author: moz
'''

from wx import ListCtrl
import sys

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
        
        colcount = 0
        for col_name in col_name_list:
            print "Adding column %s"%col_name
            self.InsertColumn(colcount, col_name)
            colcount += 1
    
        
    def InsertFromDb( self, Cursor ):
        print "inserting %d new entries"%Cursor.rowcount
        
        # adding rows
        for row in Cursor:
            print "row[0]: %s"%row[0]
            
            #converting all entries to string
            strrow = []
            for i in range(0, self.GetColumnCount()):
                strrow.append( str( row[i] ) )
                    
            index = self.InsertStringItem(sys.maxint, strrow[0] )
            for i in range(1, self.GetColumnCount()):
                self.SetStringItem( index, i, strrow[i] )
        
    def UpdateFromDb( self, Cursor ):
        # fixme: Row[0] must be primkey, make it variable
        print "Updating %d new entries"%Cursor.rowcount
        
        # adding rows
        for row in Cursor:
            print "row[0]: %s"%row[0]
    
            #converting all entries to string
            strrow = []
            for i in range(0, self.GetColumnCount()):
                strrow.append( str( row[i] ) )
                
            # using row0 as identifier
            index = self.FindItem(-1, strrow[0])
            for i in range(1, self.GetColumnCount()):
                self.SetStringItem( index, i, strrow[i] )
                
