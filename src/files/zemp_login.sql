CREATE TABLE zemp_login(emp_id BIGINT REFERENCES employee(emp_id),dept_id VARCHAR(20) REFERENCES department(dept_id),branch_id VARCHAR(20) REFERENCES branch_location(branch_id),project_id VARCHAR(20) REFERENCES project(project_id),intime DATETIME,outtime DATETIME);