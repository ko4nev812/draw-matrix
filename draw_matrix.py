




def test():
    
    t = Сanvas_matrix(10,25)
    
    t.local_draw = [7,0]
    t.makeline(0, 0, 4, 2)
    t.makeline(20, 2)
    t.makeline(25, -1)
    t.local_draw = [2,4]
    t.point(0,0)
    t.point(10,-1)
    
    t.beautify()
    
    t.pt(False)





class Сanvas_matrix:
    def __init__(self, n, k, h=' ') -> None:
        self.n=n
        self.k=k
        self.s = [[h]*self.k for i in range(self.n)]
        self.fill = "*"
        self.local_draw = [0,0]
        self.makeline_pred=[0,0]


    def pt(self, pt = False):
        for i in self.s:
            print(*i, sep='')
        if pt:
            print("-"*self.n)
    
    
    def ygl(self, rup=False, rdown=False, lup=False, ldown=False):
        if rup: self.s[self.n-1][0] = rup
        if rdown: self.s[self.n-1][self.k-1] = rdown
        if lup: self.s[0][0] = lup
        if ldown: self.s[0][self.k-1] = ldown
    

    def diag(self, fill=1, ang = 0):
        if ang ==0:
            for i in range(self.k):
                for j in range(self.n):
                    if i ==j:
                        self.s[j][i] = fill
        elif ang ==1:
            for i in range(self.k):
                for j in range(self.n):
                    if i +j == self.k-1:
                        self.s[j][i] = fill
    def fille(self, fill=1, ang1 =0, ang2=0):
        
        if ang1 ==0:
            for i in range(self.k):
                for j in range(self.n):
                    if ang2 == 0:
                        if i > j:
                            self.s[j][i] = fill
                    elif ang2 == 1:
                        if i < j:
                            self.s[j][i] = fill

        elif ang1 ==1:
            for i in range(self.k):
                for j in range(self.n):
                    if ang2 == 0:
                        if i +j > self.k-1:
                            self.s[j][i] = fill
                    elif ang2 == 1:
                        if i +j < self.k-1:
                            self.s[j][i] = fill
    def line(self, p1x, p1y, p2x, p2y):
        p1x, p1y, p2x, p2y =p1x-1, p1y-1, p2x-1, p2y-1
        for i in range(self.k):
            for j in range(self.n):
                if p1x<=i<=p2x and p1y<=j<=p2y:
                    self.s[j][i] = self.fill
    
    
    def localx(self, n):
        self.local_draw[0]+=n
    
    def localy(self, n):
        self.local_draw[1]+=n

    
    def point(self,x,y, r=2):
        for i in range(r):
            for j in range(r):
                self.s[self.local_draw[0]+y+i][self.local_draw[1]+x+j]=self.fill

    

    def makeline(self, p1x, p1y, p2x=None, p2y=None):
        if p2x == None:
            p1x,p2x=self.makeline_pred[0],p1x
        if p2y == None:
            p1y,p2y=self.makeline_pred[1],p1y
        self.makeline_pred=[p2x, p2y]

        point1, point2 =[p1x-1, p1y-1], [p2x-1, p2y-1]
    
        
        history = []

        x1, y1 = point1
        x2, y2 = point2
        pred = [x1,y1]
        
        dx = x2 - x1
        dy = y2 - y1
        
        sx = 1 if dx > 0 else -1
        sy = 1 if dy > 0 else -1
        
        dx = abs(dx)
        dy = abs(dy)
        
        x = x1
        y = y1
        
        error = dx - dy
        while True:
            if not [x,y] in history:
                self.s[self.local_draw[0]+y][self.local_draw[1]+x] = self.fill
                if (pred[0]-x!=0) and (pred[1]-y!=0):
                    self.s[self.local_draw[0]+y+pred[1]-y][self.local_draw[1]+x]=self.fill

                pred = [x,y]
                history.append([x,y])
            if (x, y) == (x2, y2):
                break
            e2 = 2 * error
            if e2 > -dy:
                error -= dy
                x += sx
            if e2 < dx:
                error += dx
                y += sy
    
    def beautify(self):
        mat = [
            ['1111', "╬"],
            ['1100', "║"],
            ['0011', "═"],
            ['0101', "╔"],
            ['0110', "╗"],
            ['1001', "╚"],
            ['1010', "╝"],
            ['1101', "╠"],
            ['1110', "╣"],
            ['0111', "╦"],
            ['1011', "╩"],
            ['0001', "╞"],
            ['0010', "╡"],
            ['0100', "╥"],
            ['1000', "╨"],
            ['0000', "▪"]
        ]
        rows, cols = len(self.s), len(self.s[0])
        plan = []
        for i in range(rows):
            for j in range(cols):
                if self.s[i][j] == self.fill:
                    top = self.s[i - 1][j] if i > 0 else '@'
                    bottom = self.s[i + 1][j] if i < rows-1 else '@'
                    left = self.s[i][j - 1] if j > 0 else '@'
                    right = self.s[i][j + 1] if j < cols - 1 else '@'
                    for m in mat:
                        if (top == self.fill)==int(m[0][0]) and (bottom == self.fill)==int(m[0][1]) and (left == self.fill)==int(m[0][2]) and (right == self.fill)==int(m[0][3]):
                            plan.append([i,j,m[1]])
                            break
        
        for p in plan:
            self.s[p[0]][p[1]]=p[2]


if __name__ == "__main__":
    test()
    while True: None