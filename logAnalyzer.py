#!/usr/bin/env python3
import sys
import logAnalyzerDb


def main():
    if (sys.argv[1].lower() == "toparticle"):
        try:
            results = logAnalyzerDb.get_top_popular(int(sys.argv[2]))
            for result in results:
                print('"{}" -- {} views'.format(result[0],result[1]))
        except (Exception) as error:
            print(error)
    elif (sys.argv[1].lower() == "topauthor"):
        try:
            results = logAnalyzerDb.get_top_author(int(sys.argv[2]))
            for result in results:
                print('{} -- {} views'.format(result[0],result[1]))
        except (Exception) as error:
            print(error)
    elif (sys.argv[1].lower() == "accidentdays"):
        try:
            results = logAnalyzerDb.get_show_stoper_days()
            for result in results:
                print('{} -- {:.1f}% errors'.format(result[0],result[1]))
        except (Exception) as error:
            print(error)
    else:
        print(sys.argv[1]+' command not found.')

if __name__ == "__main__":
    main()
