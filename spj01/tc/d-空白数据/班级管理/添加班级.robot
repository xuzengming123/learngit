#coding-utf8
*** Settings ***
Library    pylib.SchoolClassLib


*** Test Cases ***
addClass1
    ${ret1}=    add school class    1     1班     60
    #retcode=0是否添加成功
    should be true     $ret1['retcode']==0

#列出班级，检验一下
    ${ret2}=    list school class    1
    ${fc}=   evaluate   $ret2['retlist'][0]
    should be true    $fc['id']==$ret1['id']
    should be true    $fc['invitecode']==$ret1['invitecode']

    [Teardown]    delete_school_class   &{ret1}[id]

addClass2
    [Setup]   Run Keywords   delete_all_school_classes
    ...  AND   add school class    1     1班     60

#添加班级
    ${ret1}=    add school class   2     2班     80
#列出班级，检查一下
    ${classlist}=   list school class
    log   ${classlist}
    ${fc}=    evaluate   $classlist['retlist'][1]
    log    ${fc}
    should be true    $fc['id']==$ret1['id']
    should be true    $fc['invitecode']==$ret1['invitecode']

    [Teardown]    delete_all_school_classes

addClass3
    [Setup]  Run Keywords   delete_all_school_classes
    ...  AND   add school class    1     1班     60

    ${ret}=   add school class    1     1班     60
    should be true    $ret['retcode']==1