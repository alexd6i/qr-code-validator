from txtdata import* #Imports Everything from txtdata and helper

class QRCode:
    '''
    A class that represents a QR code

    Instance attributes:
        last_update_date (dict): a dictionary representing the
            last update date of the QR code
        owner (str): a string representing the owner of the QR code
        data (TxtData): represents the QR code itself
        error_correction (float): the error correction capability of a QR code
    '''
    def __init__(self, file_path, last_update_date = '00/00/0000',
        owner = 'Default Owner', error_correction = 0.0):
        '''
        (str, str, str, float) -> None

        Constructs a QRCode attribute
        >>> my_qrcode = QRCode("qrcode_binary.txt", "01/09/2024", "Vivian", 0.1)
        >>> my_qrcode.last_update_date['Day']
        '01'
        >>> my_qrcode.last_update_date['Month']
        '09'
        >>> my_qrcode.last_update_date['Year']
        '2024'
        >>> my_qrcode.owner
        'Vivian'
        >>> my_qrcode.error_correction
        0.1

        >>>my_qrcode = QRCode("small_data.txt", "01/03/2022", "Joe", 0.1)

        >>>my_qrcode = QRCode("qrcode.txt", "12/08/2017", "Lebron", 0.1)
        '''
        self.data = TxtData(get_data(file_path))
        self.last_update_date = convert_date(last_update_date)
        self.owner = owner
        self.error_correction = error_correction


    def __str__(self):
        '''
        (QRCode) -> str
        
        Returns a string describing the QR code
        >>> my_qrcode = QRCode("qrcode_binary.txt", "01/09/2024", "Vivian", 
                        0.1)
        >>> print(my_qrcode)
        The QR code was created by Vivian and last updated in 2024.
        The details regarding the QR code file are as follows:
        This TxtData object has 33 rows and 33 columns.
        >>> my_qrcode = QRCode("small_data.txt", "01/06/2025", "Alex", 0.2)
        >>> print(my_qrcode)
        The QR code was created by Alex and last updated in 2025.
        The details regarding the QR code file are as follows:
        This TxtData object has 2 rows and 2 columns.
        >>> my_qrcode = QRCode("qrcode.txt", "04/05/2022", "LeBron", 0.1)
        >>> print(my_qrcode)
        The QR code was created by LeBron and last updated in 2022.
        The details regarding the QR code file are as follows:
        This TxtData object has 6 rows and 23 columns.
        '''
        return 'The QR code was created by ' + self.owner + ' '\
                'and last updated in ' + str(self.last_update_date['Year']) +\
                '.\nThe details regarding the QR code file are as follows:'\
                + '\n' + str(self.data)

    
    def equals(self, another_qrcode):
        '''
        (QRCode) -> bool

        Returns True or False depending on if 2 QRCodes objects are equal
        >>> my_qrcode = QRCode("qrcode_binary.txt", "01/09/2024", "Vivian",
                        0.1)
        >>> my_qrcode_copy = QRCode("qrcode_binary_copy.txt", "01/09/2022",
            "Xuanpu", 0.1)
        >>> my_qrcode.equals(my_qrcode_copy)
        True
        >>> my_qrcode = QRCode("small_data.txt", "01/06/2025", "Alex",
                        0.1)
        >>> my_qrcode2 = QRCode("qrcode_binary_copy.txt", "01/09/2022",
            "Xuanpu", 0.1)
        >>> my_qrcode.equals(my_qrcode_copy)
        False
        >>> my_qrcode = QRCode("small_data.txt", "01/06/2025", "Alex",
                        0.1)
        >>> my_qrcode_copy = QRCode("small_data.txt", "03/02/2021",
            "Jake", 0.2)
        >>> my_qrcode.equals(my_qrcode_copy)
        True
        '''
        #Checking if both objects have equal data (with TxtData.equals)
        equal_data = self.data.equals(another_qrcode.data)
        #Checking if error_correction attributes of both objects are the same
        equal_ec = self.error_correction == another_qrcode.error_correction

        return equal_data and equal_ec
    
    
    def is_corrupted(self, precise_qrcode):
        '''
        (QRCode) -> bool

        Returns whether the QRCode object is corrupted
        >>> my_qrcode = QRCode("qrcode_binary.txt", "01/09/2024", "Vivian", 0.1)
        >>> my_c_qrcode = QRCode("qrcode_binary_c.txt", "01/09/2000", "Vivian",
                        0.1)
        >>> my_c_qrcode.is_corrupted(my_qrcode)
        True
        >>> my_qrcode = QRCode("small_data.txt", "01/06/2025", "Alex", 0.1)
        >>> my_c_qrcode = QRCode("small_data.txt", "01/06/2025", "Alex", 0.1)
        >>> my_c_qrcode.is_corrupted(my_qrcode)
        False
        >>> my_qrcode = QRCode("small_data.txt", "01/06/2025", "Alex", 0.1)
        >>> my_qrcode_copy = QRCode("small_data.txt", "03/02/2021",
                            "Jake", 0.2)
        >>> my_c_qrcode.is_corrupted(my_qrcode)
        True
        '''
        #Data attributes of both QRCode objects
        qr1 = self.data
        qr2 = precise_qrcode.data

        return not qr1.approximately_equals(qr2, self.error_correction)
