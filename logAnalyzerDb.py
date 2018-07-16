import psycopg2

DBNAME = "news"

def get_top_popular(top_num):
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute("SELECT articles.title, COUNT(log.path) AS num FROM articles LEFT JOIN log ON log.path LIKE '%' || articles.slug || '%' GROUP BY articles.title ORDER BY num DESC")
    titles = cursor.fetchmany(top_num)
    conn.commit()
    conn.close()
    return titles

def get_top_author(top_num):
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute("SELECT authors.name,author_result.num FROM authors JOIN (SELECT SUM(article_result.num) as num, article_result.author from (SELECT articles.title, articles.author, COUNT(log.path)\
                   AS num FROM articles LEFT JOIN log ON log.path LIKE '%' || articles.slug || '%' GROUP BY articles.title, articles.author) AS article_result GROUP BY article_result.author) as author_result\
                   ON authors.id = author_result.author ORDER BY num DESC")
    author_result = cursor.fetchmany(top_num)
    conn.commit()
    conn.close()
    return author_result

def get_show_stoper_days():
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute("SELECT time from (SELECT all_result.time::DATE, all_result.all, bad_result.bad FROM (SELECT time::DATE, COUNT(\
                    time::DATE) as all FROM log GROUP BY time::DATE) AS all_result JOIN  (SELECT time::DATE, COUNT(time::DATE) as bad from\
                    log WHERE status !='200 OK' GROUP BY TIME::DATE) as bad_result ON all_result.time::DATE = bad_result.time::DATE) AS\
                    error_report WHERE error_report.bad*100 > error_report.all")
    show_stoper_day = cursor.fetchall()
    conn.commit()
    conn.close()
    return show_stoper_day


