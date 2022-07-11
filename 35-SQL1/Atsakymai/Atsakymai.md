1. Select employees first name, last name, job_id and salary whose first name starts with alphabet S

```sql
select first_name,
        last_name,
        job_id,
        salary
 from employees
 where upper(first_name) like 'S%';
```

2. Write a query to select employee with the highest salary

```
select employee_id,
        first_name,
        last_name,
        job_id,
        salary
 from employees
 where salary = (select max(salary) from employees);
```
3. Select employee with the second highest salary

```
select employee_id,
         first_name,
         last_name,
         job_id,
         salary
  from employees
  where salary != (select max(salary) from employees)
  order by salary desc
  limit 1;
  ```
The above query selects only one person with the second-highest salary. But what if there are more than 1 person with the same salary? Or, what if we want to select the 3rd or 4th highest salary? So, let’s try a generic approach.

4. Fetch employees with 2nd or 3rd highest salary

```
 #change the input for 2nd, 3rd or 4th highest salary
 set @input:=3;
 select employee_id, 
        first_name,
        last_name,
        job_id,
        salary 
 from employees e 
 where @input =(select COUNT(DISTINCT Salary) 
           from employees p 
           where e.Salary<=p.Salary);
```

5. Write a query to select employees and their corresponding managers and their salaries

Now, this is a classic example of SELF JOIN in SQL exercises. Also, I am using the CONCAT function to concatenate the first name and last name of each employee and manager.

```
 select concat(emp.first_name,' ',emp.last_name) employee,
        emp.salary emp_sal,
        concat(mgr.first_name,' ',mgr.last_name) manager,
        mgr.salary mgr_sal
 from employees emp
 join employees mgr on emp.manager_id = mgr.employee_id;
 ```

6. Write a query to show count of employees under each manager in descending order

 ```
 select 
 sup.employee_id employee_id,
     concat(sup.first_name,' ', sup.last_name)manager_name,
     COUNT (sub.employee_id) AS number_of_reportees
 from employees sub 
 join employees sup 
 on sub.manager_id = sup.employee_id
 group by sup.employee_id, sup.first_name, sup.last_name
 order by 3 desc;
 ```

7. Find the count of employees in each department

```
 select dept.department_name,
 count(emp.employee_id) emp_count
 from employees emp
 join departments dept on emp.department_id = dept.department_id
 group by dept.department_name
 order by 2 desc;

```
8. Get the count of employees hired year wise

```
 select year(hire_date) hired_year, count(*) employees_hired_count
 from employees
 group by year(hire_date)
 order by 2 desc;

```

9. Find the salary range of employees

```
 select min(salary) min_sal, 
 max(salary) max_sal,
 round(avg(salary)) avg_sal
 from employees;

```
10. Write a query to divide people into three groups based on their salaries

```
 select concat(first_name,' ',last_name) employee,
 salary,
 case
 when salary >=2000 and salary < 5000 then "low" 
 when salary >=5000 and salary < 10000 then "mid"
 else
 "high"
 end as salary_level
 from employees
 order by 1;

```
11. Select the employees whose first_name contains “an”

```
 select (first_name)
 from employees
 where lower(first_name) like '%an%';

```
12. Select employee first name and the corresponding phone number in the format (_ _ _)-(_ _ _)-(_ _ _ _)

```
 select concat(first_name, ' ', last_name) employee,
 replace(phone_number,'.','-') phone_number
 from employees;

```

13. Find the employees who joined in August, 1994.

```
 select concat(first_name, ' ', last_name) employee,
 hire_date
 from employees
 where year(hire_date) = '1994'
 and month(hire_date) = '08';

```
14. Write an SQL query to display employees who earn more than the average salary in that company

```
 select 
 concat(emp.first_name,last_name) name,
 emp.employee_id, 
 dept.department_name department,
 dept.department_id,
 emp.salary
 from departments dept
 JOIN employees emp on dept.department_id = emp.department_id
 where emp.salary > (select avg(salary) from employees)
 order by dept.department_id;

```
15. Find the maximum salary from each department.

```
 select 
 dept.department_id,
 dept.department_name department,
 max(emp.salary)maximum_salary
 from departments dept
 JOIN employees emp on dept.department_id = emp.department_id
 group by dept.department_name,
 dept.department_id
 order by dept.department_id ;

```

16. Write a SQL query to display the 5 least earning employees

```
 select 
 first_name, last_name, 
 employee_id,
 salary
 from employees
 order by salary
 limit 5;

```
17. Find the employees hired in the 80s

```
select employee_id,
concat(first_name,' ' , last_name) employee,
hire_date
from employees
where year(hire_date) between 1980 and 1989;

```
18. Display the employees first name and the name in reverse order

```
 select lower(first_name) name, 
 lower(reverse(first_name)) name_in_reverse
 from employees;

```
19. Find the employees who joined the company after 15th of the month

```
 select employee_id,
 concat(first_name, ' ' , last_name) employee,
 hire_date
 from employees
 where day(hire_date)> 15;

```

20. Display the managers and the reporting employees who work in different departments

```
 select 
  concat(mgr.first_name,' ',mgr.last_name) manager,
  concat(emp.first_name,' ',emp.last_name) employee,
  mgr.department_id mgr_dept,
  emp.department_id emp_dept
  from employees emp
  join employees mgr on emp.manager_id = mgr.employee_id
  where emp.department_id != mgr.department_id
  order by 1;

```
