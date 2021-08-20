class List:
    array = []

    def add(self, element):
        self.array.append(element)

    def contains(self, item):
        return item in self.array

    def get(self, index):
        return self.array[index]

    def remove(self, element):
        self.array.remove(element)

    def __str__(self):
        return f'[{", ".join(map(str, self.array))}]'


if __name__ == '__main__':
    myList = List()
    myList.add(1)
    myList.add(2)
    myList.add(3)
    print(myList)
    print(myList.contains(2))
    print(myList.get(1))
    myList.remove(2)
    print(myList)
