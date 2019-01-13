#!/usr/bin/env python3
"""Udacity Log Analysis Project"""

import psycopg2

DBNAME = "news"

query_one = ''' SELECT articles.title, count(*) AS views FROM articles 
INNER JOIN log ON log.path = concat('/article/', articles.slug) 
WHERE log.status LIKE '%200%' 
GROUP BY title, log.path ORDER BY views DESC
LIMIT 3; '''

def db_connection(query):
  """Instantiate PSQL db connection and return db cursor with given query result"""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute(query)
  return c.fetchall()
  db.close()
  
def question(query):
  answers = db_connection(query)
  if query == query_one:
    print('Q1: What are the most popular three articles of all time?')
    for answer in answers:
        print('\t' + str(answer[0]) + ' - ' + str(answer[1]) + 'views')

if __name__ == '__main__':
  question(query_one)