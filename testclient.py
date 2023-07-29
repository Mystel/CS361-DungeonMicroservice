import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 54545))

test_dungeon = {
    "num_of_scenes": 12,
    "scene_range": [8, 23]
}

dungeon = json.dumps(test_dungeon)
s.send(bytes(dungeon, "utf-8"))
reply = s.recv(2048)  # buffer for stream of data to receive at a time
decoded_reply = reply.decode("utf-8")
reply_object = json.loads(decoded_reply)
print(reply_object['scene_list'])
