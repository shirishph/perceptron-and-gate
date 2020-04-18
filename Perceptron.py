import plotille


class Perceptron(object):

    def __init__(self):
        self.epochs = 2
        self.learning_rate = 1
        self.weight1 = 0
        self.weight2 = 0
        self.bias = 0

        self.truth_table = [
            [1, 1, 1],
            [1, -1, -1],
            [-1, 1, -1],
            [-1, -1, -1]
        ]

    def activation(self, y_in):
        if y_in > 0:
            return 1
        elif y_in == 0:
            return 0
        if y_in < 0:
            return -1

    def predict(self, X1, X2):
        y_in = self.bias + (self.weight1 * X1) + (self.weight2 * X2)
        return self.activation(y_in), y_in

    def train(self):

        for epoch in range(self.epochs):
            print("------------------------------------------------------------------------")
            labels_upper_row = [("Input", 3), ("Tar", 1), ("NetIP", 1), ("CalOP", 1), ("WtChanges", 3), ("Weights", 3)]
            for label in labels_upper_row:
                print(label[0].rjust(label[1]*6, ' '), end="")
            print("\n", end="")
            labels_lower_row = ["x1", "x2", "LR", "t", "y_in", "y", "dw1", "dw2", "db", "w1", "w2", "b"]
            for label in labels_lower_row:
                print(label.rjust(6, ' '), end="")
            print("\n------------------------------------------------------------------------")

            print("Epoch-" + str(epoch + 1))

            for row in self.truth_table:
                retvals = self.predict(row[0], row[1])
                y = retvals[0]
                y_in = retvals[1]
                cells = [row[0], row[1], self.learning_rate, row[2], y_in, y]
                if y != row[2]:
                    change = (self.learning_rate * row[2] * row[0])
                    cells.append(change)
                    self.weight1 = self.weight1 + change

                    change = (self.learning_rate * row[2] * row[1])
                    cells.append(change)
                    self.weight2 = self.weight2 + change

                    change = (self.learning_rate * row[2])
                    cells.append(change)
                    self.bias = self.bias + change
                else:
                    cells.append("---")
                    cells.append("---")
                    cells.append("---")

                cells.append(self.weight1)
                cells.append(self.weight2)
                cells.append(self.bias)

                for cell in cells:
                    print(str(cell).rjust(6, ' '), end="")
                print("\n", end="")

            # Equation for Decision Boundary: x2 = -x1 + 1, -99 is init value
            points = [[1, -99], [2, -99], [3, -99]]
            for point in points:
                point[1] = (point[0] * -1) + 1

            fig = plotille.Figure()
            fig.width = 30
            fig.height = 15
            fig.set_x_limits(min_=-5, max_=5)
            fig.set_y_limits(min_=-5, max_=5)
            fig.color_mode = 'byte'

            fr = [points[0][0], points[1][0]]
            to = [points[0][1], points[1][1]]
            fig.plot(fr, to, lc=None, label='')

            fr = [points[1][0], points[2][0]]
            to = [points[1][1], points[2][1]]
            fig.plot(fr, to, lc=None, label='')

            print(fig.show(legend=False))
            print("\n\n")

        return True
