----1.List the following details of each employee: employee number, last name, first name, gender, and salary.

select employee.emp_no, employee.last_name, employee.first_name, employee.gender,salaries.salary
from employee
join salaries
on  employee.emp_no=salaries.emp_no;

---2. List employees who were hired in 1986.

select emp_no, last_name, first_name,hire_date
from employee
where EXTRACT (YEAR FROM hire_date)=1986;

---3.List the manager of each department with the following information: department number, 
---department name, the manager's employee number, last name, first name, and start and end employment dates.
select distinct title 
from titles

select *
from titles
where title='Manager';

select * 
from dept_manager;

select departments.dept_name,dept_manager.emp_no,employee.last_name, employee.first_name, employee,dept_manager.from_date,dept_manager.to_date
from dept_manager 
join departments
using  (dept_no)
join employee 
using  (emp_no);

----4-List the department of each employee with the following information: employee number, last name, first name, and department name.
select department_employess.emp_no,employee.last_name, employee.first_name,departments.dept_name
from department_employess
join departments
using (dept_no)
join employee
using (emp_no);

----5.List all employees whose first name is "Hercules" and last names begin with "B."
select emp_no, last_name, first_name
from employee
where first_name='Hercules' and last_name like 'B%';

---6.List all employees in the Sales department, including their employee number, last name, first name, and department name.
select department_employess.emp_no,employee.last_name, employee.first_name,departments.dept_name,department_employess.to_date
from department_employess
join departments
using (dept_no)
join employee
using (emp_no)
where departments.dept_name='Sales' and department_employess.to_date>now();
---where departments.dept_name='Sales' ;

---7.List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
select department_employess.emp_no,employee.last_name, employee.first_name,departments.dept_name,department_employess.to_date
from department_employess
join departments
using (dept_no)
join employee
using (emp_no)
where (departments.dept_name='Sales'  or departments.dept_name='Development') and department_employess.to_date>now();
--- I filter just current employees

--8--.In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
select last_name,count(last_name)
from employee
group by last_name
order by count(last_name) desc;

--- You look down at your badge to see that your employee ID number is 499942.
select employee.emp_no, employee.last_name, employee.first_name, employee.gender,salaries.salary
from employee
join salaries
on  employee.emp_no=salaries.emp_no
where employee.emp_no=499942;





