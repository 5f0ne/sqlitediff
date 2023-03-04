from sqlitediff.model.Row import Row

class Table():
    def __init__(self, name, columns) -> None:
        self.name = name
        self.columns = columns
        self.rows = []

    def addRow(self, row):
        self.rows.append(Row(row))

    def getNumberOfRows(self):
        return len(self.rows)