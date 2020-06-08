### Securing Login Against SQL Injections and Data Security
+ SQL injections
+ Password protection
	- hashing
	- encryption *


### SQL Injection
x'OR'1'='1
admin' --
admin'/*
' or 1=1--
' or 1=1/*


' or 1=1#
admin' #
') or '1'='1--
') or ('1'='1--




### UNSAFE
("SELECT * FROM userstable WHERE username = '" + username + "AND password= '" + password + ")

"SELECT * FROM userstable WHERE username='" + username + "'AND password='" + password + "'";


"SELECT * FROM userstable WHERE username='{}' AND password = '{}'".format(username,password)

+ "SELECT * FROM userstable WHERE username='{}' AND password = '{}'"

+ "SELECT * FROM userstable WHERE username='x'
OR'1'='1' AND password = '{}'"


f"SELECT * FROM userstable WHERE username= '{username}' AND password= '{password}'"



### SAFE
'SELECT * FROM userstable WHERE username =? AND password = ?',(username,password)

"SELECT * FROM userstable WHERE username= '%s' AND password='%s'",(username,password)

"SELECT * FROM userstable WHERE username= %s AND password= %s",(username,password)



#### .
+ Jesus Saves@JCharisTech
+ Jesse E.Agbe(JCharis)