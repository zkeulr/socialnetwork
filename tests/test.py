import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import collect, visualize

analyzed_data = collect.load_analyzed_data().copy()
print(len(analyzed_data))
print(analyzed_data)
