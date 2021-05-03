
select w1.id as id
from Weather w1
where exists
(
select w2.id
from Weather w2
where DATEDIFF(w1.recordDate,w2.recordDate)=1 and w1.Temperature > w2.Temperature
)