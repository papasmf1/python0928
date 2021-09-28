
class DemoClass:
    def union(self, *ar):
        result = []
        for item in ar:
            for x in item:
                if x not in result:
                    result.append(x)
        return result 


#인스턴스 
d = DemoClass()
print( d.union("HAM", "EGG") )
print( d.union("HAM", "EGG", "SPAM") )