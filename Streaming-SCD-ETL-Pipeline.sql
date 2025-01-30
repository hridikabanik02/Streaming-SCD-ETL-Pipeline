/*--CREATE TABLE totalorder AS
SELECT o.order_id,c.customer_id,c.city,c.effective_date,c.end_date,o.order_date,o.amount
FROM dim_customers c
JOIN fact_orders o ON c.customer_id = o.customer_id
WHERE (o.order_date>= c.effective_date) AND ((o.order_date<c.end_date) OR (c.end_date IS NULL));
SELECT city, COUNT(*) AS total_number, SUM(amount) AS total_amount
FROM totalorder
GROUP BY city*/

--Part 3.1
SELECT c.city, COUNT(*) AS total_number, SUM(amount) AS total_amount
FROM dim_customers c
JOIN fact_orders o ON c.customer_id = o.customer_id
WHERE (o.order_date>= c.effective_date) AND ((o.order_date<c.end_date) OR (c.end_date IS NULL))
GROUP BY city;

--Part 3.2
SELECT o.customer_id, COUNT(order_id) AS total_orders
FROM fact_orders o
GROUP BY o.customer_id;
--Question Answer: Yes, it was required to join fact_orders to dim_customer


--Part 3.3
/*CREATE TABLE totalorder1 AS
SELECT o.order_id,c.customer_id,c.city,c.effective_date,c.end_date,c.is_current,o.order_date, o.amount
FROM dim_customers c
JOIN fact_orders o ON c.customer_id = o.customer_id
WHERE (o.order_date>= c.effective_date) AND ((o.order_date<c.end_date) OR (c.end_date IS NULL));*/
/*SELECT customer_id, SUM(CASE WHEN is_current = 1 THEN amount END) AS current_city_amount, SUM(CASE WHEN is_current = 0 THEN amount END) AS previous_city_amount
FROM totalorder1
GROUP BY customer_id;*/


SELECT customer_id, SUM(CASE WHEN is_current = 1 THEN amount END) AS current_city_amount, SUM(CASE WHEN is_current = 0 THEN amount END) AS previous_city_amount
FROM dim_customers c
JOIN fact_orders o ON c.customer_id = o.customer_id
WHERE (o.order_date>= c.effective_date) AND ((o.order_date<c.end_date) OR (c.end_date IS NULL))
GROUP BY c.customer_id;
