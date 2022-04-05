import mysql.connector
import sys
import secret
import appLogging

def insertURL(url,categoryName):
    try:
        conn = mysql.connector.connect(
                user=secret.dbuser,
                password=secret.dbpass,
                host="127.0.0.1",
                database="MIKEMELD"
                )
    except mysql.connector.Error as e:
        appLogging.logData(1,"Error Connecting to MariaDB Platform: {e}")
        sys.exit(1)

    #GET Cursor

    try:
        cur = conn.cursor()
        QUERY = "INSERT INTO URLCAT (URL,CATEGORYNAME) VALUES (%s, %s)"
        VALUES = (url, categoryName)
        cur.execute(QUERY, VALUES)

        appLogging.logData(4, " URL Inserted " + url + categoryName)
        
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        appLogging.logData(3,e)
        #Don't interrupt

def getAllCat():
    urlCatDic = dict();
    try:
        conn = mysql.connector.connect(
                user=secret.dbuser,
                password=secret.dbpass,
                host="127.0.0.1",
                database="MIKEMELD"
                )
    except mysql.connector.Error as e:
        appLogging.logData(1,"Error Connecting to MariaDB Platform: {e}")
        sys.exit(1)

    cur = conn.cursor()
    QUERY = "SELECT CATEGORY, URL FROM URLCAT"
    cur.execute(QUERY)

    for(CATEGORY,URL) in cur:
        urlCatDic[CATEGORY] = URL
    
    cur.close()
    conn.close()

    return urlCatDic

def getAllIPCatName():
    urlCatDic = dict();
    try:
        conn = mysql.connector.connect(
                user=secret.dbuser,
                password=secret.dbpass,
                host="127.0.0.1",
                database="MIKEMELD"
                )
    except mysql.connector.Error as e:
        appLogging.logData(1,"Error Connecting to MariaDB Platform: {e}")
        sys.exit(1)

    cur = conn.cursor()
    QUERY = "SELECT IPBLOCK.IP , URLCAT.CATEGORYNAME FROM IPBLOCK INNER JOIN URLCAT ON IPBLOCK.CATEGORY = URLCAT.CATEGORY"
    cur.execute(QUERY)

    for(IP,CATEGORYNAME) in cur:
        urlCatDic[IP] = CATEGORYNAME
    
    cur.close()
    conn.close()

    return urlCatDic

def insertIPBLOCK(ipblock,category):
    try:
        conn = mysql.connector.connect(
                user=secret.dbuser,
                password=secret.dbpass,
                host="127.0.0.1",
                database="MIKEMELD"
                )
    except mysql.connector.Error as e:
        appLogging.logData(1,"Error Connecting to MariaDB Platform: {e}")
        sys.exit(1)
    try:
        cur = conn.cursor()
        QUERY = "INSERT INTO IPBLOCK (IP, CATEGORY) VALUES (%s, %s)"
        VALUES = (ipblock, category)
        cur.execute(QUERY,VALUES)
        appLogging.logData(4, str(cur.rowcount) + " Record inserted " + str(ipblock) +  "CAT: " + str(category))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        t = 0
        appLogging.logData(3,e)
        #Don't interrupt

