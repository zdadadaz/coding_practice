-- very slow 8%
select Email
from Person
group by Email
having count(*)>1

-- faster 64%
select distinct a.Email as Email
from Person a, Person b
where a.Email = b.Email and a.Id <> b.Id