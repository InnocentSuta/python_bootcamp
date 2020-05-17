# -*- coding: utf-8 -*-
from urllib.request import urlopen


def fetch_words():
    story = urlopen('http://sixty-north.com/c/t.txt')
    
    story_words = []
    
    for line in story:
        
        line_words = line.decode('utf-8').split()
        
        for word in line_words:
            story_words.append(word)
            
    story.close()
    
    return story_words

def printItems(items):
    for word in items:
        print(word)
        

def main():
    words = fetch_words()
    print(words)

main()