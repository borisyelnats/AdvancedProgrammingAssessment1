import player
import player_list
import player_node

A = player.player(1, "Aaron")
B = player.player(2, "Ben")
C = player.player(3, "Charles")

An = player_node.Player_node(A)
Bn = player_node.Player_node(B)
Cn = player_node.Player_node(C)


List = player_list.PlayerList()
List.insert_node(An)
#print(List.get_tail.key)

List.insert_node(Bn)
List.insert_node(Cn)
List.display()
List.display(forward=0)
'''
print(List.get_tail.key)
List.insert_at_tail(Cn)
print(List.get_tail.key)
List.delete_tail()
print(List.get_tail.key)
'''