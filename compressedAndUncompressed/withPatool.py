import patoolib
import os
import time

def extract_with_patool(filePath, extractHere):
    startTime = time.time()
    try:
        patoolib.extract_archive(filePath, outdir=extractHere)
        endTime = time.time()
        print(f"Extraction time with patool: {endTime - startTime:.2f}")
    except Exception as e: print(f"This Error! {e}")