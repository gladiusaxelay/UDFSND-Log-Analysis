#!/usr/bin/env python3
"""Udacity Log Analysis Project"""

import psycopg2

DBNAME = "news"

query_one = ''' SELECT articles.title, count(*) AS views FROM articles 
INNER JOIN log ON log.path = concat('/article/', articles.slug) 
WHERE log.status LIKE '%200%' 
GROUP BY title, log.path ORDER BY views DESC
LIMIT 3; '''

query_two = '''SELECT authors.name, count(*) AS views FROM articles
INNER JOIN authors ON articles.author = authors.id
INNER JOIN log ON log.path = concat('/article/', articles.slug)
WHERE log.status LIKE '%200%' 
GROUP BY authors.name ORDER BY views DESC;
'''

def db_connection(query):
  """Instantiate PSQL db connection and return db cursor with given query result"""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute(query)
  return c.fetchall()
  db.close()

def print_query(answers, addition):
  for answer in answers:
        print('\t' + str(answer[0]) + ' - ' + str(answer[1]) + ' ' + addition)
  
def question(query):
  answers = db_connection(query)
  if query == query_one:
    print('Q1: What are the most popular three articles of all time?')
    print_query(answers, 'views')
  if query == query_two:
    print('Q2: Who are the most popular article authors of all time?')
    print_query(answers, 'views')

if __name__ == '__main__':
  question(query_one)
  question(query_two)