from Kernel import flags
import subprocess

def SecondaryTask(file_name="0", stay_end=False):
    if not file_name=='0':
        import os
        if not flags.Inside_Thread:
            if flags.pl == "1":
                subprocess.run(f"""osascript -e 'tell application "Terminal" to do script "python3 {str(flags.base_folder)}/../plugins/{file_name}.py {str(flags.base_folder)}"'""", shell=True, capture_output=True, check=True, encoding="utf-8")
            elif flags.pl == "2":
                if stay_end:
                    os.system(f"start cmd /k py  {flags.base_folder}/plugins/{file_name}.py {str(flags.base_folder)}")
                else:
                    os.system(f"start cmd /c py  {flags.base_folder}/plugins/{file_name}.py {str(flags.base_folder)}")
            else:
                os.system(f"python3 {flags.base_folder}/plugins/{file_name}.py {str(flags.base_folder)}")
        else:
            os.system(f"python3 {flags.base_folder}/plugins/{file_name}.py {str(flags.base_folder)}")