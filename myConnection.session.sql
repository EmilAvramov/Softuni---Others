SELECT 
product_name, 
order_date,
DATE_ADD(order_date, INTERVAL 3 DAY) AS payment_date,
DATE_ADD(order_date, INTERVAL 1 MONTH) AS delivery_date
FROM orders