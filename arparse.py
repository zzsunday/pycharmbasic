from pathlib import Path
import argparse

def showdir(path:str='.'):
    p = Path(path)
    for file in p.iterdir():
        print(file.name)

paser = argparse.ArgumentParser()
if __name__ == '__main__':
    showdir(r'E:/markdown/')
    args = paser.parse_args()