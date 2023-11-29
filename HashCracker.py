import _sha1

# hashInput = input('Enter the password\'s hash here: ')
# pwdFile = open('smalldict.txt', 'r')
# pwdFile.close()


def crackPass():
    hashInput = input('Enter the password\'s hash here: ')
    pwdFile = open('smalldict.txt', 'r')
    count = 1
    for pwd in pwdFile.readlines():
        pwd = pwd.strip('\n')
        hashes = _sha1.sha1(b'pwd')
        hashes.hexdigest()
        # hashList = hashes.split()


        # hackFile = open('Hack_Result.txt', 'w')
        # hackFile.write(str(pwd.strip()))

        print('[*] Trying password #%s: %s' % (count, pwd.strip()))
        count += 1
        if hashInput == hashes.hexdigest():
            print('[*] Password found.')
            print('\nPassword is %s' % pwd)
            return

    print("[-] Hack failed")
    return
            # print(hashes.hexdigest())
            # quit()
            # print(pwd)
            # hackFile.close()

# def main():
#    hashInput = input('Enter the password\'s hash here: ')
#    crackPass()


def main():
    crackPass()


if __name__ == '__main__':
    main()
