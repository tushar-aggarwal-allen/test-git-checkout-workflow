import sys
import requests
import numpy as np
import pandas as pd

def main():
    print("NumPy Version:", np.__version__)
    print("Pandas Version:", pd.__version__)

    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    print("Sample API Response:", response.json())

    if len(sys.argv) > 1:
        print("Received arguments:", sys.argv[1:])

if __name__ == "__main__":
    main()
