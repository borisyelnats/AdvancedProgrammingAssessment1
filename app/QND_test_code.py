
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

print(bst.search(g))


