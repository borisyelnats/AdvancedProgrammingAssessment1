
from player import player
from player_bst import PlayerBST
from player_bnode import PlayerBNode

# Create the BST instance
bst = PlayerBST()

a = (player(1,"A"))
b = (player(1,"B"))
c = (player(1,"C"))
d = (player(1,"D"))
e = (player(1,"E"))
f = (player(1,"F"))
g = (player(1,"G"))


bst.insert(c)
bst.insert(f)
bst.insert(a)
bst.insert(b)
bst.insert(f)
bst.insert(e)
bst.insert(d)


bst.bst_to_sorted_list()
print("\n\nsorted list of ndoes:")
print(bst.list_of_nodes)
print("\n\n")


#print(bst.instances)

#print(len(bst.list_of_nodes))
#print(bst.root)

bst.insert_from_sorted_list()

print(bst.sorted_tree.instances)





'''
players = bst.list_of_nodes
for i in range(len(players)-1):
    print(players[i].name, end = " ")
    if players[i].name < players[i+1].name:
        print(i, " ", True)
    else:
        print(i, " ",False)
print("/n/n")
print(bst.list_of_nodes)
for i in list(range(1,20,1)):
    print(i//2)
    print(i)
    print("/n")
'''