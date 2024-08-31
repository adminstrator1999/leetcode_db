Create table If Not Exists Employee (Id int, Salary int)
Truncate table Employee
insert into Employee (id, salary) values ('1', '100')
insert into Employee (id, salary) values ('2', '200')
insert into Employee (id, salary) values ('3', '300')

CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    select distinct(h.salary) from
    (select e.salary, dense_rank() over (order by e.salary desc) as rank from employee as e) as h
    where h.rank = N
  );
END;
$$ LANGUAGE plpgsql;
