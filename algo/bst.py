class BST(object):
    def __init__(self,value):
        self._l = None
        self._r = None
        self.root = value
        self._len = 1
        self.children = 0


    def __iter__(self):
        if self._l:
            yield from self._l
        yield self.root
        if self._r:
            yield from self._r
  

    def _get_next(self):
        if self._r:
            yield from self._r

    def add(self,value):
        self._len += 1
        if value > self.root:
            if self._r:
                self._r.add(value)
            else:
                self._r = BST(value)
                self.children += 1
        if value < self.root:
            if self._l:
                self._l.add(value)
            else:
                self._l = BST(value)
                self.children += 1
    
    def remove(self,value):
        if value in self:
            self._len -= 1
            if self._l and self._l.children == 0 and value == self._l.root  :
                self._l = None
                return
            if self._r and self._r.children == 0 and  value == self._r.root  :
                self._r = None
                return
            if value == self.root:
                if self.children == 1:
                    if self._l:
                        self.root = self._l.root
                        self.children -= 1
                        self._l = None
                        return
                    if self._r:
                        value = self._r.root
                        self.children -= 1
                        self._r = None
                        return
                if self.children == 2:
                    i = next(self._get_next())
                    self.remove(i)
                    self.root = i
                    return
            if value > self.root:
                self._r.remove(value)
            if value < self.root:
                self._l.remove(value)
        else:
            raise ValueError

    def __repr__(self):
        return self.root

    def __len__(self):
        return self._len

    def __contains__(self,item):
        if self.root == item:
            return True
        else:
            if item < self.root:
                if self._l:
                    return item in self._l
                else:
                    return False
            if item > self.root:
                if self._r:
                    return item in self._r
                else:
                    return False

bst = BST(20)

bst.add(10)
bst.add(24)
bst.add(4)
bst.add(100)
bst.add(33)
bst.add(22)
bst.add(21)
bst.add(23)


for i in bst:
    print( i)
print(f"lenght of bst: {len(bst)}")
bst.remove(10)
bst.remove(24)
bst.remove(4)
bst.remove(100)
bst.remove(33)
bst.remove(22)
bst.remove(21)
bst.remove(23)

print("\n")
for i in bst:
    print( i)


print(f"4 in bst:{4 in bst}")
print(f"5 in bst:{5 in bst}")
print(f"33 in bst:{33 in bst}")

print(f"lenght of bst: {len(bst)}")