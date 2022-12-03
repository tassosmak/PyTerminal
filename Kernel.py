try:
    if not __name__ == '__main__':
        import commands as cmd


    def history():
        with open('src/history.log', 'a') as f:    
            f.write(str(f"{cmd.LCommand}\n"))

    def core(MODE="0", pl=0, username=0):
        if MODE == '1' or MODE == '2' or MODE == '3' or MODE == '9':
            if not MODE == '3':
                cmd.CommandAsk(plt=pl, USNAME_PRINT=username, MD=MODE)
                if MODE == '1' or MODE == '3':
                    history()
            else:
                cmd.CommandAsk(plt=pl, MD=MODE, safe_mode=True)
        else:
            raise IndexError
except BaseException:
    import Error_Logger.Logger as logger
    logger.log_error()
