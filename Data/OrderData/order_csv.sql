
printf "Reading Data...\n"

if [ -d "$order_csv"]; then
        printf "Folder is exists and we will remake it...\n"
        rm -r order_csv
        mkdir order_csv
else
        printf "Folder isn't exits, and we will make it following...\n"
        mkdir order_csv
fi


cd sql_command
hive -f sql_command_3.sql > ../order_csv/order_03.csv
hive -f sql_command_4.sql > ../order_csv/order_04.csv
hive -f sql_command_5.sql > ../order_csv/order_05.csv
hive -f sql_command_6.sql > ../order_csv/order_06.csv

printf "Data has been saved at ./order_cdv directory...\n"
cd ..

