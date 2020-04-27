#coding:utf-8
import configparser
class ReadIni():
    def __init__(self,file_name=None,node=None):
        if file_name == None:
            file_name = "E:\import_selenium\config\localElement.ini"
        if node == None:
            self.node = 'RegisterElement'  #配置文件的某个节点信息
        else:
            self.node = node
        self.cf = self.load_ini(file_name)

    def load_ini(self,file_name):
        '''
        加载文件
        :param file_name: 配置文件路径
        :return: 配置文件对象
        '''
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    def get_value(self,key):
        '''
        获取value值
        :param key: 配置文件的key值
        :return: key对应的value值
        '''
        data = self.cf.get(self.node, key)
        return data


if __name__ == '__main__':
    read_ini = ReadIni()
    img_path = read_ini.get_value('img_path_key')
    print(img_path)