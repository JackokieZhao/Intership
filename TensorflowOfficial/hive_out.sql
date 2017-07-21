set mapreduce.input.fileinputformat.split.maxsize=4294967296;
drop table if exists platform_temp.shopinfo_lr_0;
create table platform_temp.shopinfo_lr_0 as
select
dt,
restaurant_id shop_id,
# 长度减3， 逗号用空格代替
substr(regexp_replace(get_json_object(info,'$.features'),' , ',' '),2,
	length(regexp_replace(get_json_object(info,'$.features'),' , ',' '))-3) features,
\	ubsodulength(regexp_replace(get_json_object(info,'$.dnnFeatures'),', ',' '))-2) dnnFeatures,
is_click,
is_order,
case
when status_code in (2,9) and no_subsidy_total <= 5 then 2
when status_code in (2,9) and no_subsidy_total > 5 and no_subsidy_total <= 12 then 3
when status_code in (2,9) and no_subsidy_total > 12 and no_subsidy_total <= 20 then 4
when status_code in (2,9) and no_subsidy_total > 20 and no_subsidy_total <= 25 then 5
when status_code in (2,9) and no_subsidy_total > 25 and no_subsidy_total <= 30 then 6
when status_code in (2,9) and no_subsidy_total > 30 and no_subsidy_total <= 35 then 7
when status_code in (2,9) and no_subsidy_total > 35 and no_subsidy_total <=40 then 8
when status_code in (2,9) and no_subsidy_total > 40 and no_subsidy_total <= 68 then 9
when status_code in (2,9) and no_subsidy_total > 68 then 10
else 0 end as total_level
from platform_dw.sr_data_matrix
where dt in ('2017-07-14','2017-07-15')
and module='CHANNEL'
and sub_module='CHANNEL_FOOD'
and is_exposure = 1
and user_id is not null
and restaurant_id is not null
and substr(regexp_replace(get_json_object(info,'$.dnnFeatures'),' , ',' '),2,
	length(regexp_replace(get_json_object(info,'$.dnnFeatures'),' , ',' '))-3) is not null
and substr(regexp_replace(get_json_object(info,'$.features'),', ',' '),2,
	length(regexp_replace(get_json_object(info,'$.features'),', ',' '))-2) is not null;


	select * from platform_dw.sr_data_matrix where dt in ('2017-07-14','2017-07-15') limit 100;
	desc platform_dw.sr_data_matrix；
	select substr(regexp_replace(get_json_object(info,'$.features'),' , ',' '),2,length(regexp_replace(get_json_object(info,'$.features'),' , ',' '))-3) from platform_dw.sr_data_matrix where dt in ('2017-07-14','2017-07-15') limit 100;
