import socket
import random
import json


ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4, TCP
ss.bind((socket.gethostname(), 54545))  # localhost
ss.listen(5)  # queue of 5 connections


"""
Parameters: number_of_scenes (int) and scene_range (list of two integers representing a range, both inclusive)
Returns:    list of number_of_scenes integers, all within the provided scene_range
"""
def generate_dungeon(num_of_scenes, scene_range):
    scene_list = []
    start = scene_range[0]
    stop = scene_range[1] + 1
    for i in range(num_of_scenes):
        scene_list.append(random.randrange(start, stop))
    return scene_list


"""
Parameters: dictionary of scene information
Returns: Tuple. First value is True if the data is valid, False if not. Second value is empty string or error string.
"""
def is_valid(request_dict):
    num_of_scenes_valid = test_num_of_scenes(request_dict)
    if not num_of_scenes_valid[0]:
        return num_of_scenes_valid
    scene_range_valid = test_scene_range(request_dict)
    return scene_range_valid


""" Confirms that the num_of_scenes value is valid """
def test_num_of_scenes(request_dict):
    if "num_of_scenes" not in request_dict:
        return (False, "num_of_scenes missing")
    if type(request_dict["num_of_scenes"]) is not int:
        return (False, "num_of_scenes must be an integer")
    if request_dict["num_of_scenes"] <= 0:
        return (False, "num_of_scenes must be greater than 0")
    return (True, "")


""" Confirms that the scene_range value is valid """
def test_scene_range(request_dict):
    if "scene_range" not in request_dict:
        return (False, "scene_range missing")
    if type(request_dict["scene_range"]) is not list:
        return (False, "scene_range is not a list")
    if len(request_dict["scene_range"]) < 2:
        return (False, "scene_range does not have start and end values")
    if len(request_dict["scene_range"]) > 2:
        return (False, "scene_range has more than two values")
    if type(request_dict["scene_range"][0]) is not int:
        return (False, "scene_range list must contain integers")
    if type(request_dict["scene_range"][1]) is not int:
        return (False, "scene_range list must contain integers")
    if request_dict["scene_range"][0] > request_dict["scene_range"][1]:
        return (False, "first integer in scene_range must be less than second integer")
    if request_dict["scene_range"][0] <= 0 or request_dict["scene_range"][1] <= 0:
        return (False, "scene_range integers must be greater than 0")
    return (True, "")


def serverloop():
    while True:
        clientsocket, address = ss.accept()  # stores client socket object and client IP addr
        request = clientsocket.recv(2048)
        request = request.decode("utf-8")
        print("Received request:", request)
        request_dict = json.loads(request)
        test_validity, validity_statement = is_valid(request_dict)
        if test_validity:
            dungeon = generate_dungeon(request_dict["num_of_scenes"], request_dict["scene_range"])
            message = json.dumps({'scene_list': dungeon})
            print("Message to send:", message)
            clientsocket.send(bytes(message, "utf-8"))  # must send as bytes
        else:
            clientsocket.send(bytes(json.dumps({"error": validity_statement}), "utf-8"))


if __name__ == '__main__':
    serverloop()
