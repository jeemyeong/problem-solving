# class IF{
#   public IF(Iterator<T>[] iterlist){
#   }
#   public T next(){
#   }
  
#   public boolean hasNext(){
#   }
# }
arr1 = [1, 2, 3];
arr2 = [4, 5];
arr3 = [6, 7, 8, 9];
iterlist = [arr1.__iter__(), arr2.__iter__(), arr3.__iter__()]

class IF:
    def __init__(self, iterlist):
        self.iterlist = iterlist
        self.len = len(iterlist)
        self.t = 0
    
    def next_lst(self):
        if self.t < self.len-1:
            self.t += 1
        else:
            self.t = 0

    def next(self):
        self.next_lst(self)
        cnt = 0
        while !iterlist[self.t].has_next():
            if cnt > self.len:
                raise Exception("StopIteration")
            cnt+= 1
            self.next_lst(self)
        return next(iterlist[self.t])
            
    def hasNext():
        cnt = 0
        while !iterlist[self.t].has_next() and cnt < self.len:
            cnt += 1
        return cnt != self.len

        

_if = IF(iterlist)
print(_if)