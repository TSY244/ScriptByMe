import scapy.all as scapy 
import re
import argparse
import sys
import signal

def check_ip(ip):
    # 检查是否是合法的ip
    if not re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ip):
        print("Invalid IP address!")
        return False
    # 检查范围
    ips = list(map(int, ip.split(".")))
    for i in ips:
        if i < 0 or i > 255:
            print("Invalid IP address!")
            return False
    return True

def create_parser():
    parser = argparse.ArgumentParser(description="TCP port scanning")
    parser.add_argument("-r", "--range", dest="range", help="range of port")
    parser.add_argument("-i", "--ip", required=True, dest="ip", help="ip address")
    parser.add_argument("-a", "--all", action="store_true", dest="all_ips", help="all ips")
    return parser

def command_line_args(args):
    parser = create_parser()
    if len(args) == 0:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args(args)
    # 检查是否输入了参数
    if args.ip is None:
        parser.print_help()
        sys.exit(1)
    # 检查ip是否合法
    if not check_ip(args.ip):
        sys.exit(1)
    # 获取输入的参数
    ip = args.ip
    # 端口范围匹配
    if args.range is None and args.all_ips is None:
        begin_port = 1204
        end_port = 65535
    elif args.range:  # 匹配端口范围
        begin_port, end_port = map(int, args.range.split("-"))
        if begin_port > end_port or begin_port < 0 or end_port > 65535:
            print("Invalid port!")
            sys.exit(1)
    elif args.all_ips:    # 如果输入了all
        begin_port = 0
        end_port = 65535
    else:
        print("Invalid port!")
        sys.exit(1)
    return ip, begin_port, end_port

def scan(ip, begin_port, end_port):
    scapy.conf.verb = 0  # 不显示发送的包的信息
    # 打印扫描的信息
    print("Scanning {} from {} to {}".format(ip, begin_port, end_port))
    # 循环发包
    for port in range(begin_port, end_port + 1):
        pkg = scapy.IP(dst=ip) / scapy.TCP(dport=port, flags="S") # 构造包
        ans, unans = scapy.sr(pkg)
        # 是否回复
        if ans.res:
            print("The port {} is open!".format(port))
        

        # res = str(ans[0]) # 获取回复的包
        # if re.findall(r"SA", res): # 如果收到了回复
        #     print("The port {} is open!".format(begin_port)) # 打印开放的端口

def signal_handler(signal, frame):
    print("Ctrl+C detected, exiting...")
    sys.exit(0)

def main(args):
    ip, begin_port, end_port = command_line_args(args)
    # 创建线程处理ctrl+c
    signal.signal(signal.SIGINT, signal_handler)
    # 开始扫描
    scan(ip, begin_port, end_port)

if __name__ == "__main__":
    main(sys.argv[1:])

