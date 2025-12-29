from Makro.MakroCore.RendererKit import Renderer as RD
from Makro.MakroCore.utils import is_gui
from Makro.MakroCore import flags
import subprocess

def SecondaryTask(file_name="0", stay_end=False):
    if not flags.safe_md:
        if not file_name=='0':
            import os
            if not flags.Inside_Thread and is_gui():
                if flags.pl == "1":
                    subprocess.run(f"""osascript -e 'tell application "Terminal" to do script "python3 {str(flags.base_folder)}/../Plugins/{file_name}.py {str(flags.USERNAME)}"'""", shell=True, capture_output=True, check=True, encoding="utf-8")
                elif flags.pl == "2":
                    if stay_end:
                        os.system(f"start cmd /k py  {flags.base_folder}/../Plugins/{file_name}.py {str(flags.USERNAME)}")
                    else:
                        os.system(f"start cmd /c py  {flags.base_folder}/../Plugins/{file_name}.py {str(flags.USERNAME)}")
                else:
                    # os.system(f"python3 {flags.base_folder}/../plugins/{file_name}.py {str(flags.base_folder)}")
                    subprocess.run(f"python3 {flags.base_folder}/../Plugins/{file_name}.py {str(flags.USERNAME)}", shell=True, capture_output=True, check=True, encoding="utf-8")
            else:
                if not flags.pl == "2":
                    os.system(f"python3 {flags.base_folder}/../Plugins/{file_name}.py {str(flags.USERNAME)}")
                else:
                    os.system(f"py {flags.base_folder}/../Plugins/{file_name}.py {str(flags.USERNAME)}")
    else:
        RD.CommandShow(msg="Safe Mode is enabled, cannot run secondary tasks.").Show("WARNING")