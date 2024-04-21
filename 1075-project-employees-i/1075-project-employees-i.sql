select p.project_id, ifnull(round(sum(experience_years)/count(experience_years),2),0) as average_years 
from Project p left join Employee e on p.employee_id = e.employee_id group by project_id