from unittest import TestCase

from line_segment import LineSegment
from points import Point2D


class LineSegment_test(TestCase):
    DELTA = 1.0e-12

    def test_evaluate(self):
        start = Point2D(-2, -2)
        end = Point2D(3, 8)
        line_segment = LineSegment(start, end)
        for t, expected in [(0, start), (0.2, Point2D(-1, 0)), (0.5, Point2D(0.5, 3.0)), (1.0, end)]:
            actual = line_segment.evaluate(t)
            self.assertIsInstance(actual, Point2D)
            self.assertAlmostEqual(expected.x, actual.x, delta=self.DELTA)
            self.assertAlmostEqual(expected.y, actual.y, delta=self.DELTA)

    def test_intersecting_line_segments(self):
        for intersect, start_1, end_1, start_2, end_2 in [((0,0), (-1, 0), (1, 0), (0, -1), (0, 1)),
                                                          ((1, 2), (-3, 4), (3, 1), (-3, 1), (5, 3)),
                                                          ((0, 0), (-1, 1), (0, 0), (0, 0), (1, 1))]:
            segment_1 = LineSegment(Point2D(*start_1), Point2D(*end_1))
            segment_2 = LineSegment(Point2D(*start_2), Point2D(*end_2))
            expected = Point2D(*intersect)
            actual = segment_1.intersect(segment_2)
            self.assertIsInstance(actual, Point2D)
            self.assertAlmostEqual(expected.x, actual.x, delta=self.DELTA)
            self.assertAlmostEqual(expected.y, actual.y, delta=self.DELTA)

    def test_non_intersecting_line_segments(self):
        for start_1, end_1, start_2, end_2 in [((-1, 0), (1, 0), (0, 1), (0, 2)),
                                               ((-1, 0), (1, 0), (0, 1e-9), (0, 2)),
                                               ((-1, 0), (1, 0), (-1, 1), (1, 1)),
                                               ((0, 0), (1, 1), (1, 1), (0, 0))]:
            segment_1 = LineSegment(Point2D(*start_1), Point2D(*end_1))
            segment_2 = LineSegment(Point2D(*start_2), Point2D(*end_2))
            actual = segment_1.intersect(segment_2)
            self.assertIsNone(actual)

