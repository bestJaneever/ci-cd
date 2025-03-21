*** Settings ***

Library    Collections

Resource  Resources/variables.robot

*** Test Cases ***
# Verify Australia exists without duplicates in [hr.].[countries]
Completness test for countries table
    [Setup]  Execute DB query    ${DB_QUERY_COMPLETENESS_COUNTRIES}
    FOR    ${element}    IN    @{DB_QUERY_RESULT}
            Should Be Greater Than    ${element}[0]    ${EXPECTED_RESULT_COMPLETENESS_COUNTRIES}
            Log    Completness test for countries table passed
    END

# Verify consistency by grouping by region_id
Consisnency test for countries table
    [Setup]  Execute DB query    ${DB_QUERY_CONSISTENCY_COUNTRIES}
    FOR    ${element}    IN    @{DB_QUERY_RESULT}
        Dictionary Should Contain Key    ${EXPECTED_RESULT_CONSISTENCY_COUNTRIES}    ${element}[0]
        Should Be Equal    ${element}[1]    ${EXPECTED_RESULT_CONSISTENCY_COUNTRIES}[${element}[0]]
    END

# Verify min_salary in [hr].[employees]
Accuracy test for employee table
    [Setup]  Execute DB query    ${DB_QEURY_ACCURACY_EMPLOYEES}
    FOR    ${element}    IN    @{DB_QUERY_RESULT}
        Should Be Greater Than    ${element}[0]    ${EXPECTED_RESULT_ACCURACY_EMPLOYEES}

    END

# Verify employees amount for department 9 in [hr].[employees]
Integrity test for employee table
    [Setup]  Execute DB query    ${DB_QUERY_INTEGRITY_EMPLOYEES}
    Should Be Equal As Integers    ${DB_QUERY_RESULT}[0][0]    ${EXPECTED_RESULT_INTEGRITY_EMPLOYEES}

# Verify unique job titles
Uniqueness test for job table
    [Setup]  Execute DB query    ${DB_QUERY_UNIQUENESS_JOBS}
    FOR    ${index}    ${element}    IN ENUMERATE    @{DB_QUERY_RESULT}
        Is Item is unique    ${DB_QUERY_RESULT}    ${index}
    END
# Verify job title President has min_salary >= max(min_salary) FROM [hr].[jobs]
# Verify President max_salary > min_salary
Accurancy test for job table
    [Setup]  Execute DB query    ${DB_QUERY_ACCURACY_JOBS}
    Should Be Equal    ${DB_QUERY_RESULT}[0][1]    ${EXPECTED_RESULT_ACCURACY_JOBS}
    Should Be Greater Than    ${DB_QUERY_RESULT}[0][3]    ${DB_QUERY_RESULT}[0][2]

# Command to execute tests with result in log file:
# robot --pythonpath . -d logs/  test.robot
