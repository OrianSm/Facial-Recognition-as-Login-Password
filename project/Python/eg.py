import mysql.connector;
import sys;

#username = sys.argv[1];
username="rushank12345678"
#password = sys.argv[2];


DB = mysql.connector.connect(host="localhost", user="root",passwd="",database="users");
pointer = DB.cursor();

pointer.execute("select Username , Password from signup");
result = pointer.fetchall();

for i in range(len(result)):
    if(username==result[i][0]):
        print("true");

#print(result[0][0]);
#print(result[0][1]);
