class globalmanager():

    flag_zt=1
    flag_tx=2

    def set_value1(value):
        globalmanager.flag_zt=value
    def set_value2(value):
        globalmanager.flag_tx=value

    def get_value1(defValue=None):
        return globalmanager.flag_zt
    def get_value2(defValue=None):
        return globalmanager.flag_tx