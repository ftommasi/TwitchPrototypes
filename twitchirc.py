import socket 


class TwitchIRC:
  def __init__(self,channel="roflstompee"):
    #setting up class vars
    self.base_url = "irc.twitch.tv"
    self.port = 6667
    self.oath_pass = "oauth:lewvrjhk9u7qcipp8ka3d6w2tne6xk"
    self.nickname = "LucioBot"
    self.channel = channel

    #setting up socket
    self.socket = socket.socket
    self.socket.bind(self.base_url,self.port)
     
    #connecting to host 
    self.join()

  def write(self,msg):
    self.socket.send(msg)

  def join(self):
    self.write("PASS {}".format(self.oath_pass))
    self.write("NICK {}".format(self.nickname))
    self.write("USER {} 0 * {}".format(self.nickname,self.nickname))
    self.write("JOIN #{}".format(self.channel))
  
  def chat(self,msg):
    self.write("PRIVMSG #{} : {}".format(self.channel,msg))


  def __str__(self):
    return "TwitchIRC Object\n  base_url: {}\n  port: {}\n  pass: {}\n     nick: {}\n  channel: {}\n".format(self.base_url,self.port,self.oath_pass,self.nickname,self.channel)
