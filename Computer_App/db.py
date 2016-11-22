import mysql.connector

logged_user = None
logged_pw = None

#initalizes database if table doesn't already exist
def addToUserTable(user, pw, fname, lname):
    (conn, cursor) = createCon('cs115','insecuurity')
    try:
        create = ("CREATE USER '%s' IDENTIFIED BY '%s'" %(user, pw))
        cursor.execute(create)
        permissions = ("GRANT SELECT,DELETE,INSERT,UPDATE ON SECUURE.DATA TO '%s' IDENTIFIED BY '%s'" %(user, pw) )
        cursor.execute(permissions)
        conn.commit()
    except mysql.connector.Error as e:
        print ("User already exists")
        conn.close()
        return
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            id  INTEGER ,
            username  text,
            first_name  text,
            last_name  text
            )""")
    insertToUserTable(fname, lname, user)
    conn.close()


#gets highest ID number in the USER table
def getUserIdNum():
    (conn, cursor) = createCon('cs115','insecuurity')
    cursor.execute("""SELECT ID from users""")
    max_id = 0
    for id in cursor:
        if id[0] > max_id:
            max_id = id[0]
    conn.close()
    return max_id

#gets highest ID number in the DATA table -- need two different functions because user permissions will be different
def getUserIdForData(username):
    (conn, cursor) = createCon('cs115','insecuurity')
    select_uid = """SELECT id, username from users where username='%s' """ %username
    cursor.execute(select_uid)
    for i, u in cursor:
        return i


def createPassTable():
    (conn, cursor) = createCon('cs115','insecuurity')
    cursor.execute("""CREATE TABLE IF NOT EXISTS data(
                userid integer,
                username text,
                website text,
                password text,
                notes text
                )""")
    conn.close()

#inserts into the "users" table.
#Thing to note: table to be inserted into CANNOT be a variable (must be hardcoded)
def insertToUserTable(fname,lname, user):
    (conn, cursor) = createCon('cs115','insecuurity')
    max_id = getUserIdNum()

    print(max_id)

    query = ("""SELECT username FROM users""")       #
    cursor.execute(query)                           #
    for u in cursor:                                # This piece checks if an account exists already
        if u[0].lower() == user.lower():           #
             print("Account name already exists")    #
             return                                  #
    cursor.execute("""INSERT IGNORE INTO users values (%s, %s, %s, %s)""", (max_id+1, user, fname, lname))
    conn.commit()
    conn.close()


#Iterates over the database and looks for login and login_pw, if they match, returns true, otherwise false.
def verMasterLogin(login, login_pw):
    if createCon(login, login_pw) is not None:
        (conn, cursor) = createCon(login, login_pw)
        global logged_user
        logged_user = login
        global logged_pw
        logged_pw = login_pw
        conn.close()
        return True
    else:
       return False

#Creates connection to local MySQL database#  Passwords for accounts are no longer stored on the db
def createCon(user, pw):
    try:
        conn = mysql.connector.connect(user=user, password=pw, host = '98.234.141.183', database='secuure') #isaak: 98.234.141.183
        cursor = conn.cursor()
        return (conn, cursor)
    except mysql.connector.Error as e:
        return
    # note the above host name is my local one: external IP is 98.234.141.183



#Adds a username and password for a specific website given by the user
def addPassForWebsite(username, pw, website, notes):
    global logged_user
    global logged_pw
    print (logged_user, logged_pw)
    (conn, cursor) = createCon(logged_user, logged_pw)
    query = ("""SELECT account, website FROM data """)
    cursor.execute(query)
    for u, w in cursor:
        if u.lower() == username.lower() and website.lower() == w.lower():
            print("Duplicate entry in table, please try again")
            conn.close
            return
    cursor.execute("""INSERT IGNORE INTO data values (%s, %s, %s, %s, %s)""", (getUserIdForData(username), username, website, pw, notes))
    conn.commit()
    conn.close()

#Prints passwords for a specified user
def getPasswordsForUser(accountName):
    global logged_user
    global logged_pw
    (conn, cursor) = createCon(logged_user, logged_pw)
    data = []
    query=("""SELECT account, password, website, notes FROM DATA WHERE userid=%s""" %getUserIdForData(accountName))
    cursor.execute(query)
    for a, p, w, n in cursor:
        if accountName.lower() == a.lower():
            data.append((a, p, w, n))
    conn.close()
    return data


#Removes entry from the table, all values have to match
def removeEntry(username, pw, website, notes):
    global logged_user
    global logged_pw
    (conn, cursor) = createCon(logged_user, logged_pw)
    query = """DELETE FROM DATA WHERE userid=%s && account='%s' && website='%s' && password='%s' && notes='%s'""" %(getUserIdForData(username), username, website, pw, notes, )

    print (query)
    cursor.execute(query)
    conn.commit()
    conn.close()


#####################
#      Testing      #
#####################

addToUserTable('joking','root', 'John', 'King')
print(verMasterLogin('joking','root'))
print("Before printing\n")
addPassForWebsite("joking", "mypass3!!!21test", "gmail", "last")
addPassForWebsite("joking", "mypass321test", "yahoo", "last")
getPasswordsForUser("joking")
print("After printing\n")
removeEntry("joking", "mypass3!!!21test", "gmail", "last")
getPasswordsForUser("joking")






