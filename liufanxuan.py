import os.path


def count_char(fn):
    if os.path.isfile(fn):
        with open(fn, 'r') as fh:  
            total = 0
            words = 0
            for line in fh:
                words = line.split(None)
                print(words)  
                total += len(words)  
            return total

count = count_char('C:/Users/na/Desktop/liufanxuan/SES2020spring/unit2/readme.md')
print(f'The total number of the words is {count}' )
