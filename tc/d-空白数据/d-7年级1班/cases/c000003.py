from pylib.SchoolClassLib import SchoolClassLib
sc = SchoolClassLib()

class c000003:
    def steps(self):
        print('''\n\n***** step 1 ***** 列出班级，检查一下 \n''')
        ret = sc.list_school_class(1)

        print('''\n\n***** step 2 ***** 添加 7年级1班 \n''')
        self.ret1 = sc.add_school_class(1,'1班',60)
        assert self.ret1['retcode'] == 1,  '返回值非1'
        assert self.ret1['reason'] == 'duplicated class name', '错误码不对'

        print('''\n\n***** step 3 ***** 列出班级，检查一下 \n''')
        ret2 = sc.list_school_class(1)
        assert ret == ret2, '添加班级后，数据不一致'

    def setup(self):
        pass

    def teardown(self):
        pass