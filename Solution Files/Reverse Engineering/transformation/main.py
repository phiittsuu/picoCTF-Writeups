def main():
    enc = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸形㝦㘲捡㕽"
    flag = ''.join([chr(ord(c) >> 8) + chr(ord(c) & 0xFF) for c in enc])
    print(flag)

if __name__ == "__main__":
    main()