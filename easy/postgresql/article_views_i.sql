Create table If Not Exists Views (article_id int, author_id int, viewer_id int, view_date date)
Truncate table Views
insert into Views (article_id, author_id, viewer_id, view_date) values ('1', '3', '5', '2019-08-01')
insert into Views (article_id, author_id, viewer_id, view_date) values ('1', '3', '6', '2019-08-02')
insert into Views (article_id, author_id, viewer_id, view_date) values ('2', '7', '7', '2019-08-01')
insert into Views (article_id, author_id, viewer_id, view_date) values ('2', '7', '6', '2019-08-02')
insert into Views (article_id, author_id, viewer_id, view_date) values ('4', '7', '1', '2019-07-22')
insert into Views (article_id, author_id, viewer_id, view_date) values ('3', '4', '4', '2019-07-21')
insert into Views (article_id, author_id, viewer_id, view_date) values ('3', '4', '4', '2019-07-21')

--select distinct(viewer_id) as id
--from Views
--where author_id = viewer_id
--order by viewer_id

-- Select 'viewer_id' as 'id' from the 'Views' table
SELECT viewer_id AS id
FROM Views
-- Filter records where 'author_id' is equal to 'viewer_id'
WHERE author_id = viewer_id
-- Group by 'viewer_id' and 'author_id' to aggregate results
GROUP BY viewer_id, author_id
-- Sort the results by 'viewer_id' in ascending order
ORDER BY viewer_id;