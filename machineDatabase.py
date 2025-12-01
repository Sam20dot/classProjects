class MyClassY2ETE :
    def __init__(self,machines):
        self.machines=[]

    # function adding the machine 
    def addMachine(self) :
        while True :
            reg_number= input (" enter the student regNumber :")
            student_name=input (" enter the student name :")
            serialNumber=input (" enter the serial number :")
            machineType=input (" enter the machine type :")
            machineInfo= {"reg_number":reg_number,"student_name":student_name,"serialNumber":serialNumber,
                          "machineType":machineType}
            self.machines.append(machineInfo)
            print (f" machine has been added successfully !\n {self.machines}")

    
