import subprocess
import sys

def process(action, file, outputPath):
    sevenZipPath = r'C:\Program Files\7-Zip\7z.exe'
    flag = 0
    while(flag != 1):
        flag = 1
        if action.strip() == 'compress': command = [sevenZipPath, 'a', '-tzip', outputPath, file]
        elif action.strip() == 'extract': command = [sevenZipPath, 'x', file, f'-o{outputPath}']
        else:
            flag = 0
            print("Invalid action. Please use 'compress' or 'extract'.")

    try:
        subprocess.run(command, check = True, shell = True)
    except subprocess.CalledProcessError as e: print(f"Error occurred: {e}")
    except FileNotFoundError as e: print(f"File not found: {e}")
    except Exception as e: print(f"Unexpected error!: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python zipProcess.py <compress/extract> <file> <outputPath/output name>")
        sys.exit(1)
    
    action = sys.argv[1]
    file = sys.argv[2]
    outputPath = sys.argv[3]

    process(action, file, outputPath)
