#!/usr/bin/env python3
#classes.py - qudaisozi.com scraper - classes
class Book:
    def __init__(self, name, chapters):
        self.name = name
        self.chapters = chapters


class Chapter:
    def __init__(self, number, verses):
        self.number = number
        self.verses = verses


class Verse:
    def __init__(self, number, text):
        self.number = number
        self.text = text
