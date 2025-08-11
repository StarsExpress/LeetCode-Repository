WITH DistinctDeptSalary AS (
    SELECT DISTINCT salary, departmentId FROM Employee
),
RankedDeptSalary AS (
    SELECT *,
    ROW_NUMBER() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS salary_rank
    FROM DistinctDeptSalary
),
DeptTopSalary As (
    SELECT departmentId, Department.name As department, salary FROM RankedDeptSalary
    LEFT JOIN Department ON departmentId = Department.id
    WHERE salary_rank <= 3  -- Only keep top 3 for each department.
)
SELECT department, name AS employee, Employee.salary AS salary FROM Employee
INNER JOIN DeptTopSalary
ON Employee.departmentId = DeptTopSalary.departmentId
AND Employee.salary = DeptTopSalary.salary