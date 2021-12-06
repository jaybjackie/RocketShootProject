import json

class Read:
    """ Store infomation such as name and score into the database """
    def __init__(self, name, score):
        if not isinstance(name, str):
            raise TypeError ("name must be a string")
        self.name = name
        if not isinstance(score, int):
            raise ValueError("score must be integer")
        self.score = score

    def __repr__(self) -> str:
        return f"Player(name='{self.name}', score={self.score})"
    
    def insert(self):
        """ Insert name and their score to database """
        new_data = {
            self.name:{
                'score':self.score}
        }

        try:
            with open('database.json','r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open('database.json','w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open('database.json','w') as data_file:
                json.dump(data, data_file, indent=4)

    def get_top(self):
        """ Return list contain player and score sorted by their score """
        try:
            with open('database.json','r') as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            print("No data File Found")
        else:
            # get name and their score into name:score
            res = dict()
            for i in data:
                res[i] = data[i]['score']
            
            # sort dict by value Decsending Order
            sorted_score = dict()
            sorted_name = sorted(res,key=res.get,reverse=True) 
            
            for name in sorted_name:
                sorted_score[name] = res[name]
            # convert dict to list to get player and their score
            name_score = sorted_score.items()
            # highest score list
            highest_score = list(name_score)[:15]
            return highest_score