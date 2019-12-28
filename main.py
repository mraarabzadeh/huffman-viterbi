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
    def __init__():
        self.state = 00
    def encode(self, string):
        