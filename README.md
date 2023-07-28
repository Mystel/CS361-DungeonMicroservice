# CS361-DungeonMicroservice

### Description
This is a python server using sockets that is meant to be run locally and that will serve as a dungeon-randomizing microservice for my CS361 partner's project.

### Running the Server
The microservice.py file must be run as its own process either from the command prompt or from an IDE such as PyCharm. It uses a TCP connection and IPv4. It runs locally (localhost) over port 54545.

### Connecting to the Server
Connect to the server using a TCP connection to port 54545 over IPv4. For example, in Python, use:
```py
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 54545))
```

### Requesting Data
Requests must be sent as JSON objects formatted as a utf-8 string and byte-encoded.
The JSON object must contain the following:
  'num_of_scenes': integer             # how many scenes to include in the dungeon
  'scene_range': list of two integers  # the range of scene numbers to include, first- and last-inclusive
For example, the JSON object may contain:
```py
test_dungeon = {
    "num_of_scenes": 12,
    "scene_range": (8, 23)
}
```
A request can then be made by sending the following message:
```py
dungeon = json.dumps(test_dungeon)
s.send(bytes(dungeon, "utf-8"))
reply = s.recv(2048)
decoded_reply = reply.decode("utf-8")
```

### Receiving Data
