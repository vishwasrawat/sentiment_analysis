import pandas as pd
import numpy as np 
import re
import nltk 

from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split, GridSearchCV

import seaborn as sb 
import matplotlib.pyplot as plt


