from db import *

print ("Adding user: 'UnitTest' to database with Password: 'root' with function 'addToUserTable\n")
print ("Printing output of addToUserTable - True = Successful, False = Failure\n")
print ("addToUserTable", addToUserTable('UnitTest','root', 'John', 'King'), "\n\n")

print ("Testing connection with newly created account: 'UserTest' by calling function 'verMasterLogin()'\n")
print ("Printing output of verMasterLogin - True = Login above was created and connection was successful, False = Failure\n")
print("verMasterLogin", verMasterLogin('UnitTest','root'))

print("Testing 'addPassForWebsite' function for user: 'UnitTest'\n")
print("Will add two entries for the same user, one for 'gmail' and one for 'yahoo' with passwords 'test1' and 'test2' respectively\n")
addPassForWebsite("UnitTest", "test1", "gmail", "UnitTest1")
addPassForWebsite("UnitTest", "test2", "yahoo", "UnitTest2")

print("Testing the input for the above inserts\n")
print("Expected output similar to: 'UnitTest' 'test1' 'gmail' 'UnitTest1'\n")
print("Second output similar to: UnitTest' 'test2' 'yahoo' 'UnitTest2'\n")
data = getPasswordsForUser("UnitTest")

for (a, w, p, n) in data:
    print ("User: ", a, "Password :", p, "Website: ", w, "Notes: ", n)

print("Testing the remove function\n")
print("Removing gmail entry from user 'UnitTest'\n")
removeEntry("UnitTest", "gmail")

print("Testing success of remove function\n")
print("Expected output show now not show the gmail entry, and only the yahoo entry submitted above\n")
data = getPasswordsForUser("UnitTest")

for (a, w, p, n) in data:
    print ("User: ", a, "Password :", p, "Website: ", w, "Notes: ", n)