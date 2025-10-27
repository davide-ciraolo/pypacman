from threading import Thread
from time import sleep

class Timer():

    def __init__(self, interval = 0.0, func = None, f_args = ()):
        self._sec = 0
        self._interval = interval
        self._isRunning = False
        self._Func = func
        self._Fargs = f_args

    def reset(self):
        self.stop()
        self._sec = 0

    def start(self):
        if self._isRunning == False:
            self._main_thread = Thread(target=self.main, args=())
            self._main_thread.setDaemon(daemonic=True)
            self._main_thread.start()

    def stop(self):
        if self._isRunning == True:
            self._isRunning = False

    def set_sec(self, sec = 0):
        self._sec = sec

    def get_sec(self):
        return self._sec

    def set_interval(self, interval = 0.0):
        self._interval = interval

    def get_interval(self):
        return self._interval

    def set_isRunning(self, bool = False):
        self._isRunning = bool

    def get_isRunning(self):
        return self._isRunning

    def set_Func(self, func = None):
        self._Func = func

    def get_Func(self):
        return self._Func

    def set_Fargs(self, f_args = ()):
        self._Fargs = f_args

    def get_Fargs(self):
        return self._Fargs

    def main(self):
        self._Running = True
        while self._Running == True:
            self._Func(*self._Fargs)
            self._sec +=1
            sleep(self._interval)
