 SELECT C.name as Customers FROM Customers C LEFT JOIN Orders O ON C.id = O.customerId WHERE O.customerId is NULL

--  the left join includes all the names in the left table, replacing the cols from the order table with null