from openpyxl import load_workbook, Workbook
import os

class Writer():
    def __init__(self, filename):
        self.filename = filename[0]

    def write(self, data): pass

    def save(self): pass

class ExcelWriter(Writer):
    def __init__(self, filename):
        super(ExcelWriter, self).__init__(filename)
        self.workbook = Workbook()
        self.row = 1

    def write(self, data):
        sheet = self.workbook.active
        sheet.title = "Sheet1"
        excel_column_index = list(range(2, len(data) + 2))
        goods = list(zip(excel_column_index, data))
        for index, goods_key in goods:
            sheet.cell(self.row, index).value = data[goods_key]
        self.row += 1

    def save(self):
        self.workbook.save(self.filename)

class TxtWriter(Writer):
    def __init__(self, filename):
        super(TxtWriter, self).__init__(filename)

    def write(self, data): pass

    def save(self): pass

class Sendter(Writer):
    def __init__(self, self_email):pass

    def write(self,data):pass

    def send(self, targer_email):pass



WRITER_CLASS = {
    ".txt" : TxtWriter.__name__,
    ".xlsx" : ExcelWriter.__name__
}
