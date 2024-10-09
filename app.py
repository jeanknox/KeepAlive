import sys
import servicemanager
import win32event
import win32service
import win32serviceutil

class KeepAliveMachine(win32serviceutil.ServiceFramework):
    _svc_name_ = "KeepAliveMachine"
    _svc_display_name_ = "KeepAliveMachine"
    _svc_description_ = "Collect alive data from this machine"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.event = win32event.CreateEvent(None, 0, 0, None)

    def GetAcceptedControls(self):
        result = win32serviceutil.ServiceFramework.GetAcceptedControls(self)
        result |=  win32service.SERVICE_ACCEPT_PRESHUTDOWN
        return result