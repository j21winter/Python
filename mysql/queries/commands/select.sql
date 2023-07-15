-- select everything from a table 
select * from users;

-- select two columns from the users table
select first_name, last_name from users;

-- select 2 columns from users and name the colums
select first_name as first,last_name as hello from users;

-- select all users from the users table with the id of 1
select * from users 
where id = 1;

-- call birthday in decending order
select * from users
where id = 1 or id=2
order by birthday desc;

-- call birthday in ascending order
select * from users
where id = 1 or id=2
order by birthday asc;

-- birthday will be set in ascending as default
select * from users
where id = 1 or id=2
order by birthday;

-- select first names that end in 'e'
SELECT * FROM users
WHERE first_name LIKE "%e";

-- select first names that dont begin with 'k'
SELECT * 
FROM users
WHERE first_name NOT LIKE "K%";

-- select 3 users with an offset of 2(starting at the 3rd user)
SELECT * FROM users
LIMIT 2,3;





