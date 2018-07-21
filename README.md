# logAnalyzer
This is a reporting command  line tool implemented by python script using psycopg2 module to connect to database. 

The database contains 3 tables,  newspaper articles, authors as well as the web server log for some site. The log has a database row for each time a reader loaded a web page.

The reporting tool provide 3 commands to support 3 kind of query :

1. **What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.**
**Example:**

```
"Princess Shellfish Marries Prince Handsome" — 1201 views
"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
"Political Scandal Ends In Political Scandal" — 553 views
```
2. **Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.**
**Example:**

```
Ursula La Multa — 2304 views
Rudolf von Treppenwitz — 1985 views
Markoff Chaney — 1723 views
Anonymous Contributor — 1023 views
```
3. **On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)**
**Example:**
```
July 29, 2016 — 2.5% errors
```

## Requirements
- [Vagrant](https://www.vagrantup.com/)
- [VirtualBox](https://www.virtualbox.org/)

## Build the application
1. Clone the repo in  [provided by Udacity](https://github.com/udacity/fullstack-nanodegree-vm/tree/master/vagrant)
2. Launch the command line console, type command
```vagrant up```
3. After the virtual machine is ready tpye command:
```vagrant ssh```
4. copy logAnalyzer.py and logAnalyzerDb.py to the vagrant folder;
5. copy the database file from: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
6. back to the command line console, import the database by:<br>
   ```psql -d news -f newsdata.sql```

## Command lines for query
### get top popular articles record
``` python logAnalyzer.py toparticle [number]```
   <br>the [number] (by default is 3) is number of top articles to be retrieved
### get top popular author record
``` python logAnalyzer.py toparticle [number]```
   <br>the [number] (by default is 3) is number of top authors to be retrieved

### get the day of accident
``` python logAnalyzer.py accidentdays```

### report all of the information above
``` python logAnalyzer.py reportall```


