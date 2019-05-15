import random
from queue import Queue

class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        if numUsers <= avgFriendships:
            raise ValueError('The number of users must be greater than the average number of friendships!')
        
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        
        # Add users
        for n in range(1, numUsers+1):
            self.addUser(n)

        # Create friendship combinations in random order
        combos = []
        for n in range(1, numUsers+1):
            for f in range(n+1, self.lastID+1):
                combos.append([n, f])
        random.shuffle(combos)

        # Add friendships
        for f in range(avgFriendships*numUsers//2):
            n, f = combos[f]
            self.addFriendship(n, f)

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}
        paths = Queue([userID])
        while paths.size() > 0:
            path = paths.dequeue()
            u = path[-1]
            if u not in visited:
                visited[u] = path
                for f in self.friendships[u]:
                    if f not in visited:
                        paths.enqueue(path + [f])
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(1000, 5)
    print('\nFriendships: ', sg.friendships)
    print()
    connections = sg.getAllSocialPaths(1)
    print('Connections: ', connections, '\n', len(connections.keys()))
