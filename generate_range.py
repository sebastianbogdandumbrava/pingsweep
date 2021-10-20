import sys

init_ip = sys.argv[1][0]
ip_range = []
ip = sys.argv[1] 

def contains_wildcard(ip):
    for c in ip:
        if c == '*':
            return True

    return False

def list_init():
    ip_split = ip.split('.')
    template = [[], [], [], []]

    for num in range(4):
        if ip_split[num] == '*':
            template[num] = range(256)
        else:
            template[num] = ip_split[num]

    for num1 in template[0]:
        for num2 in template[1]:
            for num3 in template[2]:
                for num4 in template[3]:
                    ip_range.append(str(num1) + '.' + str(num2) + '.' + str(num3) + '.' + str(num4))
    return

            

def main():
    
    if contains_wildcard(ip):
        print("test")
        list_init()
        
        for elem in ip_range:
            print(elem)
    else:
        print(ip)
        #singleton_init()
        
    return


main()
    
