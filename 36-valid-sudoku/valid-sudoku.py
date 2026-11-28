class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        def box(x,y):
            xpos=(x//3)+1
            ypos=(y//3)+1
            e=(xpos,ypos)
            d={(1,1):1,(1,2):2,(1,3):3,(2,1):4,(2,2):5,(2,3):6,(3,1):7,(3,2):8,(3,3):9}
            return d[e]
        l=[[] for _ in range(9)]
        for i,x in enumerate(board):
            for j,y in enumerate(x):
                if y!='.':
                    l[box(i,j)-1].append(y)
                
        for i,x in enumerate(board):
            for j,y in enumerate(x):
                if y!=".":
                    if y in x[j+1:]:
                        return False
                    for p in range(i+1,len(board)):
                        if y in board[p][j]:
                            return False
                    if l[box(i,j)-1].count(y)>1:
                        return False
        return True