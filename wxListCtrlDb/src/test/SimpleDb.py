'''
Created on Aug 7, 2012

@author: moz
'''
import sqlite3
from sys import stderr
import datetime
import random

class SimpleDb():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''

        print >> stderr, "Simple db constructor. Inits db."
        
        self._InitQuery = '''
                create table Data( 
                        EntryId INTEGER, 
                        AcqTime TIMESTAMP, 
                        SomeInt INTEGER,
                        SomeText TEXT,
                        PRIMARY KEY(EntryId ASC));
        '''
        
        self._conn = sqlite3.connect( ':memory:' )
        self._conn.executescript( self._InitQuery )

    def GetAllData(self):
        print >> stderr, "Retrieve data"

        q = "select * from data"
        cursor = self._conn.execute( q )
        return cursor

    def GetData(self, EntryId ):
        print >> stderr, "Retrieve data entry %d"%EntryId

        q = "select * from data where EntryId = ?"
        cursor = self._conn.execute( q, (EntryId,) )
        return cursor    
       
    def InsertData(self):
        print >> stderr, "Insert data"
        q = "insert into Data (AcqTime, SomeInt, SomeText) values ( ?,?,?)"
        
        AcqTime = datetime.datetime.now()
        SomeInt = random.randint(1, 1000000)
        SomeText = "abc" # yes, really random.
        
        c = self._conn.execute( q, (AcqTime, SomeInt, SomeText) )

        print >> stderr, "Inserted id %d"%c.lastrowid
        return c.lastrowid

    
    def UpdateData(self, EntryId ):
        print >> stderr, "update  entry %d"%EntryId
        q = '''
            UPDATE Data
            SET AcqTime = ?, SomeInt = ?, SomeText = ?
            WHERE EntryId = ?
        '''
        
        AcqTime = datetime.datetime.now()
        SomeInt = random.randint(1, 1000000)
        SomeText = "abc" # yes, really random.
        
        c = self._conn.execute( q, (AcqTime, SomeInt, SomeText, EntryId) )
        return  
    

    

    
    