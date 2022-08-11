# https://www.hackerrank.com/challenges/the-company/problem?isFullScreen=true
select c.company_code, c.founder, sub.lead, sub.senior, sub.manager, sub.employee
from company c
join (select company_code,
      count(distinct lead_manager_code) lead,
            count(distinct senior_manager_code) senior,
            count(distinct manager_code) manager,
            count(distinct employee_code) employee
    from Employee
    group by company_code) sub
    on c.company_code = sub.company_code
order by c.company_code ASC;
