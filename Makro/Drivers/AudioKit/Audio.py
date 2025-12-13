"""PyTerminal Audio Library"""
# to fix errors type this ffmpeg -i !original_file! !new_file!
from Makro.MakroCore.RendererKit import Renderer as RD
from Makro.MakroCore import flags
import subprocess

def play(file):
    try:
        if flags.EnableAudio and flags.FTU == '1':
            subprocess.run(f'mpg123 {flags.base_folder}/../{file}', shell=True, capture_output=True , check=True, encoding="utf-8")
    except:
        RD.CommandShow("AudioKit failed").Show('FAIL')
        from Makro.MakroCore.JSONhander import JSONhandle
        json = JSONhandle(f'{flags.base_folder}/users/default.json')
        json.edit_json(loc1='UI', loc2='Enable-Audio', content='0')
        flags.EnableAudio = False