from get_options import Options

class SelectParameters():
    def __init__(self):
        self.options = Options()

    def want_parameters(self):
        i = input(str())
        output = self.options.focus
        if i == output:
            print(output)

q = SelectParameters()
q.want_parameters()