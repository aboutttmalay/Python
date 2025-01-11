# can you change the malay-parameter inside a class to something else (say
# "harry"). Try changing malay to "slf" or "harry" and see the effects.




from random import randint  #importing randint from random module


class Train:


    def __init__(malay,trainNo):
        malay.trainNo = trainNo


    def book(malay, trainNo , fro,to):
        print(f"Ticket is booked in train no: {malay.trainNo} from {fro} to {to}")

    def get_status(malay, trainNo , fro,to):
         print(f" Train no:{malay.trainNo} from {fro} to {to} is on time")

    def get_Fare(malay, trainNo , fro,to):
        print(f" Fare for train no:{malay.trainNo} from {fro} to {to} is {randint(222,2500)}")


Train_number = int(input("Enter the train number: "))
fro = input("Enter the source: ")
to = input("Enter the destination: ")
t=Train(Train_number)
t.book(Train_number,fro,to)
t.get_status(Train_number,fro,to)
t.get_Fare(Train_number,fro,to)
