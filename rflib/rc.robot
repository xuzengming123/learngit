*** Settings ***
Library  Collections
Library  SeleniumLibrary
Variables  cfg.py

*** Keywords ***
Setup WebTest
    Open Browser   http://localhost   chrome
    Set Selenium Implicit Wait  10

Teardown WebTest
    Close Browser

#登录
Login Web Site
    #访问某个网址(前提是已经打开过浏览器），所以用例集中的初始化要先打开浏览器。
    go to  http://localhost/mgr/login/login.html
    input text   id=username   &{adminuser}[name]
    input text   id=password   &{adminuser}[pw]
    click element   tag=button

#删除所有课程
DeleteAllCourse
    click element    css=ul.nav a[href*=course]
    sleep   1

    set selenium implicit wait  3
    :For  ${one}  IN RANGE   99
        \  sleep  1
        \  ${html}=   get webelement   tag=html
        \  ${eles}=   evaluate  $html.find_element_by_css_selector("button[ng-click^='delOne(one)']")

        \  EXIT FOR LOOP IF  $eles==[]
        \  click element    @{eles}[0]
        \  click element    css=button.btn-primary
    set selenium implicit wait  5


#课程管理
Add Course
    [Arguments]  ${name}    ${desc}   ${display_idx}
    click element  css=ul.nav a[href*=course]
    sleep  1
    click element   css=button[ng-click^=showAddOne]

    input text      css=input[ng-model='addData.name']    ${name}
    input text      css=textarea[ng-model="addData.desc"]       ${desc}
    input text      css=input[ng-model="addData.display_idx"]   ${display_idx}

    click element    css=button[ng-click^=addOne]

    sleep  1


#获取课程名称
Get Course List
    click element   css=ul.nav a[href*=course]
    sleep  1
    ${lessons}=  create list
    ${eles}=   get webelements  css=tr>td:nth-child(2)

    :For  ${ele}   IN   @{eles}
        \  log to console   ${ele.text}
        \  append to list  ${lessons}  ${ele.text}
    [Return]  ${lessons}


#删除所有老师
DeleteAllTeacher
    click element    css=ul.nav a[href*=teacher]
    sleep   1

    set selenium implicit wait  3
    :For  ${one}  IN RANGE   99
        \  sleep  1
        \  ${html}=   get webelement   tag=html
        \  ${eles}=   evaluate  $html.find_element_by_css_selector("button[ng-click^='delOne(one)']")

        \  EXIT FOR LOOP IF  $eles==[]
        \  click element    @{eles}[0]
        \  click element    css=button.btn-primary
    set selenium implicit wait  5



#老师管理
Add Teacher
    [Arguments]  ${realname}   ${username}   ${desc}  ${display_idx}  ${lesson}
    click element     css=ul.nav a[href*=teacher]
    sleep  1

    click element     css=button[ng-click="showAddOne=true"]

    input text   css=input[ng-model="addEditData.realname"]     ${realname}
    input text   css=input[ng-model="addEditData.username"]     ${username}
    input text   css=textarea[ng-model="addEditData.desc"]     ${desc}
    input text   css=input[ng-model="addEditData.display_idx"]     ${display_idx}

    Select From List By Label  css=select[ng-model*="courseSelected"]     ${lesson}     #下拉框选中课程
    click element   css=button[ng-click*="addTeachCourse()"]      #点击加号

    click element   css=button[ng-click="addOne()"]
    sleep  1


#获取老师名称
Get Teacher List
    click element    css=ul.nav a[href*=teacher]
    sleep  1
    ${teachers}=  create list
    ${eles}=   get webelements   css=tr>td:nth-child(2)
    :FOR  ${ele}  in   @{eles}
        \       log to console   ${ele.text}
        \       append to list   ${teachers}   @{ele.text}
    [return]   ${teachers}
