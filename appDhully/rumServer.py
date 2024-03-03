import os
import time
from appDhully.server.server.serverModule import Module
from appDhully.server.client.serverClient import SSLclientfile
from appDhully.alice.Configurations import ConfigsAlice


def main():
   Module(ConfigsAlice())



if __name__ == '__main__':
   main()