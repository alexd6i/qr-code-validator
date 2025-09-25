#Constants for length of each part of 'dd/mm/yyyy'
D = 2
M = 2
Y = 4

def convert_date(date_str):
    '''
    (str) -> dict
    Returns a dd/mm/yyyy date in dictionary format

    >>>>convert_date("09/01/2024")
    {'Day': '09', 'Month': '01', 'Year': '2024'}
    >>>> convert_date("06/01/2025")
    {'Day': '06', 'Month': '01', 'Year': '2025'}
    >>>>convert_date("banana")
    Traceback (most recent call last):
    ValueError: Input format incorrect!
    '''
    parts = date_str.split('/') #Split date in 3 parts: ['dd', 'mm', 'yyyy']
    
    if len(parts) != 3: #Check for 3 parts
        raise ValueError('Input format incorrect!')
    
    #Ensuring each part has the right length
    elif len(parts[0]) != D or len(parts[1]) != M or len(parts[2]) != Y:
        raise ValueError('Input format incorrect!')
    
    else: #Date format is good
    
        date = {}
    
        date['Day'] = parts[0]
        date['Month'] = parts[1]
        date['Year'] = parts[2]
    
    return date

def get_data(file_path):
    '''
    (str) -> list
    Returns a nested list of integers representing the data of a file
    >>>get_data("small_data.txt")
    [[0, 1], [1, 0]]
    >>>get_data('qrcode_binary_error.txt')
    Traceback (most recent call last):
    ValueError: File should contain only 0s and 1s!
    >>get_data("data.txt")
    [[1, 0, 1, 0], [1, 0, 1, 0], [1, 0, 1, 0], [1, 0, 1, 0]]
    '''
    fobj = open(file_path, 'r') #Opens file in read mode
    
    data = []
    
    for line in fobj:
        l = [] #Sublist of data representing each row
        line = line.strip() #Removes the \n char at the end of the line
        
        for char in line:     
            if char != '0' and char != '1':
                raise ValueError('File should contain only 0s and 1s!')

            else:
                l.append(int(char))
            
        data.append(l) #Adds a the sublist to data
        
    fobj.close()
    
    return data
