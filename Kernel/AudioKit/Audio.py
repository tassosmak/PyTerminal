# to fix errors type this ffmpeg -i !original_file! !new_file!
import subprocess

def play(file):
    subprocess.run(f'mpg123 {file}', shell=True, capture_output=True , check=True, encoding="utf-8")