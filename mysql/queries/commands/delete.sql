-- delete rows from the result grid --
select * from tweets;

delete from tweets
where id = 14;

select * from tweets;