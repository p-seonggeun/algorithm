import sys
sys.setrecursionlimit(10**7)
def solution(nodeinfo):
    answer = [[]]
    pre = []
    post = []
    for index, i in enumerate(nodeinfo) :
        i.insert(0, index + 1)
    
    nodeinfo.sort(key = lambda x : (-x[2], x[1]))
    
    def predivide(node) :
        node.sort(key = lambda x : (-x[2], x[1]))
        left = []
        right = []
        mid = node[0]
        pre.append(mid[0])
        for index, i in enumerate(node) :
            if index == 0 :
                continue
            if i[1] > mid[1] :
                right.append(i)
            elif i[1] < mid[1] :
                left.append(i)
        return left, right
    
    def preorder(node) :
        if len(node) <= 1 :
            if node :
                pre.append(node[0][0])
            return  
        else :
            left, right = predivide(node)
            preorder(left)
            preorder(right)
    
    def postdivide(node) :
        node.sort(key = lambda x : (-x[2], x[1]))
        left = []
        right = []
        mid = node[0]
        for index, i in enumerate(node) :
            if index == 0 :
                continue
            if i[1] > mid[1] :
                right.append(i)
            elif i[1] < mid[1] :
                left.append(i)
        return left, right
    
    def postorder(node) :
        if len(node) <= 1 :
            if node :
                post.append(node[0][0])
            return True
        else :
            left, right = postdivide(node)
            postorder(left)
            postorder(right)
            post.append(node[0][0])
    
    preorder(nodeinfo)
    postorder(nodeinfo)
    
    answer = [pre, post]
            
    return answer