
select Visits.customer_id , count(Visits.visit_id) as count_no_trans
from Visits
left join Transactions t
on Visits.visit_id = t.visit_id
where t.transaction_id is null
group by Visits.customer_id;