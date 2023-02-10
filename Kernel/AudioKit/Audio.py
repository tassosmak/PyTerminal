# to fix errors type this ffmpeg -i !original_file! !new_file!
import subprocess
from Kernel.RendererKit import Renderer as RD
from Kernel import flags

def play(file):
    try:
        if flags.EnableAudio:
            subprocess.run(f'mpg123 {file}', shell=True, capture_output=True , check=True, encoding="utf-8")
    except:
        RD.CommandSay("AudioKit failed", 'FAIl')