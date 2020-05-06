import numpy as np
import matplotlib.pyplot as plt


class Triangle:
    def __init__(self, points, id=0):
        super().__init__()
        self.vertex1, self.vertex2, self.vertex3 = points
        self.vertex1 = np.array(self.vertex1)
        self.vertex2 = np.array(self.vertex2)
        self.vertex3 = np.array(self.vertex3)
        self.id = id % 2

    def get_vertex(self):
        return self.vertex1, self.vertex2, self.vertex3

    def get_midpoints(self):
        pt1 = (self.vertex1 + self.vertex2) / 2
        pt2 = (self.vertex2 + self.vertex3) / 2
        pt3 = (self.vertex3 + self.vertex1) / 2
        return [pt1, pt2, pt3]

    def display(self, ax=None):
        k = ax if ax is not None else plt
        x, y = zip(*self.get_vertex())
        k.plot(x, y, ".", linestyle="None")

    def display_fill(self, ax=None):
        t = plt.Polygon(self.get_vertex())
        # clr = "black" if self.id else "red"
        if ax is None:
            plt.gca().add_patch(t)
        else:
            ax.add_patch(t)

    def get_sub_triangles(self):
        mp1, mp2, mp3 = self.get_midpoints()
        t1 = Triangle([self.vertex1, mp1, mp3])
        t2 = Triangle([self.vertex2, mp1, mp2])
        t3 = Triangle([self.vertex3, mp2, mp3])
        return t1, t2, t3


def sierpinsky(triangle: Triangle = None, depth: int = 5):
    if depth < 1:
        return [triangle]
    st = triangle.get_sub_triangles()
    out = [triangle]
    for t in st:
        out += sierpinsky(t, depth - 1)
    return out


if __name__ == "__main__":
    t = Triangle([(0, 0), (1, 0), (0.5, 0.75)])

    fig, ax = plt.subplots()
    # t.display(ax=ax)
    k = sierpinsky(t, depth=5)
    for st in k:
        # st.display_fill(ax=ax)
        st.display(ax=ax)
    plt.show()
    # print([x.get_vertex() for x in k])
    # print(k)
