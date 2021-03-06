def db_errorcode(driver, excep):
    """pass exception code and message from various drivers in standard way"""
    try:
        return excep.msg_no, excep.args[0]
    except AttributeError:
        if type(excep) is LoginError:
            return 1031, excep.args[0]
        else:
            print("type {type}".format(type(excep)))
            print(excep)
            print(dir(excep))

def db_error_needs_new_session(driver, code):
    """some errors justify a new database connection. In that case return true"""
    if driver == "Cx_Oracle":
        if code in(28, 1012, 1041, 3113, 3114, 3135):
            return True
        if code == 15000:
            printf('%s: asm requires sysdba role\n', \
            datetime.datetime.fromtimestamp(time.time()))
            return True
    return False
