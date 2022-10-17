import pandas as pd # pandas это библиотеку которую надо скачать $ pip install pandas

def main():
    text = input()
    lst = list(text.lower())
    lst.sort()
    for i in range(len(lst)):
        if lst[0] in [' ',',','.',';',':','...',"'",'!','?','/','\\','|','@','#','№','$','*','-','=','+','"','{','}','[',']','(',')','&','^','%','`','~']:
            lst.pop(0)
    print(pd.Series(lst).value_counts())


if __name__ == "__main__":
    main()