try:
    if not __name__ == '__main__':
        from Kernel import Input_Output as IO
        import commands as cmd


    def history():
        if not cmd.LCommand == '0':
            with open('src/history.log', 'a') as f:
                f.write(str(f"{cmd.LCommand}\n"))

    def core(MODE="0"):
        if MODE == '1' or MODE == '2' or MODE == '3' or MODE == '9':
            if not MODE == '3':
                IO.CommandAsk(MD=MODE, Module=cmd.CommandList)
                if MODE == '1' or MODE == '3':
                    history()
            else:
                IO.CommandAsk(MD=MODE, Module=cmd.CommandList, safe_mode=True)
        else:
            raise IndexError
except BaseException:
    from Kernel.utils import Exit
    Exit.error_exit()
