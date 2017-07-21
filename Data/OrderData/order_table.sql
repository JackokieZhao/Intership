# !/bin/sh
cd /data1/sharedata/jackokie/data/order_data/date_2017_03_01-2017_06_30

hive

set mapreduce.input.fileinputformat.split.maxsize=4294967296;

drop table if exists platform_temp.jackokie_order_03 platform_temp.jackokie_order_04
platform_temp.jackokie_order_05
platform_temp.jackokie_order_06;

create table platform_temp.jackokie_order_06
as select restaurant_id, user_id, payment_time from platform_dw.sr_data_matrix
where dt between "2017-06-1" and "2017-06-30" and is_order=1 and eleme_city_id=1;

create table platform_temp.jackokie_order_05
as select restaurant_id, user_id, payment_time from platform_dw.sr_data_matrix
where dt between "2017-5-1" and "2017-05-31" and is_order=1 and eleme_city_id=1;

create table platform_temp.jackokie_order_04
as select restaurant_id, user_id, payment_time from platform_dw.sr_data_matrix
where dt between "2017-4-1" and "2017-04-30" and is_order=1 and eleme_city_id=1;

create table platform_temp.jackokie_order_03
as select restaurant_id, user_id, payment_time from platform_dw.sr_data_matrix
where dt between "2017-3-1" and "2017-03-31" and is_order=1 and eleme_city_id=1;

