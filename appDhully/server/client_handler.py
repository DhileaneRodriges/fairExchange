from appDhully.server.files2sockets import read_send_file
import os

class ClientHandler:
  """
  Thread handler leaves the main thread free to
  handle any other incoming connections
  """

  def __init__(self, conn, conf):

    self.conn = conn
    self.conf = conf
    self.ser_fileName = self.conf.ser_fileName
    print("\n\n\n...........ser_fileName:", self.ser_fileName)

  def start(self):
    try:
      # Read up to 1024 bytes from the client
      ###client_req = self.conn.recv(1024)
      ###print("Rcvd from cli_str.py ", client_req.decode("UTF-8").rstrip())
      """ 
      11 sep 2023
      received= self.conn.recv(BUFFER_SIZE).decode()
      filename, filesize= received.split(SEPARATOR)

      # remove filename path if any
      filename= os.path.basename(filename)
      filename= RECV_FILE_NAME_PREFIX + filename
      filesize= int(filesize)
      # start receiving the file from the socket
      # and writing to the file stream


      ########## server will receive from client ########
      recv_store_file(filename, filesize, BUFFER_SIZE, self.conn)
      print("ser_file_file.py server has read file from socket....")
      11 sep 2023 
      """

      cli_req = self.conn.recv(1024)
      print("client request: ", cli_req.decode("UTF-8"))

      ########## server will send file to client ########
      # experimenting with marco.txt file stored on current subdir
      filename = self.ser_fileName
      filesize = os.path.getsize(filename)
      # In python sockets send and receive strings. Send a string
      self.conn.send(f"{filename}{self.conf.EPARATOR}{filesize}".encode())
      read_send_file(filename, filesize, BUFFER_SIZE, self.conn)
      print("ser_file_file.py has sent a file to cli_file)flie.py")

      # print("ser_str.py will now send a string to cli_str.py")
      # You are responsible for converting any data into bytes strings
      # self.conn.send(b"2nd: I'm here cli_str.py\n")

    except ssl.SSLError as e:
      print(e)
    except Exception as e:
      print(e)
    finally:
      self.conn.close()
      print("ser_str.py has closed the socket")