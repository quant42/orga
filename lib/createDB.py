#! python
# -*- coding: UTF-8 -*-

import sqlite3 as sl

def dropTables():
    with sl.connect('db.dat') as con:
        con.execute("DROP TABLE IF EXISTS TASKS;")
        con.execute("DROP TABLE IF EXISTS CONFIGURATION;")
        con.execute("DROP TABLE IF EXISTS LOGIN;")
        con.execute("DROP TABLE IF EXISTS USER;")
        con.execute("DROP TABLE IF EXISTS TASKLIST;")
        con.execute("DROP TABLE IF EXISTS TASKLISTSECURITY;")

def createTables():
    with sl.connect('db.dat') as con:
        con.execute("""
            CREATE TABLE CONFIGURATION (
                Section TEXT NOT NULL,
                Name TEXT NOT NULL,
                Value TEXT,
                Type TINYINT,
                PRIMARY KEY(Section, Name)
            );
        """)
        con.execute("""
            CREATE TABLE USER (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT
            );
        """);
        con.execute("""
            CREATE TABLE LOGIN (
                id INTEGER NOT NULL PRIMARY KEY REFERENCES USER(id),
                passwordEncryptionAlgorithm INTEGER,
                hash TEXT,
                cryptedPassword TEXT,
                lastLogin DATETIME,
                needPasswordChange BOOLEAN
            );
        """)
        con.execute("""
            CREATE TABLE TASKLIST (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name STRING,
                description STRING,
                everyoneCanRead BOOLEAN,
                loggedinUserCanRead BOOLEAN,
                loggedinUserCanWrite BOOLEAN
            );
        """)
        con.execute("""
            CREATE TABLE TASKS (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                listId INTEGER REFERENCES TASKLIST(id),
                done BOOLEAN,
                description STRING
            );
        """)
        con.execute("""
            CREATE TABLE TASKLISTSECURITY (
                userId INTEGER REFERENCES USER(id),
                tableId INTEGER REFERENCES TASKLIST(id),
                canRead BOOLEAN,
                canWrite BOOLEAN,
                canCheck BOOLEAN,
                PRIMARY KEY(userId, tableId)
            )
        """)

if __name__ == '__main__':
    dropTables();
    createTables();
