class Queue:
    def __init__(self):
        self.first=None
        self.last=None
        self.size=0
    
    def add(self, node):
        if(self.first!=None):
            self.last.before = node
            node.next=self.last
            self.size+=1
            self.last=node
            return True
        self.first=self.last=node
        self.size+=1
        return True
    
    def get(self):
        if(self.size>1):
            nodeFirst = self.first
            self.first.before.after = None
            self.first=self.first.before
            self.size-=1
            return nodeFirst