import dbService as db
import queries

# Verify Australia exists without duplicates in [hr.].[countries]
def test_completeness_hr_countries():
    expected_min_count = 1
    query_result = run_query(queries.completeness_hr_countries_query)
    assert query_result["amount"].values[0] >= expected_min_count

# Verify min_salary in [hr].[employees]
def test_accuracy_min_salary():
    expected_min_salary = 2500
    query_result = run_query(queries.accuracy_min_salary_query)
    assert query_result["min_salary"].values[0] == expected_min_salary

# Verify employees amount for department 9 in [hr].[employees]
def test_integrity_emp_count_for_dep_9():
    expected_count = 3
    query_result = run_query(queries.integrity_emp_count_for_dep_9_query)
    assert query_result["emp_amount"].values[0] == expected_count

# Verify consistency by grouping by region_id
def test_consistency_by_grouping_by_region_id():
    expected_result = {1: 8, 2: 5, 3: 6, 4: 6}
    query_result = run_query(queries.consistency_by_grouping_by_region_id_query)
    for index, row in query_result.iterrows():
        assert row["region_id"] in expected_result
        assert row["amount"] == expected_result[row["region_id"]]

# Verify unique job titles
def test_uniqueness_by_job_title():
    query_result = run_query(queries.uniqueness_by_job_title_query)
    assert len(query_result["job_title"].unique()) == len(query_result["job_title"])

# Verify job title President has min_salary >= max(min_salary) FROM [hr].[jobs]
# Verify President max_salary > min_salary
def test_accuracy_for_salary():
    expected_job_title = 'President'
    query_result = run_query(queries.accuracy_for_salary_query)
    assert query_result["max_salary"].values[0] > query_result["min_salary"].values[0]
    assert query_result["job_title"].values[0] == expected_job_title


def run_query(query):
    db_service = db.dbService()
    return db_service.execute_query(query)
