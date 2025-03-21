# Home task 1 - Robot Framework

# Overview

This project automates testing for the TRN database hosted on a Microsoft SQL Server using Robot Framework and the pyodbc
library. The tests validate data in multiple tables, including counts, existence of specific values, minimum and maximum
values, and data ranges.

# Prerequisites

1. Database Setup
   Ensure you have a database "TRN" hosted on a SQL Server instance. Tests will be run against the following tables:

[hr].[countries]
[hr].[employees]
[hr].[jobs]
Database schema should include the following data:

- Countries, with region_id and country_name.
- Employees, with department_id and salary.
- Jobs, with job_title, min_salary, and max_salary.

2. Database User
   Create a dedicated database user for Robot Framework:

Execute the following SQL script:

    CREATE LOGIN dbo_user WITH PASSWORD = '******';
    CREATE USER dbo_user FOR LOGIN dbo_user;
    ALTER ROLE db_datareader ADD MEMBER dbo_user;
    GRANT CONNECT TO dbo_user;

3. Environment Requirements

Environment requirements located in requirements.txt

4. Generate an HTML Report:

robot --pythonpath . -d logs/  test.robot

# Project Structure

The project files are organized as follows:

📁 robot-framework-tests/

├── 📄 test.robot # Tests for database validation

├── 📄 common_keywords.robot # Common functions for tests execution

├── 📄 variables.robot # Variables in queries

├── 📄 README.md # Documentation (this file)

├── 📄 DatabaseService.py # Database connection module

├── 📄 Helper.py # To check element is unique in the list

# How It Works

The tests connect to the SQL Server database using pyodbc and execute SQL queries. With Robot Framework, the following
validations are performed:

Row counts (aggregates).
Existence of specific values.
Verifications of minimum and maximum values.
Validation of rows filtered by specific conditions.

# Test Cases

Test Case Summary

The following tests are included in the script test.robot:

[hr].[countries]

Test Case 1: Number of Countries by Region ID

Steps:

1. SQL Query:

   SELECT region_id, COUNT(*) as amount FROM [hr].[countries] GROUP BY region_id;

2. Verify that the result is not empty.

Expected Result: There should be at least one country per region.

Test Case 2: Australia Exists as a Country

Steps:

1. SQL Query:

   SELECT COUNT(*) as amount FROM [hr].[countries] WHERE country_name = 'Australia';

2. Verify that the count is equal to 1.

Expected Result: "Australia" exists in the database with no duplicates values presented.

[hr].[employees]

Test Case 3: Minimum Salary in Employees Table

Steps:

1. SQL Query:

   SELECT MIN(salary) AS min_salary FROM [hr].[employees];

2. Verify that the minimum salary is equal to 2500.00.

Expected Result: Minimum salary for employees should be 2500.00.

Test Case 4: Number of Employees in Department 9

Steps:

1. SQL Query:

   SELECT COUNT(*) as amount FROM [hr].[employees] WHERE department_id = 9;

2. Verify that the result equals 3.

Expected Result: Department 9 must have exactly 3 employees.

[hr].[jobs]

Test Case 5: Job titles are unique

Steps:

1. SQL Query:

   SELECT job_title FROM [hr].[jobs];

2. Verify that the result is not empty.

Expected Result: All job titles are presented.

Test Case 6: Job Title with max(Min Salary) 

Steps:

1. SQL Query:

   SELECT * FROM [hr].[jobs] WHERE min_salary >= (SELECT max(min_salary) FROM [hr].[jobs]);

2. Verify that the job title is "President".

Expected Result: The job must be "President". "President" min_salary < max_salary


# Running the Tests

Follow these steps to execute the tests:

1. Navigate to the project folder:

   cd {project_path}

2. Run the tests:

   robot --pythonpath . -d logs/  test.robot

# Output

After the tests complete, reports and logs are saved in logs folder.

Report Files:

1. report.html:
    - Summary of overall test results.
    - Includes passed, failed, and skipped tests.

2. To view the reports:
    - Open the report.html file in a browser.
    - Review the success and failure of each test case.