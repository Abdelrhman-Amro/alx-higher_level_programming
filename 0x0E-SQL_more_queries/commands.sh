## 1 ##

## 2 ##

## 3 ##
cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
echo 'INSERT INTO force_name (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
echo 'SELECT * FROM force_name;' | mysql -hlocalhost -uroot -p hbtn_0d_2
## 4 ##
cat 4-never_empty.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
echo 'INSERT INTO id_not_null (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
echo 'SELECT * FROM id_not_null;' | mysql -hlocalhost -uroot -p hbtn_0d_2
## 5 ##
cat 5-unique_id.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
echo 'INSERT INTO unique_id (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
echo 'SELECT * FROM unique_id;' | mysql -hlocalhost -uroot -p hbtn_0d_2
## 6 ##
cat 6-states.sql | mysql -hlocalhost -uroot -p
echo 'INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
## 7 ##
cat 7-cities.sql | mysql -hlocalhost -uroot -p
echo 'INSERT INTO cities (state_id, name) VALUES (1, "San Francisco");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa

## 8 ##
echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
cat 8-cities_of_california_subquery.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
## 9 ##

## 10 ##

## 11 ##

## 12 ##

## 13 ##

## 14 ##

## 15 ##

## 16 ##

## 100 ##

## 101 ##

## 102 ##

## 103 ##
