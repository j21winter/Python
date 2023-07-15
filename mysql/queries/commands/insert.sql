-- see all tweets in tweets database and edit directly in the result grid.
select * from tweets;


-- insert a tweet into the tweets database using a query
insert into tweets (tweet, user_id, created_at, updated_at)
values ('hello', 1, now(), now());

-- check to see if the tweet made it to the database.
select * from tweets;

