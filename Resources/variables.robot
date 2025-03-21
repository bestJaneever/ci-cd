*** Settings ***

Library  String
Library  OperatingSystem
Library  OperatingSystem
Library  pyodbc

Resource  ./common_keywords.robot

*** Variables ***

${DB_QUERY_COMPLETENESS_COUNTRIES}          SELECT COUNT(*) as amount FROM [hr].[countries] WHERE country_name = 'Australia';
${DB_QUERY_CONSISTENCY_COUNTRIES}           SELECT region_id, COUNT(*) as amount FROM [hr].[countries] GROUP BY region_id;
${DB_QEURY_ACCURACY_EMPLOYEES}              SELECT MIN(salary) AS min_salary FROM [hr].[employees];
${DB_QUERY_INTEGRITY_EMPLOYEES}             SELECT COUNT(*) as emp_amount FROM [hr].[employees] WHERE department_id = 9;
${DB_QUERY_UNIQUENESS_JOBS}                 SELECT job_title FROM [hr].[jobs];
${DB_QUERY_ACCURACY_JOBS}                   SELECT * FROM [hr].[jobs] WHERE min_salary >= (SELECT max(min_salary) FROM [hr].[jobs]);

${EXPECTED_RESULT_COMPLETENESS_COUNTRIES}   1
${EXPECTED_RESULT_CONSISTENCY_COUNTRIES}    ${{ {1: 8, 2: 5, 3: 6, 4: 6} }}
${EXPECTED_RESULT_ACCURACY_EMPLOYEES}       2500
${EXPECTED_RESULT_INTEGRITY_EMPLOYEES}      3
${EXPECTED_RESULT_ACCURACY_JOBS}            President
