try:
    if not __name__ == '__main__':
        import commands as cmd


    def history():
        if not cmd.LCommand == '0':
            with open('src/history.log', 'a') as f:
                f.write(str(f"{cmd.LCommand}\n"))

    def core(MODE="0"):
        if MODE == '1' or MODE == '2' or MODE == '3' or MODE == '9':
            if not MODE == '3':
                cmd.CommandAsk(MD=MODE)
                if MODE == '1' or MODE == '3':
                    history()
            else:
                cmd.CommandAsk(MD=MODE, safe_mode=True)
        else:
            raise IndexError
except BaseException:
    from Kernel.utils import error_exit
    error_exit()
