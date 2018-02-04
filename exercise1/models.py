# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import json
# Create your models here.

class ValidWord(models.Model):
	inputword = models.CharField(max_length=20)
	listword = models.TextField()
	
	def saveValid(self):
		valid_words = open("exercise1\static\words.txt", "r")
		mywords = []
		for valid_word in valid_words:
			word_array = list(valid_word.replace("\n", "").lower())
			input_word_array = list(self.inputword.lower())
			if len(word_array) > len(input_word_array):
				continue
			match = True
			for letter in word_array:
				if letter in input_word_array:
					input_word_array.pop(input_word_array.index(letter))
				else:
					match = False
					break
			if match:
				#self.listword =  json.dumps(valid_word.replace("\n", ""))
				mywords.append(valid_word.replace("\n", ""))
		self.listword = ',\n'.join(mywords)	
		print self.listword
		valid_words.close()

	def __str__(self):
		return self.listword