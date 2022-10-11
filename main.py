import requests
from bs4 import BeautifulSoup
import argparse
import nltk
from nltk.corpus import stopwords
import typing
import random

def main():
    args = parse_args()
    word_list = parse_text_body(args.url)
    stop_words = set(stopwords.words('english'))
    filtered_words = [k for k in word_list if k not in stop_words]
    filtered_words = list(set(filtered_words))
    # print(filtered_words_set)
    # pick random compound words
    rand_list = random.choices(filtered_words, k=100)
    rand_tuple = [(rand_list[k],rand_list[k+1]) for k in range(0,len(rand_list),2)]
    print(rand_tuple)

def parse_text_body(url: str) -> list:
    """return text body as list"""
    word_list = []
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text,"html.parser")
        # filter whitespace
        word_list = [*filter(lambda s: s.isalpha(), map(lambda
            s:s.strip("\n").lower(), soup.get_text().split(" ")))]
    else:
        print("Error making request")
    return word_list

def parse_args():
    """Handle argument parsing"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-url', help="Url to scrape from")
    return parser.parse_args()

if __name__ == "__main__":
    main()
