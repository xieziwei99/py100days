import matplotlib.pyplot as plt
import json

MAX_VALUE = 1000000


class Point:
    def __init__(self, x=0, y=0, z=0) -> None:
        self.x = x
        self.y = y
        self.z = z


class Line:
    def __init__(self, points=(), line_type='solid') -> None:
        self.mini = MAX_VALUE
        self.maxi = 0
        self.points: list[Point] = []
        for p in points:
            self.points.append(Point(**p))
            self.mini = min(self.mini, self.points[-1].x, self.points[-1].y)
            self.maxi = max(self.maxi, self.points[-1].x, self.points[-1].y)
        self.type = line_type

    def draw(self, axes: plt.Axes) -> plt.Axes:
        xx = [p.x for p in self.points]
        yy = [p.y for p in self.points]
        line_style = '.--' if self.type == 'dashed' else '.-'
        axes.plot(xx, yy, line_style)
        return axes


class Map:
    def __init__(self, lines=()) -> None:
        self.mini = MAX_VALUE
        self.maxi = 0
        self.lines: list[Line] = []
        for line in lines:
            self.lines.append(Line(**line))
            self.mini = min(self.mini, self.lines[-1].mini)
            self.maxi = max(self.maxi, self.lines[-1].maxi)

    def draw(self, axes: plt.Axes) -> plt.Axes:
        for line in self.lines:
            line.draw(axes)
        return axes


def get_color(r, g, b):
    return '#%02X%02X%02X' % (r, g, b)


def draw_begin() -> plt.Axes:
    plt.figure()
    axes = plt.gca()
    axes.axis('equal')
    axes.spines['top'].set_visible(False)
    axes.spines['right'].set_visible(False)
    axes.set_facecolor(get_color(222, 222, 222))

    return axes


def draw_end():
    plt.show()
    plt.close()


def main():
    with open('map.json', 'r') as f:
        mmap = json.load(f)
    mmap = Map(**(mmap['map']))

    axes = draw_begin()
    if mmap.mini < mmap.maxi:
        plt.xlim(mmap.mini, mmap.maxi + 1)
        plt.ylim(mmap.mini, mmap.maxi + 1)
    else:
        plt.xlim(0, 10)
        plt.ylim(0, 10)
    mmap.draw(axes)
    draw_end()


if __name__ == '__main__':
    main()
