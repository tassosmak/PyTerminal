try:
    import commands as cmd


    def history():
        with open('history.log', 'a') as f:    
            f.write(str(f"{cmd.LCommand}\n"))
                    
    def core(MODE="0", pl=0, username=0):
        if MODE == "1":
            cmd.MD = MODE
            cmd.CommandAsk(plt=pl, USNAME_PRINT=username)
            history()
        elif MODE == "2":
            cmd.MD = MODE
            cmd.CommandAsk(plt=pl, USNAME_PRINT=username)
        elif MODE == "9":
            cmd.MD = MODE         
            cmd.CommandAsk(plt=pl, USNAME_PRINT=username)
        else:
            raise IndexError
except BaseException:
    import Error_Logger.Logger as logger
    logger.log_error()
