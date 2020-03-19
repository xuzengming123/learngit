*** Settings ***
Library   cases/c000002.py  WITH NAME   C000002
Library   cases/c000003.py  WITH NAME   C000003

*** Test Cases ***
添加班级2 - tc00002
    [Setup]     C000002.setup
    C000002.steps
    [Teardown]     C000002.teardown

添加班级3 - tc00003
    [Setup]     C000003.setup
    C000003.steps
    [Teardown]     C000003.teardown