import queue



class huffman():
    def __init__(self, left = 0, right = 0):
        self.left = left
        self.right = right
    def children(self):
        return ((self.left, self.right))

def create_tree(frequense):
    ma = []
    string = 'a'
    for i in frequense:
        ma.append((i, string))
        string = chr(ord(string) + 1)
    p = queue.PriorityQueue()
    for i in ma:
        p.put(i)
    while p.qsize() > 1:
        l , r = p.get(), p.get()
        node = huffman(l,r)
        p.put((l[0] + r[0],node))
    return p.get()
def walk_tree(node, pref='',code={}):
    if isinstance(node[1].left[1], huffman):
        walk_tree(node[1].left,pref+"1", code)
    else:
        code[node[1].left[1]]=pref+"1"
    if isinstance(node[1].right[1],huffman):
        walk_tree(node[1].right,pref+"0", code)
    else:
        code[node[1].right[1]]=pref+"0"
    return(code)

def run():
    f = open("F:\\ut\\7\\data_trans\\prj2\\freq.txt",'r')
    text = f.readline()
    text = text[1:-1]
    text = text.split(',')
    base = create_tree(text)
    dic = {}
    dic = walk_tree(base, '', dic)
    print(dic)
run()

class convolotional():
    def __init__(self):
        self.state = 00
    def encode(self, string):
        output = ''
        for i in string:
            if i == '0' and self.state == 00:
                output += '00'
            elif i == '1' and self.state == 00:
                output += '11'
                self.state = 10

            elif i == '0' and self.state == 10:
                output += '11'
                self.state = 1
            elif i == '1' and self.state == 10:
                output += '00'
                self.state = 11

            elif i == '0' and self.state == 1:
                output += '10'
                self.state = 00
            elif i == '1' and self.state == 1:
                output += '01'
                self.state = 10

            elif i == '0' and self.state == 11:
                output += '01'
                self.state = 1
            elif i == '1' and self.state == 11:
                output += '10'
                self.state = 11
        return output
    def drived_from(self, state):
        if state == 0:
            return [(0,'00', '0'),(1,'10', '0')]
        if state == 1:
            return [(3,'01', '0'),(2,'11', '0')]
        if state == 2:
            return [(0,'11','1'),(1,'01', '1')]
        if state == 3:
            return [(3,'10', '1'),(2,'00', '1')]
    def calc_diff(self, st1, st2):
        r = 0
        if st1[0] != st2[0]:
            r += 1
        if st1[1] != st2[1]:
            r += 1
        return r
    def decode(self, string):
        res = ['','','','']
        matrix = [[0 for x in range(int(len(string)/2) + 1)] for y in range(4)]
        matrix[1][0] = 10000
        matrix[2][0] = 10000
        matrix[3][0] = 10000

        p = [string[i] + string[i+1] for i in range(0,int(len(string)),2)] 
        for i in range(1, len(p)+1):
            for j in range(4):
                status = self.drived_from(j)
                if self.calc_diff(p[i - 1], status[0][1]) + matrix[status[0][0]][i-1] < \
                    self.calc_diff(p[i - 1], status[1][1]) + matrix[status[1][0]][i-1]:
                    matrix[j][i] = self.calc_diff(p[i - 1], status[0][1]) + matrix[status[0][0]][i-1]
                    res[j] += status[0][2]
                else:
                    matrix[j][i] = self.calc_diff(p[i - 1], status[1][1]) + matrix[status[1][0]][i-1]
                    res[j] += status[1][2]
        for i in range(4):
            print(res[i] , matrix[i][-1])
s = convolotional()
print(s.encode('1110110110'))
(s.decode(s.encode('1110110110')))
