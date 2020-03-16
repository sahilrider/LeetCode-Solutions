'''https://leetcode.com/problems/keys-and-rooms/'''

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return True
        #bfs
        q = [0]
        visited = []
        while q:
            room = q.pop(0)
            if room not in visited:
                visited.append(room)
                q.extend(rooms[room])
        return len(visited)==len(rooms)