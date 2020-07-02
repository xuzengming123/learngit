import xlrd
from xlutils.copy import copy

class ExcelUntil:
    '''读取xls文件'''
    def __init__(self,excel_path=None,index=None):
        '''

        :param excel_path: 文件路径
        :param index: 文件sheets的位置
        '''
        if excel_path is None:
            excel_path = 'E:\import_selenium\config\casedata.xlsx'
        if index is None:
            index = 0
        #打开XLS文件，返回数据对象
        self.data = xlrd.open_workbook(excel_path)
        #打开列表，index=0，返回表格sheet
        self.table = self.data.sheets()[index]

    #[[],[]]
    #获取Excel数据，按照每行一个list，添加到一个大的list里面
    def get_data(self):
        result = []
        rows = self.get_lines()
        if rows != None:
            for i in range(rows):
            #循环次数为表格行数
                col = self.table.row_values(i)
                #获取每一行的数据
                result.append(col)
            return result
        return None

    #获取行数
    def get_lines(self):
        #获取表格行数
        rows = self.table.nrows
        if rows >= 1:
            return rows
        return None

    def get_col_value(self,row,col):
        '''
        获取单元格的数据
        :param row: 行
        :param col: 列
        :return: 单元格的数据
        '''
        if self.get_lines()>row:
            data = self.table.cell(row,col-1).value
            return data
        return None

    def write_value(self,row,col,value):
        '''
        写入数据
        :param row:行
        :param col:列
        :param value:写入的值
        :return:
        '''
        read_value = self.data
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row,col,value)
        write_data.save('E:\import_selenium\config\keyword.xlsx')

if __name__ == '__main__':
    ex = ExcelUntil('E:\import_selenium\config\keyword.xlsx')
    print(ex.get_col_value(1,5))
    # ex.write_value(20,10,'test')