import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWebEngineWidgets, QtWebEngine, QtWebEngineCore
import subprocess
import urllib.request as _req
import zipfile

uiFile = "pixArk.ui"


class Example(QWidget):

    def __init__(self, app):
        super(Example, self).__init__()
        self.app = app
        self.rp_path = None
        self.branch_text = None
        self.com_msg = None
        self.stdouterr = None
        self.counter = 0
        self.steam_cmd = os.path.expanduser("~/Desktop/steamcmd")
        if not os.path.isdir(self.steam_cmd):

            url = 'http://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip'
            response = _req.urlopen(url)
            zip_data = response.read()
            download_save_location = os.path.expanduser("~/Downloads/steamcmd.zip")
            output = open(download_save_location, 'wb')
            output.write(zip_data)
            output.close()
            with zipfile.ZipFile(download_save_location, 'r') as zip:
                zip.extractall(path=self.steam_cmd)
                zip.close()
        self.init_UI()

    def init_UI(self):
        uic.loadUi(uiFile, self)

        self.start_server.setDefault(False)
        self.start_server.clicked.connect(self.start)

        self.setWindowTitle("PixArk Server Manager")

    def start(self):
        port = self.port.text()
        c_port = self.cube_port.text()
        q_port = self.q_port.text()
        rcon_port = self.rcon_port.text()
        server_path = self.location_text.text()
        server_name = self.server_name.text()
        server_pass = self.server_pass.text()
        admin_pass = self.admin_pass.text()
        players_no = self.players_no.text()
        if not os.path.isdir(server_path):
            os.chdir(self.steam_cmd)
            subprocess.Popen(["start steamcmd.exe +login anonymous +force_install_dir {0} +app_update 824360 validate ".
                             format(server_path)],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT,
                             shell=True,
                             bufsize=0)
        subprocess.Popen(["start steamcmd.exe +login anonymous +force_install_dir {0} +app_update 824360 validate ".
                         format(server_path)],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT,
                         shell=True,
                         bufsize=0)

    def quit(self):
        self.app.instance().quit()


class TaskThread(QThread):
    taskFinished = pyqtSignal()

    def __init__(self, task, param):
        super(TaskThread, self).__init__()
        self.task = task
        self.param = param

    def run(self):
        if not isinstance(self.param, list):
            self.task(self.param)
            self.taskFinished.emit()
        else:
            for command in self.param:
                self.task(command)
                self.taskFinished.emit()













