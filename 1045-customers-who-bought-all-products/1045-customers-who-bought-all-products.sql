select customer_id from
(select customer_id from customer group by customer_id having count(distinct(product_key)) = (select count(product_key) from product)) as x