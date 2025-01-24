#[0x0, 0xd, 0x6, 0x5, 0x7, 0x0, 0xc, 0x4, 0xb, 0x1, 0xA, 0xf, 0x3, 0x9, 0x2]。

if __name__ == '__main__':

    for i in range(16):
        x = list(map(int, bin(i)[2:].rjust(4, '0')))  # x3存储在x[0]，即x3 x2 x1 x0存储在x[0-3]上
        # print(x)
        x = x[::-1]  # 逆序
        # print(x)

        t = [0] * 104
        y = [0] * 22
        z = [0] * 18
        s = [0] * 8

        t[1] = x[2] & x[1]
        t[2] = x[2] ^ x[1]
        t[3] = x[3] ^ t[1]
        t[4] = x[0] ^ t[2]
        t[5] = t[3] | t[4]
        # 这里多弄一个量子位
        t[6] = x[1] ^ t[5]
        t[7] = t[4] | x[1]
        t[8] = t[3] | t[7]
        t[9] = t[2] & t[4]
        t[10] = x[3] ^ t[8]
        t[11] = t[9] | t[10]
        t[12] = t[3] ^ t[4]
        t[13] = x[3] & t[12]
        t[14] = t[9] ^ t[13]
        t[15] = t[6] | t[13]
        t[16] = x[2] ^ t[12]
        t[17] = t[16] ^ 1
        t[18] = t[15] ^ t[17]

        s[0] = t[6]
        s[1] = t[14]
        s[2] = t[11]
        s[3] = t[18]


        result = str( str(s[3]) + str(s[2]) + str(s[1]) + str(s[0]))


        #result = str(str(s[1]) + str(s[2]) + str(s[3]) + str(s[0]))
        output = "".join(list(map(str, result)))
        print(hex(int(output, 2))[2:].rjust(2, '0'), end=" ")
        if i % 16 == 15:
            print()

