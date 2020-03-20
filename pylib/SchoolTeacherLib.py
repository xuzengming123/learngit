import requests
from cfg import g_vcode
from pprint import pprint
from robot.libraries.BuiltIn import BuiltIn

class  SchoolTeacherLib:
    URL = "http://ci.ytesting.com/api/3school/teachers"

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self.vcode = g_vcode

    def set_vcode(self,vcode):
        self.vcode = vcode


    def list_teacher_list(self,subjectid=None):
        #列出老师
        params = {
            'vcode': self.vcode,
            'action': 'search_with_pagenation'
        }
        if subjectid != None:
            params['subjectid'] = subjectid

        response = requests.get(self.URL, params=params)

        bodyDict = response.json()
        pprint(bodyDict, indent=2)
        return bodyDict



    def add_teacher_list(self,username,realname,subjectid,classlist,phonenumber,email,idcardnumber,idSaveName=None):
        #添加老师
        params = {
            'vcode':self.vcode,
            'action':'add',
            'username':username,
            'realname':realname,
            'subjectid':int(subjectid),
            'classlist':classlist,
            'phonenumber':phonenumber,
            'email':email,
            'idcardnumber':idcardnumber
        }
        response = requests.post(self.URL,data=params)

        bodyDict = response.json()
        pprint(bodyDict, indent=2)

        if idSaveName:
            BuiltIn().set_global_variable('${%s}'%idSaveName, bodyDict['id'])
        return bodyDict


    def modify_school_teacher(self,teacherid,realname,subjectid,classlist,phonenumber,email,idcardnumber):
        #修改老师
        payload = {
            'vcode'  : self.vcode,
            'action':'modify',
            'realname':realname,
            'subjectid':int(subjectid),
            'classlist':classlist,
            'phonenumber':phonenumber,
            'email':email,
            'idcardnumber':idcardnumber
        }

        url = '{}/{}'.format(self.URL,teacherid)
        response = requests.put(url,data=payload)
        bodyDict = response.json()
        pprint (bodyDict,indent=2)
        return bodyDict

    def delete_school_class(self,teacherid):
        #删除老师
        payload = {
            'vcode'  : self.vcode,
        }

        url = '{}/{}'.format(self.URL,teacherid)
        response = requests.delete(url,data=payload)

        bodyDict = response.json()
        pprint (bodyDict,indent=2)
        return bodyDict

if __name__ == '__main__':
    stc = SchoolTeacherLib()

    res = stc.add_teacher_list('lishiming','李世民',1,[{"id":230},{"id":231}],13451813456,'jcysdf@123.com',3209251983090987899)
    trd = stc.add_teacher_list('lishiming','李世民',1,[{"id":230},{"id":231}],13451813456,'jcysdf@123.com',3209251983090987899)
    ret = stc.list_teacher_list()
