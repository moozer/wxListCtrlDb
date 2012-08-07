'''
Created on Jul 23, 2012

@author: moz
'''
import sys

def InitListCtrl( Cursor, ListCtrl ):
    ''' init the listctrl with appropriate columns. No rows are added '''
    # remove any existing columns.
    ListCtrl.DeleteAllColumns()
    ListCtrl.DeleteAllItems()
    
    # set header stuff
    col_name_list = [desc[0] for desc in Cursor.description]
    
    colcount = 0
    for col_name in col_name_list:
        print "Adding column %s"%col_name
        ListCtrl.InsertColumn(colcount, col_name)
        colcount += 1
        
#    # adding rows
#    for row in Cursor:
#        print "row[0]: %s"%row[0]
#        index = ListCtrl.InsertStringItem(sys.maxint, row[0])
#        for i in range(1, ListCtrl.GetColumnCount()-1):
#            ListCtrl.SetStringItem( index, i, str( row[i] ) )
    
def ListCtrlInsert( Cursor, ListCtrl ):
    print "inserting %d new entries"%Cursor.rowcount
    
    # adding rows
    for row in Cursor:
        print "row[0]: %s"%row[0]
        
        #converting all entries to string
        strrow = []
        for i in range(0, ListCtrl.GetColumnCount()):
            strrow.append( str( row[i] ) )
                
        index = ListCtrl.InsertStringItem(sys.maxint, strrow[0] )
        for i in range(1, ListCtrl.GetColumnCount()):
            ListCtrl.SetStringItem( index, i, strrow[i] )
    
def ListCtrlUpdate( Cursor, ListCtrl ):
    # fixme: Row[0] must be primkey, make it variable
    print "Updating %d new entries"%Cursor.rowcount
    
    # adding rows
    for row in Cursor:
        print "row[0]: %s"%row[0]

        #converting all entries to string
        strrow = []
        for i in range(0, ListCtrl.GetColumnCount()):
            strrow.append( str( row[i] ) )
            
        # using row0 as identifier
        index = ListCtrl.FindItem(-1, strrow[0])
        for i in range(1, ListCtrl.GetColumnCount()):
            ListCtrl.SetStringItem( index, i, strrow[i] )
    
