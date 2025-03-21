*** Settings ***

Library  libraries/DatabaseService.py
Library  Libraries/Helper.py

Resource  variables.robot

*** Keywords ***
Execute DB query
    [Arguments]  ${query}
    [Documentation]  Execute query in destination DB

    ${response} =  Execute Query    ${query}
    Set Test Variable    ${DB_QUERY_RESULT}  ${response}

Should Be Greater Than
    [Arguments]    ${value_1}    ${value_2}
    IF    ${value_1} < ${value_2}
         Fail   The value ${value_1} is not larger than ${value_2}
    END

Is Item is unique
    [Arguments]    ${collection}    ${index}
    ${is_unique} =  Is Element Is Unique    ${collection}    ${index}
    IF    $is_unique == False
        Fail    Element is not unique
    END

