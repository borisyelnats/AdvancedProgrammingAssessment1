import sys
sys.path.append("/Users/benjamincooper/Documents/TAFE/advanced programming/AP_ass1/SRUS-BJC-Games/app")
import player
import player_list
import player_node
import argon2
hasher = argon2.PasswordHasher()


player1 = player.player(1, "A")


player1.add_password("TEST PASSWORD")

print(player1.verify_password("TEST PASSWORD"))





