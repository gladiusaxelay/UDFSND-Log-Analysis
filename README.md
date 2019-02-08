# Log Analysis

This project goal is to create a Python reporting tool that prints out (in plain text) the answer to the below queries based on the data in the database. 

This DB contains:
*Newspaper articles and their authors, as well as the web server log for the site. 
*The log has a database row for each time a reader loaded a web page.

Queries to answer:
1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
3. On which days did more than 1% of requests lead to errors?

## Getting Started

1. Donwload and install [Vagrant](https://www.vagrantup.com/downloads.html), [VirtualBox](https://www.virtualbox.org/wiki/Downloads), [Python](https://www.python.org/downloads/).
2. Clone or download the following [repository](https://github.com/udacity/fullstack-nanodegree-vm).

### Prerequisites

*Unix style terminal
*Vagrant (VM configuration file available in the repository above)
*VirtualBox
*Python
*newsdata DB from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

### Installing

1. On the repository ```vagrant/``` sub-directory do ```vagrant up```. This will make Vagrant download and install the Linux image and dependencies. It may take a while.
2. After it finishes, run ```vagrant ssh``` to log in to this newly-installed VM.
3. Put the ```newsdata.sql``` into the ```vagrant/``` directory, which is shared with your virtual machine.
4. To load the data, ```cd``` into the ```vagrant``` directory and use the command ```psql -d news -f newsdata.sql```. Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

## Running the report

To run the report do:

```
python news.py
```

### Results

The output on your terminal should be as:

```
Q1: What are the most popular three articles of all time?
        Candidate is jerk, alleges rival - xxx views
        Bears love berries, alleges bear - yyy views
        Bad things gone, say good people - zzz views
Q2: Who are the most popular article authors of all time?
        Ursula La Multa - xxx views
        Rudolf von Treppenwitz - yyy views
        Anonymous Contributor - zzz views
        Markoff Chaney - aaa views
Q3: On which days did more than 1% of requests lead to errors?
        2016-07-17 - x.xx % of errors
```

## Acknowledgments

* Vagrant VM configuration and DB provided by Udacity.
