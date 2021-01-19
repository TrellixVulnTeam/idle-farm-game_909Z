from src import Crop


class Potato(Crop.Crop):

    def __init__(self, line: str, create_new=False):
        # we define initial values of Crop
        if create_new:
            # create new carrot object (define default parameters)
            line = "Potato,0,0,0,0,0,0,0,1,0,0,0,0,0"
        super().__init__(line)