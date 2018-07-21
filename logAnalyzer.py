#!/usr/bin/env python3
import sys
import logAnalyzerDb


def main():
    try:
        if (len(sys.argv) < 2):
            print("please input the query command!")
            return
        if (len(sys.argv) > 2):
            arg = int(sys.argv[2])
        else:
            arg = 3

        if (sys.argv[1].lower() == "toparticle"):
            report_top_articles(arg)
        elif (sys.argv[1].lower() == "topauthor"):
            report_top_authors(arg)
        elif (sys.argv[1].lower() == "accidentdays"):
            report_accident_days()
        elif (sys.argv[1].lower() == "reportall"):
            print('*' * 20 + ' Top popular articles ' + '*' * 20)
            report_top_articles(arg)
            print('*' * 20 + ' Top popular authors ' + '*' * 20)
            report_top_authors(arg)
            print('*' * 20 + ' accident days ' + '*' * 20)
            report_accident_days()
        else:
            print(sys.argv[1]+' command not found.')
    except (Exception) as error:
        print(error)


def report_accident_days():
    """On which days did more than 1% of requests lead to errors"""
    try:
        results = logAnalyzerDb.get_show_stoper_days()
        for date, errorRate in results:
            print('{} -- {:.1f}% errors'.format(date, errorRate))
    except (Exception) as error:
        print(error)


def report_top_authors(num):
    """Who are the most popular article authors of all time?"""
    try:
        results = logAnalyzerDb.get_top_author(num)
        for author, views in results:
            print('{} -- {} views'.format(author, views))
    except (Exception) as error:
        print(error)


def report_top_articles(num):
    """On which days did more than 1% of requests lead to errors?"""
    try:
        results = logAnalyzerDb.get_top_popular(num)
        for title, views in results:
            print('"{}" -- {} views'.format(title, views))
    except (Exception) as error:
        print(error)

if __name__ == "__main__":
    main()
