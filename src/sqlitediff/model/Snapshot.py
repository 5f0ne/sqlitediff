import sqlite3

from sqlitediff.sqlite.Command import Command
from sqlitediff.model.Table import Table

class Snapshot():
    def __init__(self, name, path) -> None:
        self.name = name
        self.tables = []
        self.dbHandle = sqlite3.connect(path)
        self.dbCursor = self.dbHandle.cursor()
        self._processTables()
        
    def _processTables(self):
        tables = self.dbCursor.execute(Command.TABLE_NAMES).fetchall()
        for table in tables:
            self._createTable(table[0])

    def _processColumns(self, columns):
        result = []
        for row in columns:
            result.append(row[0])
        return result
    
    def _createTable(self, tableName):
        rows = self.dbCursor.execute(Command.SELECT_ALL.substitute(table=tableName)).fetchall()
        columns = self._processColumns(self.dbCursor.description)

        t = Table(tableName, columns)
        for row in rows:
            t.addRow(row)
        self.tables.append(t)

    def getTablesSet(self):
        result = set()
        for table in self.tables:
            result.add(table.name)
        return result
    
    def getTablesList(self):
        result = []
        for table in self.tables:
            result.append((table.name, table.getNumberOfRows()))
        return result