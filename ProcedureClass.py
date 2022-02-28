class Procedure:
    def __init__(self, pname, pdate, practitioner_name, charges, p_id):
        self.__pname= pname
        self.__pdate = pdate
        self.__practitioner_name = practitioner_name
        self.__charges = charges
        self.__p_id = p_id


    def get_pname(self):     
        return self.__pname

    def get_pdate(self):
        return self.__pdate

    def get_practitioner_name(self):
        return self.__practitioner_name

    def get_charges(self):
        return self.__charges
        
    def get_p_id(self):
        return self.__p_id


    def print_Procedure(self):
        print("Name of the procedure:", self.__pname)
        print("Date of the procedure:", self.__pdate)
        print("Name of the practitioner who performed the procedure:", self.__practitioner_name)
        print("Charges for the procedure:", self.__charges)
        print("patient ID:", self.__p_id)
        

