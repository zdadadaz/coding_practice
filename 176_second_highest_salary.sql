-- # Write your MySQL query statement below
select Max(Salary) as SecondHighestSalary
from Employee
where Salary < (select max(Salary) from Employee)