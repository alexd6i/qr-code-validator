from helper import *
import copy

class TxtData:
    '''
    A class representing text data, in form of a list

    Instance attributes:
        data (list): nested list representing data
        rows (int): rows of the nested list
        cols (int): columns of the nested list
    ''' 
    def __init__(self, data):
        '''
        (list) -> None

        Constructor of the class TxtData
        >>>my_list = get_data("qrcode_binary.txt")
        >>>my_txt = TxtData(my_list)
        >>>my_txt.rows
        33
        >>>my_txt.cols
        33

        >>>list = [[1,0,1], [1,0,1], [1,0,1]]
        >>>txt = TxtData(list)

        >>>my_list = get_data("small_code.txt")
        >>>my_txt = TxtData(my_list)
        >>>my_txt.rows
        2
        >>>my_txt.cols
        2
        '''
        self.data = copy.deepcopy(data)
        self.rows = len(self.data)
        self.cols = len(self.data[0]) #The length of a nested list in data

    
    def __str__(self):
        '''
        (list) -> str

        Returns a string describing the row and column count of a list
        >>>my_list_simple = [[6,9,6]]
        >>>my_txt_simple = TxtData(my_list_simple)
        >>>print(my_list_simple)
        This TxtData object has 1 rows and 3 columns.
        >>>my_list = get_data("qrcode_binary.txt")
        >>>my_txt = TxtData(my_list)
        >>>print(my_txt)
        This TxtData object has 33 rows and 33 columns.
        >>>my_list = get_data("small_data.txt")
        >>>my_txt = TxtData(my_list)
        >>>print(my_txt)
        This TxtData object has 2 rows and 2 columns.
        '''
        rows = str(self.rows)
        cols = str(self.cols)

        r = 'This TxtData object has ' + rows + ' rows and '\
        + cols + ' columns.'

        return r


    def get_pixels(self):
        '''
        (None) -> int
        
        Returns the total number of pixels in data, with row * column
        >>>my_list_simple = [[1,2,3],[4,5,6]]
        >>>my_txt_simple = TxtData(my_list_simple)
        >>>my_txt_simple.get_pixels()
        6
        >>>list = get_data("small_data.txt")
        >>>txt = TxtData(my_list)
        >>>txt.get_pixels()
        4
        >>>txt = TxtData([1, 0, 1, 1, 1, 0])
        txt.get_pixels()
        6
        '''
        pixels = self.rows * self.cols #Computing total number of pixels

        return pixels

    
    def get_data_at(self, row, col):
        '''
        (int, int) -> int

        Returns the value at the position indicated by the two input integers
        >>>my_list_simple = [[1,2,3],[4,5,6]]
        >>>my_txt_simple = TxtData(my_list_simple)
        >>>my_txt_simple.get_data_at(0,0)
        1
        >>>my_list_simple = [[1, 0, 1, 0, 0], [1, 0, 1, 0, 0]]
        >>>my_txt_simple = TxtData(my_list_simple)
        >>>my_txt_simple.get_data_at(1,1)
        0
        >>>my_list_simple = [[1, 1], [1, 1], [1, 1], [1, 1]]
        >>>my_txt_simple = TxtData(my_list_simple)
        >>>my_txt_simple.get_data_at(34,23)
        Traceback (most recent call last):
        ValueError: Index out of bound!
        '''
        #Checking if requested position is out of bounds
        if row + 1 > self.rows or col + 1 > self.cols:
            raise ValueError('Index out of bound!')

        return self.data[row][col]

    
    def pretty_save(self, file_name):
        '''
        (str) -> None

        Converts binary in a prettier form and writes it in file_name
        >>>my_list = get_data("qrcode_binary.txt")
        >>>my_txt = TxtData(my_list)
        >>>my_txt.pretty_save("qrcode_pretty.txt")

        >>>my_list = get_data("small_data.txt")
        >>>my_txt = TxtData(my_list)
        >>>my_txt.pretty_save("small_data_pretty.txt")

        >>>my_list = get_data("ones_and_zeroes.txt")
        >>>my_txt = TxtData(my_list)
        >>>my_txt.pretty_save("blocks_and_spaces.txt)
        '''
        fobj = open(file_name, 'w', encoding="utf-8") #opens file for writing

        for line in self.data:
            pretty_line = '' #Creates line where box/space is added

            for char in line:
                if char == 0:
                    pretty_char = '  '
               
                elif char == 1:
                    pretty_char = '\u2588' * 2 #2 Black boxes

                pretty_line += pretty_char
            
            fobj.write(pretty_line)
            fobj.write('\n') #Starts next iteration on a new line

        fobj.close()


    def equals(self, another_data):
        '''
        (TxtData) -> bool

        Returns True if two TxtData objects are equal, False otherwise
        >>>my_list_simple = [[1,2,3],[4,5,6]]
        >>>my_txt_simple_1 = TxtData(my_list_simple)
        >>>my_txt_simple_2 = TxtData(my_list_simple)
        >>>my_txt_simple_1.equals(my_txt_simple_2)
        True
        >>>list1 = []
        >>>list2 = [0]
        t1 = TxtData(list1)
        t2 = TxtData(list2)
        t1.equals(t2)
        False
        >>>list1 = get_data("small_data.txt")
        >>>list2 = get_data("small_data.txt")
        t1 = TxtData(list1)
        t2 = TxtData(list2)
        t1.equals(t2)
        True
        '''
        return self.data == another_data.data

    def approximately_equals(self, another_data, precision):
        '''
        (TxtData, float) -> bool
        
        Returns a bool showing if two TxtData objects are approximately equal
        >>>my_list_simple_1 = [[1,2,3],[4,5,6]]
        >>>my_list_simple_2 = [[1,2,3],[7,8,9]]
        >>>my_txt_simple_1 = TxtData(my_list_simple_1)
        >>>my_txt_simple_2 = TxtData(my_list_simple_2)
        >>>my_txt_simple_1.approximately_equals(my_txt_simple_2, 0.5)
        True
        >>>list1 = get_data("small_data.txt")
        >>>list2 = get_data("small_data.txt")
        t1 = TxtData(list1)
        t2 = TxtData(list2)
        t1.approximately_equals(t2, 0.1)
        True
        >>>list1 = [[1,4,2], [7,8,4]]
        >>>list2 = [[9,0,9], [3,2,1]]
        t1 = TxtData(list1)
        t2 = TxtData(list2)
        t1.approximately_equals(t2, 0.3)
        False
        '''
        inconsistent_values = 0

        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i][j] != another_data.data[i][j]:
                    inconsistent_values += 1

        inconsistent_rate = inconsistent_values / self.get_pixels()

        return inconsistent_rate <= precision
