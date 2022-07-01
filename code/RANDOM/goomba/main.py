def goomba_stomp():
    print("Goomba has been stomped rip")
    
def goomba_stun():
    print("Goomba has been stunned")

def galoomba_stomp():
    print("Galoomba has been stomped rip")
    
def galoomba_stun():
    print("Galoomba has been stunned")

class GoombaArray:
    def __init__(self, size=100):
        self.size = size
        self.graph = {} 
        self.player_items = []  
    
    def createPlayArena(self, graph_input):
        graph = {}
        for i in range(1, self.size):
            if i in graph_input:
                graph[i] = graph_input.get(i) 
            else:
                graph[i] = None 
        self.graph = graph 


    def begin(self):
        for i in self.graph.items():
            self.do_action(i[0], i[1])

        if(all(None is x for x in list(self.graph.values()))): 
            return
        else:
            self.play_items()
            self.begin() 
                
    def play_items(self): 
        for item in self.player_items:
            item.perform_action() 
                

    def do_action(self, block, goomba):
        if(goomba == None):
            return  
        else:
            try:
                res = self.graph[block]()
                try:
                    if(res.__name__() is Item.__name__):
                        self.player_items.append(res)
                except:
                    pass 
            except Exception as E: 
                print(E)
                self.graph[block] = None  
        
        
class Goomba:
    def __init__(self, state, f1, f2):
        self.state = state  
        self.f1 = f1
        self.f2 = f2
        
    def stomp(self):
        self.f1() 
        return None 
        
    def stun(self):
        self.f2() 
        return self 
    
    def __call__(self):
        res = 0 
        if(self.state == 1):
            res = self.stun()
        elif(self.state == 0):
            res =self.stomp() 
        elif(self.state < 0):
            del self 
        self.state -= 1;
        return res
    
    
class StunableGoomba(Goomba):
    def __init__(self, *args, stuns):
        Goomba.__init__(self, *args)   
        self.extra_stuns = stuns 
    def stun(self):
        if(self.extra_stuns > 0):
            self.state +=1
            self.extra_stuns -= 1
        self.f2() 
        return self 
            
class Galoomba(Goomba):
    def __init__(self, *args, flight):
        Goomba.__init__(self, *args)   
        self.flight = flight 
    def __call__(self):
        if(self.flight > 0):
            self.flight -= 1
        else:
            super().__call__()
            

class Item():
    def __init__(self, *args):
        self.item = args  
        
    def perform_action(self):
        pass 


class FlippableGoombaItem(Item):  
    def __init__(self, *args):
        Item.__init__(self, *args)  

    def perform_action(self):
        print("PERFORMING FLIPPABLE GOOMBA ITEM")  
        
    def __name__(self):
        return (self.__class__.__base__).__name__
    
    
    
    
         
            
class FlippableGoomba(Goomba):
    def __init__(self, *args,):
        Goomba.__init__(self, *args)  
    def stomp(self):
        self.f2() 
        FGI = FlippableGoombaItem(None) 
        return  FGI
    
                
GA = GoombaArray() 

g1 = Goomba(7, goomba_stomp, goomba_stun) 
g2 = StunableGoomba(7, goomba_stomp, goomba_stun, stuns=10) 
g3 = Goomba(2, goomba_stomp, goomba_stun) 
g4 = Galoomba(2, galoomba_stomp, galoomba_stun, flight=5) 
g5 = FlippableGoomba(20, galoomba_stomp, galoomba_stun) 


goombaGraph = {1: g1, 2: g2, 3: g3, 5:g4, 6:g5}

GA.createPlayArena(goombaGraph)
GA.begin() 