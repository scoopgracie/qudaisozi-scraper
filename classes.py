#!/usr/bin/env python3
#classes.py - qudaisozi.com scraper - classes
class Book:
    '''Book(name, chapters);
name = book name;
chapters = list of Chapter objects'''
    def __init__(self, name, chapters):
        self.name = name
        self.chapters = chapters


class Chapter:
    '''Chapter(number, verses);
number = int (chapter number);
verses = list of Verse objects'''
    def __init__(self, number, verses):
        self.number = number
        self.verses = verses


class Verse:
    '''Verse(number, text);
number = int (verse number);
text = text of verse'''
    def __init__(self, number, text):
        self.number = number
        self.text = text
