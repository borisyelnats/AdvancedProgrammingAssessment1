import player_bst
from player_bnode import PlayerBNode
import player

A = player.player(1, "Aaron")
B = player.player(2, "Ben")

An = PlayerBNode(A)
Bn = PlayerBNode(B)

BST = player_bst
BST.insert_player_node(A)


