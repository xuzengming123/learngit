#coding=utf-8
import sys
sys.path.append('E:\import_selenium')
from src.until.excel_until import ExcelUntil
from keywords.actionMethod import ActionMethod
class KeywordCasse:
    def run_main(self):
        self.action_method = ActionMethod()
        handle_excel = ExcelUntil('E:\import_selenium\config\keyword.xlsx')
        case_lines = handle_excel.get_lines()
        if case_lines != None:
            for i in range(1,case_lines):
                is_run = handle_excel.get_col_value(i,4)
                if is_run == 'yes':
                    #执行方法
                    method = handle_excel.get_col_value(i,5)
                    #输入的数据
                    send_value = handle_excel.get_col_value(i,6)
                    #操作元素
                    handle_value = handle_excel.get_col_value(i,7)
                    # if send_value:
                    self.run_method(method,send_value,handle_value)
                #执行方法（输入数据，操作元素）
            #没有输入数据
                #执行方法（操作元素）
    def run_method(self,method,send_value,handle_value):

        method_value = getattr(self.action_method, method)
        if send_value:
            method_value(send_value,handle_value)
        else:
            method_value(handle_value)

if __name__ == '__main__':
    ex = KeywordCasse()
    ex.run_main()