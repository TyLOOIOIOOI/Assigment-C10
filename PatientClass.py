class Patient:
    def __init__(self, id, name, address, phone, vs):
        self.__id = id
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__vs = vs

#accessor methods(
    def get_id(self):     
        return self.__id

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone
        
    def get_vs(self):
        return self.__vs
#)
    def print_Patient(self):
        print("Name:", self.__name)
        print("Address:", self.__address)
        print("Phone:", self.__phone)
        