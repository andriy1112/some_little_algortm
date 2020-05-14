from _collections import deque
graph = {}
graph['you']   = ['alice', 'bob', 'claire']
graph['alice'] = ['peggy']
graph['bob'] = ['anuj', 'peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

def person_is_saller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_saller(person):
                print(person, 'is a mango seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
search('you')