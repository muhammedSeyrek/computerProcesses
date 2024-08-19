import pyzipper
import time


def extract_with_pyzipper(filePath, extractHere):
    startTime = time.time()
    try:
        with pyzipper.AESZipFile(filePath, 'r') as zip_ref:
            zip_ref.extractall(extractHere)
        endTime = time.time()
        print(f"Extraction time with pyzipper: {endTime - startTime:.2f}")
    except FileNotFoundError as e: print(f"File not found: {e}")
    except Exception as e: print(f"This error: {e}")
