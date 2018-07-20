#!/usr/bin/env python3
import psycopg2

DBNAME = "news"

def execute_query(cmd):
    """ common function for psql query """
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute(cmd)
    result = cursor.fetchall()
    conn.close()
    return result


def get_top_popular(top_num):
    """ query the top(top_num) popular articles 
        top_num => list of [title, count]
    """
    cmd = """SELECT articles.title, COUNT(log.path) AS num
                   FROM articles LEFT JOIN log 
                   ON log.path = '/article/'||articles.slug
                   GROUP BY articles.title ORDER BY num DESC LIMIT {}""".format(top_num)
    return execute_query(cmd)


def get_top_author(top_num):
    """ query the top(top_num) popular author 
        top_num => list of [author, count]
    """
    cmd = """SELECT authors.name,author_result.num 
                    FROM authors JOIN 
                    (SELECT SUM(article_result.num) as num, article_result.author
                    from (SELECT articles.title, articles.author, COUNT(log.path) AS num 
                    FROM articles LEFT JOIN log ON log.path = '/article/'
                    || articles.slug GROUP BY articles.title, articles.author) AS article_result
                    GROUP BY article_result.author) as author_result
                    ON authors.id = author_result.author ORDER BY num DESC LIMIT {}""".format(top_num)
    return execute_query(cmd)


def get_show_stoper_days():
    """ query the accident(errors happened more than 1%) days 
        => list of [date, error rate]
    """
    cmd = """SELECT time,error_report.bad*100/error_report.all::float as errors from (SELECT all_result.time::DATE,
             all_result.all, bad_result.bad FROM (SELECT
             time::DATE, COUNT(
             time::DATE) as all FROM log GROUP BY time::DATE)
             AS all_result JOIN  (SELECT time::DATE,
             COUNT(time::DATE) as bad from
             log WHERE status !='200 OK' GROUP BY
             TIME::DATE) as bad_result ON
             all_result.time::DATE = bad_result.time::DATE)
             AS error_report WHERE
             error_report.bad*100 > error_report.all"""
    return execute_query(cmd)
