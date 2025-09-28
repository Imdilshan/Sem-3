
1.  **How do we model a many-to-many relationship between two database tables?**
    * [x] We add a table with two foreign keys
-----

2.  **In Python, what is a database "cursor" most like?**
    * [x] A file handle
-----

3.  **What method do you call in an SQLite cursor object in Python to run an SQL command?**
    * [x] execute()
-----

4.  **In the following SQL, what is the purpose of the "?"?**
`cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))`

    * [x] It is a placeholder for the contents of the "org" variable
-----

5.  **In the following Python code sequence, what is the value in row if no rows match the WHERE clause?**
`row = cur.fetchone()`
    * [x] None

-----

6.  What does the LIMIT clause in the following SQL accomplish?

    ```sql
    1   SELECT org, count FROM Counts
    2   ORDER BY count DESC LIMIT 10
    ```

      * [x] It only retrieves the first 10 rows from the table
-----

7.  What does the executescript() method in the Python SQLite cursor object do that the normal execute() method does not do?

      * [x] It allows multiple SQL statements separated by semicolons
-----


**8. What is the purpose of "OR IGNORE" in the following SQL:**

```sql
1   INSERT OR IGNORE INTO Course (title) VALUES ( ? )
```

  * [x] It makes sure that if a particular title is already in the table, there are no duplicate rows inserted
-----

**9. What do we generally avoid in a many-to-many junction table?**
  * [x] Data items specific to the many-to-many relationship
-----












