

import time
import os
from threading import Thread

from threading import Lock
clear = lambda: os.system('cls')
lock = Lock()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self, new_data):
        self.data = new_data
    def set_next(self, new_next):
        self.next = new_next
    def __str__(self):
        return self.data
 
    """allows the linked list to be iterated through, to validate usernames/passwords"""
class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item = self.current.get_data()
            self.current = self.current.get_next()
            return item

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        return LinkedListIterator(self.head)
    def add(self, item): 
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node
    

class Credential(LinkedList):
    def __init__(self):
        return self
    def add(self, item): 
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node

    usernames = LinkedList()       
    passwords = LinkedList()
    """assigning usernames to a linked list"""        
    usernames.add("user1")
    usernames.add("user2")
    usernames.add("user3")
    usernames.add("user4")
    usernames.add("user5")
    usernames.add("user6")
    usernames.add("user7")
    usernames.add("user8")
    usernames.add("user9")
    usernames.add("user10")
    """assigning passwords to a seperate linked list"""
    passwords.add("pass1")
    passwords.add("pass2")
    passwords.add("pass3")
    passwords.add("pass4")
    passwords.add("pass5")
    passwords.add("pass6")
    passwords.add("pass7")
    passwords.add("pass8")
    passwords.add("pass9")
    passwords.add("pass10")

    """searches a linked list for a key word using linear search, then returns it's position in the list, 
    this ensures that usernames and passwords are in the same position in their corresponding linked lists"""
    def indexSearch(self, key):
        count = 0
        for i in self:
            if key != i:
                count +=1
            if key == i:
                return count
                    
class Graph:  
    def __init__(self, VE):  
        self.VE = VE  
        self.ed = []  
        self.Alist = {v: [] for v in VE}  
        
    """Kruskal's Algorithm"""    
    def addEdge(self, u, v, weight):  
        self.ed.append((u, v, weight))  
        self.Alist[u].append((v, weight))  
        self.Alist[v].append((u, weight))  

    def find_parent(self, parent, i):  
        if parent[i] == i:  
            return i  
        return self.find_parent(parent, parent[i])  
  
    def union(self, parent, rank, x, y):  
        rootx = self.find_parent(parent, x)  
        rooty = self.find_parent(parent, y)  
        if rank[rootx] < rank[rooty]:  
            parent[rootx] = rooty  
        elif rank[rootx] > rank[rooty]:  
            parent[rooty] = rootx  
        else:  
            parent[rooty] = rootx  
            rank[rootx] += 1  
  
    def kruskalMST(self):  
        mst = set()  
        parent = {}  
        rank = {}  
        for v in self.VE:  
            parent[v] = v  
            rank[v] = 0  
        sorted_ed = sorted(self.ed, key=lambda x: x[2])  
        for ed in sorted_ed:  
            u, v, weight = ed  
            rootu = self.find_parent(parent, u)  
            rootv = self.find_parent(parent, v)  
            if rootu != rootv:  
                mst.add(ed)  
                self.union(parent, rank, rootu, rootv)  
        return mst
    
    def printKMST():
        VE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  
        g = Graph(VE)  
        g.addEdge(6, 8, 1)  
        g.addEdge(2, 1, 2)
        g.addEdge(7, 8, 3)  
        g.addEdge(4, 2, 5)  
        g.addEdge(10, 9, 5)
        g.addEdge(5, 6, 5)
        g.addEdge(4, 5, 6)
        g.addEdge(4, 11, 11)
        g.addEdge(9, 5, 13)
        g.addEdge(3, 1, 1)
        g.addEdge(3, 1, 15)
        MST = g.kruskalMST()  
        print("Edges in the constructed MST")
        print("U, V, Weight ")
        for i in MST:
            print(i)

    def minDistance(self, dis, vis):
        min = self.inf
        for v in range(self.n):
            if dis[v] < min and vis[v] == False:
                min = dis[v]
                min_index = v
        return min_index
    """Dijkstra's Algorithm"""
    def DijkStrasMain(src):
        n = 11
        inf = 1 << 60 
        dis = [inf] * n
        vis = [False] * n
        graph = [[0,2,15,0,0,0,11,0,0,0,0],
                [2,0,0,5,0,6,0,0,0,0,0],
                [15,0,18,0,0,0,0,0,0,0,0],
                [0,5,18,0,6,0,0,0,0,0,11],
                [0,0,0,6,0,5,0,0,0,0,12],
                [0,6,0,0,5,0,0,1,0,0,0],
                [11,0,0,0,0,0,0,3,0,0,0],
                [0,0,0,0,0,1,3,0,0,0,0],
                [0,0,0,0,13,0,0,0,0,5,0],
                [0,0,0,0,0,0,0,0,5,0,37],
                [0,0,0,11,12,0,0,0,0,37,0]
                ]

        def minDistance(dis, vis):
            min = inf
            for v in range(n):
                if dis[v] < min and vis[v] == False:
                    min = dis[v]
                    min_index = v
            return min_index

        def dijkstra(src):
            dis[src] = 0
            for cout in range(n):
                u = minDistance(dis, vis)
                vis[u] = True
                for v in range(n):
                    if (graph[u][v] > 0 and
                    vis[v] == False and
                    dis[v] > dis[u] + graph[u][v]):
                        dis[v] = dis[u] + graph[u][v]
                        
        
        dijkstra(src)
        for _ in range(11):
                      print(f"#{_+1} Distance from {src} to {_} is: {dis[_]}") 

            
            
    """Prim's MST Algorithm"""                
    def primMST():
        pinf = 9999
        n = 11
        key = [pinf] * n
        parent = [None] * n
        vis = [False] * n
        key[0] = 0
        parent[0] = -1
        pgraph= [[0,2,15,0,0,0,11,0,0,0,0],
                [2,0,0,5,0,6,0,0,0,0,0],
                [15,0,18,0,0,0,0,0,0,0,0],
                [0,5,18,0,6,0,0,0,0,0,11],
                [0,0,0,6,0,5,0,0,0,0,12],
                [0,6,0,0,5,0,0,1,0,0,0],
                [11,0,0,0,0,0,0,3,0,0,0],
                [0,0,0,0,0,1,3,0,0,0,0],
                [0,0,0,0,13,0,0,0,0,5,0],
                [0,0,0,0,0,0,0,0,5,0,37],
                [0,0,0,11,12,0,0,0,0,37,0]
                ]
        def minKey(key, vis):
            min = pinf
            for v in range(n):
                if key[v] < min and vis[v]==False:
                    min = key[v]
                    min_index = v
            return min_index   
        def printMST(parent):
            print ("Edge \tWeight")
            for i in range(1, n):
                print (parent[i], "-", i, "\t", pgraph[i][parent[i]])
        for cout in range(n):
            u = minKey(key, vis)
            vis[u] = True
            for v in range(n):
                if pgraph[u][v] > 0 and vis[v] == False and key[v] > pgraph[u][v]:
                    key[v] = pgraph[u][v]
                    parent[v] = u
        printMST(parent)
    
    """Breadth First Search Algorithm"""
    def mainBFS(node):
        graph = {'A': ["B", "C", "G"],
                 'B': ["A", "D", "F"],
                 'C': ["A", "D"],
                 'D': ["B", "C", "E", "K"],
                 'E': ["D", "G", "K"],
                 'F': ["B", "E", "H"],
                 'G': ["A", "H"],
                 'H': ["F", "G"],
                 'I': ["E", "J"],
                 'J': ["I", "J"],
                 'K': ["D", "E", "J"]}
        visited = []
        queue = []
    
        def bfs(visited, graph, node):
            visited.append(node)
            queue.append(node)
            while queue:
                vertex = queue.pop(0)
                print (vertex)
                for neighbour in graph[vertex]:
                    if neighbour not in visited:
                        visited.append(neighbour)
                        queue.append(neighbour)
                        
        bfs(visited, graph, node)                    
    
                    
    """Depth First Search Algorithm"""                
    def mainDFS(node):   
        graph = {'A': ["B", "C", "G"],
                 'B': ["A", "D", "F"],
                 'C': ["A", "D"],
                 'D': ["B", "C", "E", "K"],
                 'E': ["D", "G", "K"],
                 'F': ["B", "E", "H"],
                 'G': ["A", "H"],
                 'H': ["F", "G"],
                 'I': ["E", "J"],
                 'J': ["I", "J"],
                 'K': ["D", "E", "J"]}
        visited = []
        visited1 = set()
        def dfs(visited1, graph, node):
            if node not in visited:
                print(node)
                visited1.add(node)
                for neighbour in graph[node]:
                    if neighbour not in visited1:
                        dfs(visited1, graph, neighbour)
                        
        dfs(visited1, graph, node)                    
    
                    
class MainProject(Graph, Credential):
    def __init__(self):
        return None
    """Initial Menu, allows users to log into an existing account or create a new one"""
    def firstMenu(self):
        print("Are you a new or existing user?")
        choice = input("1: New / 2: Existing: ")
        if choice == ("1"):
            clear()
            self.newUser()
        elif choice ==("2"):
            clear()
            self.logIn()
        else:
            print("Sorry, this choice is not recognised, returning to menu")
            time.sleep(2)
            clear()
            self.firstMenu()
            
    """Allows users to create an account, and checks username is not already in use"""            
    def newUser(self):
        user = input("Please enter a new username: ")
        print(user)
        if Credential.indexSearch(Credential.usernames, user) != None:
            print("Sorry, this username already exists, please try again")
            time.sleep(2)
            clear()
            self.newUser()
            
        else: 
            password = input("Please enter a new password: ")
            password2 = input("Please repeat password: ")
            if password != password2:
                print("sorry, these passwords don't match, please try again")
                time.sleep(2)
                clear()
                self.newUser()
            else:
                Credential.usernames.add(user)
                Credential.passwords.add(password)
                print("Username " + user + " created with password " + password + " proceeding to login screen")
                time.sleep(2)
                clear()
                self.logIn()
                
    """Confirms selected username exists and uses linear search (indexSearch) to confirm both are at the same 
    index in their respective linked lists to validate log in, will return users to the first menu if username doesn't 
    exist or the password is incorrect. Correct details will take users to the main menu"""            
    def logIn(self):
        user = input("Please enter your username: ")
        if Credential.indexSearch(Credential.usernames, user) != None:
            password = input("Please enter your password: ")
            if Credential.indexSearch(Credential.passwords, password) == Credential.indexSearch(Credential.usernames, user):
                print("Log in successful, welcome!")                
                time.sleep(2)
                clear()
                self.showFunction()
                
            else:
                print("Sorry this password is incorrect. Returning to login.")
                time.sleep(2)
                self.firstMenu()
        else:
            print("Sorry the username " + user + " isn't recognised. Returning to login.")
            time.sleep(2)
            clear()
            self.firstMenu()
        """A List of the available functions for users to choose, users are also able to log out, 
        and return back to the menu from whichever function they choose, invalid input will reload the menu"""
    def showFunction(self):
        print("Welcome to the city tracker.")
        time.sleep(0.15)
        print("Please choose from the following options")
        time.sleep(0.15)
        print("1. Find minumum distance between two cities")
        time.sleep(0.15)
        print("2. Search a City")
        time.sleep(0.15)
        print("3. Find minimum spanning tree")
        time.sleep(0.15)
        print("4. Log out")
        time.sleep(0.15)
        choice = input("1/2/3/4: ")
        if choice == "1":
            clear()
            print("Minimum Distances")
            """Allows users to select a city, and assigns a corresponding integer for the algorithm"""
            city = input("Please select a City A-K")
            if city == "A":
                src = 0
            elif city =="B":
                src = 1
            elif city =="C":
                src = 2
            elif city =="D":
                src = 3      
            elif city =="E":
                src = 4
            elif city =="F":
                src = 5
            elif city =="G":
                src = 6        
            elif city =="H":
                src = 7
            elif city =="I":
                src = 8
            elif city =="J":
                src = 9
            elif city =="K":
                src = 10
            else:
                print("Not recognised, please try again")
                time.sleep(2)
                clear()
                self.showFunction()
            Graph.DijkStrasMain(src)
            time.sleep(2)
            back = input("Press 1 to return to menu: ")
            if back == "1":
                clear()
                self.showFunction()
                         
            time.sleep(2)
        elif choice == "2":
            clear()
            print("Search Cities" )
            back = input("Press 1 for BFS, 2 for DFS or 3 to return to the menu  ")
            if back == "1":
                clear()
                node = input("Please select a city from A-K")
                """Allows users to choose a city, ensures that the selection is valid"""
                CorrectChoices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J","K"]  
                if node in CorrectChoices:                  
                    Graph.mainBFS(node)
                    time.sleep(2)
                    back = input("Press 1 to return to menu: ")
                    if back == "1":
                        clear()
                        self.showFunction()
                else:
                    print ("choice not recognised, returning to menu.")
                    time.sleep(2)
                    clear()
                    self.showFunction()
            elif back == "2":
                clear()
                node = input("Please select a city from A-K")
                CorrectChoices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J","K"]
                if node in CorrectChoices:
                    Graph.mainDFS(node)
                    time.sleep(2)
                    back = input("Press 1 to return to menu: ")
                    if back == "1":
                        clear()
                        self.showFunction()
                else:
                    print ("choice not recognised, returning to menu.")
                    time.sleep(2)
                    clear()
                    self.showFunction()
            elif back == "3":
                clear()
                self.showFunction()
           
        elif choice == "3":
            clear()
            print("Minimum Spanning Tree")
            """Uses locking to ensure synchronisation when printing Kruskals & Prims MST"""
            def KMST():
                lock.acquire()
                print("Printing Kruskals MST")
                Graph.printKMST()
                lock.release()
            def PMST():
                lock.acquire()
                print("Printing Prim's MST")
                Graph.primMST()
                lock.release()
            t = Thread(target=KMST, args=())
            t2= Thread(target=PMST, args=())
            t.start()
            t2.start()
            t.join()
            t2.join()
            back = input("Press 1 to return to menu: ")
            if back == "1":
                clear()
                self.showFunction()
            time.sleep(2)
        elif choice == "4":
            clear()
            print("Logging out")
            time.sleep(2)
            clear()
            self.firstMenu()
        else:
            clear()
            print("Sorry, " + choice + " is not recognised. Returning to menu")
            time.sleep(2)
            clear()
            self.showFunction()
print("Welcome to")
run = MainProject()
run.firstMenu()