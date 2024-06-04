from player import player
from player_bnode import PlayerBNode

class PlayerBST:
    '''
    instantiating this Binary Search Tree requires no inputs
    '''
    
    def __init__(self):
        self.__root = None
        self.__instances = 0
        self.list_of_nodes = []
        self.sorted_tree = None


    @property
    def instances(self):
        return self.__instances

    def instance_increment(self):
        self.__instances += 1


    @property
    def root(self):
        return self.__root
    
    @root.setter
    def root(self, player):
        self.__root = PlayerBNode(player)

    def insert(self, player):
        if self.root is None:
            self.root = PlayerBNode(player)
            self.instance_increment()
            return
        else: 
            self.recursive_insert_player_node(self.root, player)
            return
        
    def recursive_insert_player_node(self, node, player):
        if player.name < node.name:
            if node.left is None:
                node.left = PlayerBNode(player)
                self.instance_increment()
                return
            else:
                self.recursive_insert_player_node(node.left, player)
        elif player.name > node.name:
            if node.right is None:
                node.right = PlayerBNode(player)
                self.instance_increment()
                return
            else:
                self.recursive_insert_player_node(node.right, player)
        elif player.name == node.name:
            node = PlayerBNode(player)
    
    def search(self, player):
        name = player.name
        if self.root.name == name:
            return name
        else:
            searching = self.search_recursive(self.root, name)
            return searching

    def search_recursive(self, node, name):
        '''node is the node we begin search at, name is 
        the target name we are searching for'''
        if name < node.name:

            if node.left is None:
                return None
            elif name == node.left.name:
                return node.left
            else:
                searching = self.search_recursive(node.left, name)
                return searching

        if name > node.name:

            if node.right is None:
                return None
            elif name == node.right.name:
                return node.right
            else:
                searching = self.search_recursive(node.right, name)
                return searching
    

    def bst_to_sorted_list(self):
        '''traverses the tree and adds each node to an unsorted list'''
        self.list_of_nodes = []
        self.traverse_and_insert(self.root)

        def namesort(array):
          
            '''
            sorts list_list_of_nodes list, the player_bnode uses __eq__ and 
            __ge__ to define this comparison on the name aprameter'''
            if len(array) <=1:
                return array
            else:
                pivot_index = (len(array)//2)
                pivot = array[pivot_index]
                left = []
                right = []
            
                for index, player in enumerate(array):
                    if index == pivot_index:
                        continue
                    if (player <= pivot):
                        left.append(player)
                    else:
                        right.append(player)

                left = namesort(left)
                right = namesort(right)
                return (left + [pivot] + right)
            
        self.list_of_nodes = namesort(self.list_of_nodes)


    def traverse_and_insert(self, node):
        if node is not None:
            print(node)
            self.list_of_nodes.append(node)
            self.traverse_and_insert(node.left)
            self.traverse_and_insert(node.right)


    def insert_from_sorted_list(self):
        self.sorted_tree = PlayerBST()

        def insert_middle(array):

            pivot = len(array)//2

            left = array[:pivot]
            right = array[pivot+1:]
            

            if len(array) == 1:
                self.sorted_tree.insert(array[pivot])
                print(f"inserting: {array[pivot]}")
                return
            elif len(array) ==0:
                return
            else:
                self.sorted_tree.insert(array[pivot])
                print(f"inserting: {array[pivot]}")
                print(f"LEFT:{left}")
                print(f"RIGHT:{right}")
                insert_middle(left)
                insert_middle(right)

        insert_middle(self.list_of_nodes)

    
