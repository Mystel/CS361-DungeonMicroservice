import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 54545))

test_dungeon = {
    "difficulty": "easy",
    "num_of_scenes": 10,
    "scene_range": (1, 15)
}

dungeon = json.dumps(test_dungeon)
s.send(bytes(dungeon, "utf-8"))
reply = s.recv(2048)  # buffer for stream of data to receive at a time
print(reply.decode("utf-8"))
