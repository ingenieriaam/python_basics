##########################################

myList = [1,2,3,4]
print(len(myList))

class Object:
    pass

myObject = Object()
# print(len(myObject)) it will not work

class CD:
    def __init__(self,artist,title,songs):
        self.artist = artist
        self.title = title
        self.songs = songs
    # special methods
    def __str__(self):
        return f"{self.artist} - {self.title} - have {self.songs} songs"
    def __len__(self):
        return self.songs
    def __del__(self):
        print("I've been deleted")

myCd = CD('AC/DC','Back in Black',10)

print(myCd)
print(len(myCd))
del myCd
