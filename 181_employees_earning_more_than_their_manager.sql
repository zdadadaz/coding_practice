-- mine
select Name as Employee from Employee E where ManagerId in
(select Id from Employee where E.Salary > Salary)

-- join condition (worse)
select a.Name as Employee from Employee a, Employee b 
where a.ManagerId=b.Id and a.Salary > b.Salary