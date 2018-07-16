import sys
import logAnalyzerDb


def main():
    if (sys.argv[1].lower() == "toparticle"):
        try:
            print(logAnalyzerDb.get_top_popular(int(sys.argv[2])))
        except:
            print(sys.argv[2])
            print("The argument is not correct.")
    elif (sys.argv[1].lower() == "topauthor"):
        try:
            print(logAnalyzerDb.get_top_author(int(sys.argv[2])))
        except:
            print("The argument is not correct.")
    elif (sys.argv[1].lower() == "accidentdays"):
        print(logAnalyzerDb.get_show_stoper_days())
    else:
        print(sys.argv[1]+' command not found.')

if __name__ == "__main__":
    main()
