import zipfile
import time

def extract_with_zipfile(filePath, extractHere):
    startTime = time.time()
    try:
        with zipfile.ZipFile(filePath, 'r') as zip_ref:
            zip_ref.extractall(extractHere)
        endTime = time.time()
        print(f"Extraction time with zipfile: {endTime - startTime:.2f} ")
    except FileNotFoundError as e: print(f"File not found: {e}")
    except Exception as e: print(f"This Error: {e}")


