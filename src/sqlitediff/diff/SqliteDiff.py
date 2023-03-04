from sqlitediff.model.Snapshot import Snapshot
from sqlitediff.sqlite.Command import Command
from sqlitediff.diff.DiffResult import DiffResult

class SqliteDiff():
    def __init__(self, pathBefore, pathAfter) -> None:
        self.beforeSnapshot = Snapshot("before", pathBefore)
        self.afterSnapshot = Snapshot("after", pathAfter)
        self.bTableSet = self.beforeSnapshot.getTablesSet()
        self.aTableSet = self.afterSnapshot.getTablesSet()

    def _getDeletedTables(self):
        t = self.bTableSet.difference(self.aTableSet)
        return list(t)
    
    def _getCreatedTables(self):
        t = self.aTableSet.difference(self.bTableSet)
        return list(t)
    
    def _getDeletedRows(self):
        pass

    def _getUpdatedRows(self):
        pass

    def _getCreatedRows(self):
        pass

    def processTables(self):
        deletedTables = self._getDeletedTables()
        createdTables = self._getCreatedTables()
        beforeTables = self.beforeSnapshot.getTablesList()
        afterTables = self.afterSnapshot.getTablesList()
        result = DiffResult(deletedTables, createdTables, 
                            beforeTables, afterTables)
        return result

    def processRows(self):


        return ()

