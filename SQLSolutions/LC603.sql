-- Write your PostgreSQL query statement below
-- this is the editorial solution
-- select distinct a.seat_id
-- from cinema a cross join cinema b 
-- where abs(a.seat_id - b.seat_id) = 1 and a.free = 1 and b.free = 1
-- order by a.seat_id

-- below is a faster solution which also is more intuitive. just check if the next or the previous set also is free
SELECT distinct seat_id
FROM cinema
WHERE free = 1 AND
(seat_id - 1 in (select seat_id FROM cinema WHERE free = 1) OR
seat_id + 1 in (select seat_id FROM cinema WHERE free = 1))
ORDER BY seat_id;

-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | seat_id     | int  |
-- | free        | bool |
-- +-------------+------+
-- seat_id is an auto-increment column for this table.
-- Each row of this table indicates whether the ith seat is free or not. 1 means free while 0 means occupied.

 

-- Find all the consecutive available seats in the cinema.

-- Return the result table ordered by seat_id in ascending order.

-- The test cases are generated so that more than two seats are consecutively available.

-- The result format is in the following example.