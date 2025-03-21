completeness_hr_countries_query = ("SELECT COUNT(*) as amount "
                                   "FROM [hr].[countries] "
                                   "WHERE country_name = 'Australia';")

accuracy_min_salary_query = ("SELECT MIN(salary) AS min_salary "
                             "FROM [hr].[employees];")

integrity_emp_count_for_dep_9_query = ("SELECT COUNT(*) as emp_amount "
                                       "FROM [hr].[employees] "
                                       "WHERE department_id = 9;")

consistency_by_grouping_by_region_id_query = ("SELECT region_id, COUNT(*) as amount "
                                              "FROM [hr].[countries] "
                                              "GROUP BY region_id;")

uniqueness_by_job_title_query = "SELECT job_title FROM [hr].[jobs];"

accuracy_for_salary_query = ("SELECT *  "
                             "FROM [hr].[jobs] "
                             "WHERE min_salary >= (SELECT max(min_salary) FROM [hr].[jobs])")
