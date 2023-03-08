# to fix errors type this ffmpeg -i !original_file! !new_file!
from Kernel.RendererKit import Renderer as RD
from Kernel import flags
import subprocess

def play(file):
    try:
        if flags.EnableAudio and flags.FTU == '1':
            subprocess.run(f'mpg123 {file}', shell=True, capture_output=True , check=True, encoding="utf-8")
    except:
        RD.CommandSay("AudioKit failed", 'FAIL')
        from Kernel.utils import edit_json
        edit_json(loc1='UI', loc2='Enable-Audio', content='0')
        flags.EnableAudio = False