


from random import randint  #importing randint from random module


class Train:


    def __init__(self,trainNo):
        self.trainNo = trainNo


    def book(self, trainNo , fro,to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def get_status(self, trainNo , fro,to):
         print(f" Train no:{self.trainNo} from {fro} to {to} is on time")

    def get_Fare(self, trainNo , fro,to):
        print(f" Fare for train no:{self.trainNo} from {fro} to {to} is {randint(222,2500)}")


Train_number = int(input("Enter the train number: "))
fro = input("Enter the source: ")
to = input("Enter the destination: ")
t=Train(Train_number)
t.book(Train_number,fro,to)
t.get_status(Train_number,fro,to)
t.get_Fare(Train_number,fro,to)
