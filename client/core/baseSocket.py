import socket, ssl
from core.config import Settings
from core.syslog import Syslog
from core import utils


# from utils import *

class BaseSocket(object):
    """docstring for Client."""
    def __init__(self, **arg):
        super(BaseSocket, self).__init__()
        self.msgCode = ('login','logout','refresh','list','get','put')
        self.userName = None
        self.passWord = None
        self.host = None
        self.port = None

        self.sslContext = None

        self.SEND_BUFFER_SIZE = 1024

        self.ctrlSock = None
        self.ctrlSockPort = None

        self.dataSock = None
        self.dataSockPort = None

        self.recvInfo = None
        self.lastCmd = None
        self.lastCmdCode = None
        self.certInfo = None

        if arg:
            self.__dict__.update(arg)

        self.log = Syslog()
        self.settings = Settings()
        self.createSslConttext()
        self.createConnection()

    def createConnection(self):
        self.log.info('start createConnection')
        try:
            tmpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.ctrlSock = self.sslContext.wrap_socket(tmpSock, server_hostname = self.host)
            self.ctrlSock.connect((self.host, int(self.port)))
        except Exception as e:
            self.log.info(str(e))
            # raise
        else:
            self.certInfo = str(self.ctrlSock.cipher())
            self.log.info('connecting to remote host ...')

    def createSslConttext(self):
        self.sslContext = ssl.create_default_context()
        certFileName = "{}.crt".format(self.host)
        certFilePath = utils.joinFilePath(self.settings.certificates.certdirs, certFileName)

        if not utils.checkFileExists(certFilePath):
            self.acquire_remote_cert()

        try:
            self.sslContext.load_verify_locations(certFilePath)
        except Exception as e:
            self.log.error(str(e))

    def createDataSock(self):
        self.dataSock = self.ctrlSock

    def acquire_remote_cert(self):
        self.log.info('start acquire remote host cert')
        try:
            cert = ssl.get_server_certificate((self.host, self.port))
        except Exception as e:
            self.log.info('can\' t load remote certificate :{}'.format(str(e)))
            return (1, str(e))
        certFileName = "{}.crt".format(self.host)
        certFilePath = utils.joinFilePath(self.settings.certificates.certdirs, certFileName)
        try:
            with open(certFilePath, 'w') as f:
                f.write(cert)
        except Exception as e:
            self.log.info('can\' t save remote certificate on local :{}'.format(str(e)))
            return (1, str(e))
        else:
            self.log.info('load and save remote server cert successd')
            return (0, 'ok')

    def sendFile(self):
        with open(self.filepath, 'rb') as f:
            try:
                sendSize = self.ctrlSock.sendfile(f)
            except Exception as e:
                self.log.info('send file fails : {}'.format(str(e)))
            else:
                self.log.info('send file Successd')
            finally:
                self.log.info('total send size is :{:.2f} M'.format(sendSize / 1024))

    def recvFile(self):
        self.log.info('######## start recv file ########')
        loop = int(self.fileSize) // 1024
        extend = int(self.fileSize) % 1024
        with open(self.saveFilePath, 'wb') as f:
            recvedFileSize = 0
            for i in range(loop):
                recvfile = self.dataSock.recv(1024)
                # self.log.info('receving data of file is : {:.2f}%'.format(recvedFileSize / filesize * 100))
                f.write(recvfile)
                self.log.info('start recv {} loop'.format(i))
                self.log.info('this task need to loop {}, the last info size of info is : {}'.format(loop, extend))
                self.signal.recv.emit(1)
                self.log.info('emit 1')

                recvedFileSize += len(recvfile)
                # self.dataSock.send(b'1') # receiving file
            recvfile = self.dataSock.recv(extend)
            f.write(recvfile)
            self.signal.recv.emit(0)
        # self.log.info('save size:{}/ file size:{}'.format(os.path.getsize(self.saveFilePath), self.downloadFileInfo['size']))
        if utils.calculateHashCodeForFile(self.saveFilePath) == self.fileHashCode:
            # self.sslDataSock.send(b'0') # recv finished
            self.log.info('download file finished')
            return (0, 'ok')
        else:
            # self.sslDataSock.send(b'2') # size not match
            return (1, 'size not match')

    def checkCmdCode(func):
        def wrapper(self):
            res = func(self)
            if self.recvInfo['code'] != self.lastCmdCode:
                self.log.info('lastCmdCode is not same, login fails')
            return res
        return wrapper

    def setupCmdCode(func):
        def wrapper(self, msg):
            self.lastCmdCode = str(utils.generateRandomDigitFromRange(10000, 99999))
            # print('*********** send msg len is :{},type is {}, info is {}'.format(len(msg),type(msg),msg))
            msg['code'] = self.lastCmdCode
            return func(self, msg)
        return wrapper

    def fillSnedMsg(func):
        def wrapper(self, msg):
            msg = str.encode(str(msg))
            fillSize = self.SEND_BUFFER_SIZE - len(msg)
            msg = b''.join((msg, b' ' * fillSize))
            # print('resize send msg len is :{},type is {}, info is {}'.format(len(msg),type(msg),msg))
            return func(self, msg)
        return wrapper

    @setupCmdCode
    @fillSnedMsg
    def sendMsg(self, msg):
        self.lastCmd = msg
        try:
            self.ctrlSock.send(msg)
        except Exception as e:
            return (1, str(e))
        else:
            self.log.info('send info : {}'.format(msg.strip()))
            # self.log.info('###########{}##########'.format(msg))
            return (0, "ok")

    @checkCmdCode
    def recvMsg(self):
        try:
            recvInfo = self.ctrlSock.recv(1024).strip()
        except Exception as e:
            return (1, str(e))
        else:
            self.recvInfo = utils.rebuildDictFromBytes(recvInfo)
            self.log.info('recv info {}'.format(recvInfo.strip()))
            return (0, "ok")

    def recvMark(self):
        try:
            recvInfo = self.ctrlSock.recv(1).strip()
        except Exception as e:
            self.log.info(' recv upload file transfer mark error : {}'.format(str(e)))
        else:
            # self.recvInfo = literal_eval(recvInfo.decode('utf8'))
            # self.log.info('recv info {}'.format(recvInfo.strip()))
            return recvInfo
    def logout(self):
        pass

    def reconnect(self):
        pass

    def close(self):
        self.ctrlSock.shutdown(socket.SHUT_RDWR)
        self.ctrlSock.close()

    @staticmethod
    def test():
        print('host')




# clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# clientSocket.connect(("127.0.0.1", 2333))
#
# f = open('./tmp/1.jpg','rb')
# print('start Sending...')
# l = f.read(1024)
# while (l):
#     print('Sending...')
#     clientSocket.send(l)
#     l = f.read(1024)
# f.close()
# clientSocket.close()
