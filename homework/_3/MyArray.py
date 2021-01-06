class MyArray:

    def __init__(self, data_type, length, array):
        self.type_name = data_type
        self.length = length
        self.data = []
        for i in range(length):
            self.data.append(None)

        if array is not None:
            if len(array) > length:
                for i in range(length):
                    self.data[i] = array[i]
            else:
                for i in range(len(array)):
                    self.data[i] = array[i]

    def __getitem__(self, index):
        try:
            return self.data[index]
        except IndexError:
            raise IndexError

    def __setitem__(self, index, value):
        try:
            self.data[index] = value
        except IndexError:
            raise IndexError

    def __str__(self):
        return str(self.data)


if __name__ == '__main__':
    arr = MyArray(int, 5, [1, 2, 3, 4, 5])
    print(arr)
    for j in range(5):
        arr[j] = 4
    print(arr)
