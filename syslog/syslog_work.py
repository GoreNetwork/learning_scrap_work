import socket

"""get splunk container working with 
docker run -d -p 8000:8000 -p 514:514 -p 514:514/udp -e "SPLUNK_START_ARGS=--accept-license" -e "SPLUNK_PASSWORD=password" --name splunk splunk/splunk:latest

then splunk app Cisco Network Assurance Engine Add-on for Splunk Enterprise
then make a new settings/data input, udp port 514.
https://www.youtube.com/watch?v=ZIXonhcpz3g

"""

class Facility:
  "Syslog facilities"
  KERN, USER, MAIL, DAEMON, AUTH, SYSLOG, \
  LPR, NEWS, UUCP, CRON, AUTHPRIV, FTP = range(12)

  LOCAL0, LOCAL1, LOCAL2, LOCAL3, \
  LOCAL4, LOCAL5, LOCAL6, LOCAL7 = range(16, 24)

class Level:
  "Syslog levels"
  EMERG, ALERT, CRIT, ERR, \
  WARNING, NOTICE, INFO, DEBUG = range(8)

class Syslog:
  """A syslog client that logs to a remote server.

  Example:
  >>> log = Syslog(host="foobar.example")
  >>> log.send("hello", Level.WARNING)
  """
  def __init__(self,
                #This is my docker server with splunk running
               host="192.168.0.117",
               port=514,
               facility=Facility.DAEMON):
    self.host = host
    self.port = port
    self.facility = facility
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

  def send(self, message, level):
    "Send a syslog message to remote host using UDP."
    data = "<%d>%s" % (level + self.facility*8, message)
    print (type(self.host), type(self.port))
    self.socket.sendto(data.encode('utf-8'), (self.host, self.port))

  def warn(self, message):
    "Send a syslog warning message."
    self.send(message, Level.WARNING)

  def notice(self, message):
    "Send a syslog notice message."
    self.send(message, Level.NOTICE)

  def error(self, message):
    "Send a syslog error message."
    self.send(message, Level.ERR)

log = Syslog()
log.send("howdy", Level.WARNING)