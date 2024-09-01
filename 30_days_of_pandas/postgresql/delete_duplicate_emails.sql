Create table If Not Exists Person (Id int, Email varchar(255))
Truncate table Person
insert into Person (id, email) values ('1', 'john@example.com')
insert into Person (id, email) values ('2', 'bob@example.com')
insert into Person (id, email) values ('3', 'john@example.com')

delete from person p1
using person p2
where p1.email = p2.email and p1.id > p2.id

delete from Person
where id not in (
    select min(id)
    from Person
    group by email
)