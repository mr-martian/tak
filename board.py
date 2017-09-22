WHITE = 4
STAND = 2
ISCAP = 1
numpiece = [0, 0, 0, 10, 15, 22, 31, 0, 52]
def rot(board):
    return [list(x) for x in list(zip(*board[::-1]))]
    #https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
class board:
    def __init__(self, board):
        self.board = board
    def __eq__(self, other):
        a = other.board
        af = a[::-1]
        b = rot(a)
        bf = b[::-1]
        c = rot(b)
        cf = c[::-1]
        d = rot(c)
        df = d[::-1]
        s = self.board
        if s == a or s == af or s == b or s == bf or s == c or s == cf or s == d or s == df:
            return True
        return False
    def istoe(self):
        empty = 0
        bo = self.board
        ln = len(bo)
        w = [[False]*ln]*ln
        b = [[False]*ln]*ln
        wf, bf = 0, 0
        wc, bc = 0, 0
        for i in range(ln):
            for j in range(ln):
                s = bo[i][j]
                print([s, s==[]])
                if s == []:
                    empty += 1
                elif s[0] & WHITE and not s[0] & STAND:
                    w[i][j] = True
                    wf += 1-(s[0] & ISCAP)
                elif not s[0] & WHITE and not s[0] & STAND:
                    b[i][j] = True
                    bf += 1-(s[0] & ISCAP)
                for k in s:
                    if k & WHITE:
                        wc += 1
                    else:
                        bc += 1
        if empty == ln*ln:
            return "empty"
        bols = [w, rot(w), b, rot(b)]
        for k in range(4):
            for i in range(1, ln):
                passln = bols[k][i-1]
                thisln = bols[k][i]
                for j in range(ln):
                    if not thisln[j]:
                        passln[j] = False
                ch = True
                while ch:
                    ch = False
                    if not passln[0] and thisln[0] and passln[1]:
                        passln[0] = True
                        ch = True
                    if not passln[-1] and thisln[-1] and passln[-2]:
                        passln[-1] = True
                        ch = True
                    for j in range(1, ln-1):
                        if not passln[j]:
                            if thisln[j] and (passln[j-1] or passln[j+1]):
                                passln[j] = True
                                ch = True
            if True in bols[k][-1]:
                bols[k] = True
            else:
                bols[k] = False
        wv = bols[0] or bols[1]
        bv = bols[2] or bols[3]
        if wv and bv:
            return "double toe"
        if wv:
            return "white toe"
        if bv:
            return "black toe"
        if empty == 0 or wc == numpiece[ln] or bc == numpiece[ln]:
            if wf > bf:
                return "white flat"
            if bf > wf:
                return "black flat"
            return "tie"
        return False
if __name__ == '__main__':
    print("hi!")
    x = board([[[4], [4], [4]], [[], [], []], [[], [], []]])
    print(x.istoe())

