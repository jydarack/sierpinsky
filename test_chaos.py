import numpy as np
import pytest
from sierpinsky_points import Triangle


@pytest.fixture
def get_t():
    return Triangle([(0, 0), (1, 0), (0.5, 0.75)])


def test_triangles():
    points = [(0, 0), (1, 0), (0.5, 0.75)]
    t = Triangle(points)
    assert isinstance(t, Triangle)
    assert all([x == y for x, y in zip(t.vertex1, np.array(points[0]))])
    assert all([x == y for x, y in zip(t.vertex2, np.array(points[1]))])
    assert all([x == y for x, y in zip(t.vertex3, np.array(points[2]))])


def test_t_fix(get_t):
    print(get_t.get_midpoints())
    assert isinstance(get_t, Triangle)
