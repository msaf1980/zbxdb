def db_errorcode(driver, excep):
    """pass exception code and message from various drivers in standard way"""
    if excep.pgcode is None:
        c = 1031
    else:
        c = excep.pgcode
    return c, str(excep.args[0])

def db_error_needs_new_session(driver, code):
    """some errors justify a new database connection. In that case return true"""
    return False
