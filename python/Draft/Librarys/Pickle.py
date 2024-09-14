# Draft/Librarys/Pickle.py
import pickle


#|> Pickle module is used to save an object instance into file.
#|> Python pickling is very useful when we want the store large instances.
#|> Pickled files are very dengrous because we can not load the files untell we run it.


class PICKLE:

    def __init__(self) -> None:
        self.name   = "Learn python"
        self.device = "So weak ): "

    def discribe(self):
        return f"Name: {self.name}, Device: {self.device}"
    

# Create an instance.
Pick = PICKLE()

# To save it.
with open(r"C:\Users\Hp\Desktop\bilal\files\Codes\Python\Results\pickle\Pick.pickle", "wb") as file:
    pickle.dump(Pick, file)


# Load it.
with open(r"C:\Users\Hp\Desktop\bilal\files\Codes\Python\Results\pickle\Pick.pickle", "rb") as file:
    returnedobj = pickle.load(file)

