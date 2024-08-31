Create table If Not Exists Employee (id int, salary int)
Truncate table Employee
insert into Employee (id, salary) values ('1', '100')
insert into Employee (id, salary) values ('2', '200')
insert into Employee (id, salary) values ('3', '300')

with helper as (
    select salary, dense_rank() over (order by salary desc) as rank
    from employee)

select (select distinct salary as SecondhighestSalary
from helper
where rank = 2) secondhighestsalary

select max(salary) as SecondhighestSalary
from employee
where salary < (select max(salary) from employee)

