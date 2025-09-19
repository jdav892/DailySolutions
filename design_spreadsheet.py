class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows
        self.grid = {}

    def _parse_cell(self, cell: str):
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:]) - 1
        return row, cell

    def setCell(self, cell: str, value: int) -> None:
        row, col = self._parse_cell(cell)
        self.grid[(row, col)] = value


    def resetCell(self, cell: str) -> None:
        row, col = self._parse_cell(cell)
        if (row, col) in self.grid:
            del self.grid[(row, col)]


    def getValue(self, formula: str) -> int:
        formula = formula[1:]
        parts = formula.split('+')

        total = 0
        for part in parts:
            part = part.strip()
            if part.isdigit():
                total += int(part)
            else:
                row, col = self._parse_cell(part)
                total += self.grid.get((row, col), 0)

        return total
# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)