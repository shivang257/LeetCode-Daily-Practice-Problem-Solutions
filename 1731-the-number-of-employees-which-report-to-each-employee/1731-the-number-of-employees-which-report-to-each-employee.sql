select mgr.employee_id, mgr.name, count(emp.reports_to) as reports_count, round(avg(emp.age)) as average_age 
from Employees emp join employees mgr
on emp.reports_to = mgr.employee_id
group by employee_id 
order by employee_id