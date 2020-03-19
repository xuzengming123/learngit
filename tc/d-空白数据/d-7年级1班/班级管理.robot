*** Settings ***
Library    pylib.SchoolClassLib

*** Test Cases ***
添加班级1 - tc000001
#添加班级
    [Setup]  delete_all_school_classes
    ${ret}=    add school class  1    1班   60
    should be true    $ret['retcode']==0
#列出班级，检查一下
    ${ret1}=  list school class   1
    ${fc}=  evaluate  $ret1['retlist'][0]
    should be true  $fc['id']==$ret['id']
    should be true  $fc['invitecode']==$ret['invitecode']

    [Teardown]  delete_all_school_classes


添加班级2 - tc000002
    ${ret1}=   add school class    1   2班  60
    should be true    $ret1['retcode']==0
#列出班级，检查一下
    ${ret2}=   list school class   1
    ${fc}=   evaluate   $ret2['retlist']
    classlist should contain   ${fc}
    ...   2班   七年级   &{ret1}[invitecode]    60    0    &{ret1}[id]
    [Teardown]  delete_school_class    &{ret1}[id]


添加班级3 - tc000003
#添加之前
    ${before}=   list school class   1
    ${ret1}=   add school class    1   1班  60      #添加同名班级，会失败
    should be true    $ret1['retcode']==1
    should be true    $ret1['reason']=='duplicated class name'

#添加之后
    ${after}=   list school class   1
#对比
    should be true  $before==$after


修改班级1 - tc000051
#添加班级2班
    ${ret2}=    add school class  1    2班   60
    should be true    $ret2['retcode']==0
    ${classid}=   evaluate   $ret2['id']

    ${modifyret}=   modify school class   ${classid}   22班   60
    should be true    $modifyret['retcode']==0
#列出班级，检查一下
    ${ret}=   list school class     1
    ${retlist}=  evaluate   $ret['retlist']

    classlist should contain   ${retlist}
    ...   22班   七年级   &{ret2}[invitecode]    60    0    &{ret2}[id]
   [Teardown]  delete_school_class    &{ret2}[id]

修改班级2 - tc000052
#添加一个新班级
    ${ret}=    add school class  1    2班   60
    should be true    $ret['retcode']==0
    ${classid}=   evaluate   $ret['id']

#修改班级，修改的班级名称和上一步添加的班级名称一样
    ${retbefore}=    list school class  1
    ${modifyret}=   modify school class   ${classid}   1班   60
    should be true    $modifyret['retcode']==1
    should be true    $modifyret['reason']=='duplicated class name'

#列出班级，检查返回的结果和修改     之前的结果是否一致
    ${retafter}=    list school class  1
    should be true   $retbefore==$retafter
    [Teardown]  delete_school_class     ${classid}


修改班级3 - tc000053
    ${modifyret}=   modify school class   99999999   1班   60
    log  ${modifyret}
    should be true    $modifyret['retcode']==404
    should be true    $modifyret['reason']=="id 为`99999999`的班级不存在"


删除班级1 - tc000081
    ${deleteret}=   delete school class   99999999
    should be true    $deleteret['retcode']==404
    should be true    $deleteret['reason']=="id 为`99999999`的班级不存在"

删除班级2 - tc000082
#添加一个新班级
    ${ret}=    add school class  1    2班   60
    should be true    $ret['retcode']==0
    ${classid}=   evaluate   $ret['id']

#列出班级
    ${retbefore}=    list school class  1
    classlist should contain   &{retbefore}[retlist]
    ...     2班  七年级   &{ret}[invitecode]    60   0   &{ret}[id]
#删除班级，删除的id和上一步添加的班级id一样
    ${deleteret}=   delete school class   ${classid}
    should be true    $deleteret['retcode']==0

#列出班级，检查返回的结果和修改     之前的结果是否一致
    ${retafter}=    list school class  1

    classlist should contain   &{retafter}[retlist]
    ...     2班  七年级   &{ret}[invitecode]
    ...     60   0   &{ret}[id]   0