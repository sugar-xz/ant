import sys
import os
import threading
import datetime
from colorama import Fore, Style
from config.setting import BASE_DIR, AUTO_LOG_LEVEL, AUTO_LOG_WRITE, REPORT_NAME, AUTO_SEND_EMAIL


class Log:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():
        if Log.log is None:
            Log.mutex.acquire()
            Log.log = Logger()
            Log.mutex.release()

        return Log.log

    @classmethod
    def get_report_path(cls):
        """
        get report file path
        :return:
        """
        report_path = os.path.join(Logger().LOG_PATH, REPORT_NAME)
        return report_path

    @classmethod
    def get_result_path(cls):
        """
        get test result path
        :return:
        """
        return Logger().LOG_PATH


class Logger:

    def __init__(self):
        self._setLevel(AUTO_LOG_LEVEL)
        self._export_path()

    def debug(self, message):
        self._println(message, "DEBUG", Fore.BLUE)

    def info(self, message):
        self._println(message, "INFO", Fore.GREEN)

    def warning(self, message):
        self._println(message, "WARNING", Fore.YELLOW)

    def error(self, message):
        frame = sys._getframe()
        list = []
        strs = ""
        self._errorLog(frame, list)
        for obj in list:
            strs += obj + "\n"
        strs = strs.strip("\n")
        self._println(str(message) + "\n" + strs, "ERROR", Fore.RED)

    def exception(self, message):
        self.error(message)
        exit()

    def _errorLog(self, frame, strs):
        if (frame.f_back != None):
            strs.append(
                "   " + frame.f_code.co_filename + ",line " + str(frame.f_lineno) + ", in " + frame.f_code.co_name)
            self._errorLog(frame.f_back, strs)
        else:
            strs.append(
                "   " + frame.f_code.co_filename + ",line " + str(frame.f_lineno) + ", in " + frame.f_code.co_name)

    def _println(self, message, type, color):
        switch = {
            "DEBUG": 36,
            "INFO": 37,
            "WARNING": 35,
            "ERROR": 31
        }
        if type in self.level:
            strMessage = datetime.datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S') + " - " + sys._getframe().f_back.f_back.f_code.co_filename + "[line " + str(
                sys._getframe().f_back.f_back.f_lineno) + "]" + " - " + str(type) + ": " + str(message)
            # print("\033[1;" + str(switch[type]) + ";0m" + strMessage + "\033[0m")
            print(color + strMessage + Style.RESET_ALL)

            # write
            if AUTO_LOG_WRITE:
                filename = os.path.join(self.LOG_PATH, "run.log")
                if not os.path.exists(filename):
                    f2 = open(filename, 'w')
                    f2.close()
                f = open(filename, 'a')
                f.write(strMessage + "\n")
                f.close()

    def _setLevel(self, level):
        if level == 10:
            self.level = ["DEBUG", "INFO", "WARNING", "ERROR"]
        elif level == 20:
            self.level = ["INFO", "WARNING", "ERROR"]
        elif level == 30:
            self.level = ["WARNING", "ERROR"]
        elif level == 40:
            self.level = ["ERROR"]

    def _export_path(self):
        EXPORT_PATH = os.path.join(BASE_DIR, "export")
        if not os.path.exists(EXPORT_PATH):
            os.mkdir(EXPORT_PATH)
        self.LOG_BASE_PATH = os.path.join(EXPORT_PATH, str(datetime.datetime.now().year))
        self.LOG_SUB_PATH = os.path.join(self.LOG_BASE_PATH, str(datetime.datetime.now().month))
        self.LOG_PATH = os.path.join(self.LOG_SUB_PATH, str(datetime.datetime.now().day))
        if AUTO_LOG_WRITE or AUTO_SEND_EMAIL:
            if not os.path.exists(self.LOG_BASE_PATH):
                os.mkdir(self.LOG_BASE_PATH)
            if not os.path.exists(self.LOG_SUB_PATH):
                os.mkdir(self.LOG_SUB_PATH)
            if not os.path.exists(self.LOG_PATH):
                os.mkdir(self.LOG_PATH)
