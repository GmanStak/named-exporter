import argparse, json

def get_args():
    parser = argparse.ArgumentParser(description='named export options!')
    parser.add_argument("-a","--ipaddress",type=str,default='localhost')
    parser.add_argument("-p","--port",type=int,default=9098)
    parser.add_argument("-c","--config",type=str,default="./conf/config.json")
    args = parser.parse_args()
    return args
