import urllib.request
import string
from thefuzz import fuzz

def import_text(url):
    """This Function read in the text from the url"""
    response = urllib.request.urlopen(url)
    data = response.read()  # a `bytes` object
    text = data.decode('utf-8')
    return text

# def get_a_score(text):
#     score = SentimentIntensityAnalyzer().polarity_scores(text)
#     return score

def get_word_num(url,skip_header):
    """This function break up the text and count each word and insert it into
    a dictionary with the key is the word and the value is the number of time it appers"""
    text = import_text(url)
    hist = {}
    hist_process = {}

    if skip_header:
        skip_gutenberg_header(text)

    strippables = string.punctuation
    
    for c in strippables:
        text = text.replace(c," ")
    text_new = text.lower()
   
    for word in text_new.split():
        if word.startswith('*** END OF THIS PROJECT'):
            break

            # update the dictionary
        hist[word] = hist.get(word, 0) + 1
    
    for key in hist:
        if hist[key] > 10:
            hist_process[key] = hist[key]
    
    hist_process = dict(sorted(hist_process.items(), key=lambda x:x[1],reverse= True))
    return hist_process


def stop_word(filename):
    fp = open(filename, encoding='UTF8')
    stop_dic = {}
    for line in fp:
        word = line.strip()
        stop_dic[word] = 0
    return stop_dic


def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.
    d1, d2: dictionaries
    """
    final = {}
    for key in d1:
        if key not in d2:
            final[key] = d1[key]

    return final

def get_top_10(text):
    count = 0
    top = []
    for key, value in text.items():
        count += 1
        if count <= 10:
            top.append([key,value])
    return top

def print_top_10(name,content):
    print("The top ten words for", name, ":")
    for item in content:
        print(item[0],item[1])

def compare_text(text1,text2):
    print(fuzz.ratio(text1,text2))
    print(fuzz.token_sort_ratio(text1,text2))
    print(fuzz.token_set_ratio(text1,text2))

def skip_gutenberg_header(text):
    """Reads from text until it finds the line that ends the header.

    """
    for line in text:
        if line.startswith('*** START OF THIS PROJECT'):
            break

def main():
    url1 = 'https://www.gutenberg.org/files/93/93-0.txt'
    url2 = 'https://www.gutenberg.org/files/76/76-0.txt'
    text1 = import_text(url1)
    text2 = import_text(url2)
    # print("The score for text1 is:", get_a_score(text1))
    # print("The score for text1 is:", get_a_score(text1))
    d1 = get_word_num(url1,skip_header=True)
    d2 = get_word_num(url2,skip_header=True)
    filename = 'data/stopwords.txt'
    d = stop_word(filename)
    clean_1 = subtract(d1,d)
    clean_2 = subtract(d2,d)
    top1 = get_top_10(clean_1)
    top2 = get_top_10(clean_2)
    print(print_top_10("text1",top1))
    print(print_top_10("text2",top2))
    compare_text(text1,text2)

if __name__ == "__main__":
    main()