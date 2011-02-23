'''
Copy of Rect5 (http://pypi.python.org/pypi/Rect/5)

changes:
- top and bottom are exchanged
- int instead float
- new methods starting at __getitem__
'''

class ScreenRect(object):
    """
    The ScreenRect class is used for storing and manipulating rectangular areas.

    It has left, top, width and height attributes, which are automatically
    changed by assignment to the right, bottom, bottomleft, bottomright, topleft, 
    topright or center properties.

    Rects can be added to greater a greater containing rectangle, or a 
    Rect.union classmethod is available to sum a list of Rect objects.

    The collidepoint and intersects methods are used for collision testing.

    Eg:
    >> Rect((0,0,10,10)).collidepoint((2,2))
    >> True
    >> Rect((0,0,10,10)).collidepoint((20,20))
    >> False

    This Rect class is different to the Pygame Rect class, in that is stores
    coordinates internally as ints, and uses a left-handed coordinate
    system.


    """
    def __init__(self, *args, **kwargs):
        """
        xywh must be a 2 or 4 tuple or a rect instance.
        
        (left, top, width, height) or (width, height)
        """
        from_size = kwargs.get('from_size', False)
        if len(args) == 1:
            xywh = args[0]
        else:
            xywh = args
        if isinstance(xywh, ScreenRect):
            self.left = xywh.left
            self.top = xywh.top
            self.width = xywh.width
            self.height = xywh.height
        else:
            if len(xywh) == 4:
                if from_size:
                    self.left, self.top, self.width, self.height = (int(i) for i in xywh)
                else:
                    x = list(int(i) for i in xywh)
                    self.left, self.top, self.width, self.height = (x[0], x[1], x[2] - x[0], x[3] - x[1])
            elif len(xywh) == 2:
                self.left, self.top, self.width, self.height = (0, 0) + tuple(int(i) for i in xywh)


    def __repr__(self):
        return "%s((%s,%s,%s,%s))" % (self.__class__.__name__, self.left, self.top, self.right, self.bottom)

    def __iter__(self):
        return (i for i in (self.left, self.top, self.right, self.bottom))

    def set_bottom(self, s):
        self.top = s - self.height
    def get_bottom(self):
        return self.top + self.height
    bottom = property(get_bottom, set_bottom)

    def set_right(self, s):
        self.left = s - self.width
    def get_right(self):
        return self.left + self.width
    right = property(get_right, set_right)

    def set_center(self, xy):
        self.left = xy[0] - (self.width * 0.5)
        self.top = xy[1] - (self.height * 0.5)
    def get_center(self):
        return self.left + (self.width * 0.5), self.top + (self.height * 0.5)
    center = property(get_center, set_center)

    def set_bottomleft(self, xy):
        self.left = xy[0]
        self.bottom = xy[1]
    def get_bottomleft(self):
        return self.left, self.bottom
    bottomleft = property(get_bottomleft, set_bottomleft)

    def set_bottomright(self, xy):
        self.right = xy[0]
        self.bottom = xy[1]
    def get_bottomright(self):
        return self.right, self.bottom
    bottomright = property(get_bottomright, set_bottomright)

    def set_topright(self, xy):
        self.right = xy[0]
        self.top = xy[1]
    def get_topright(self):
        return self.right, self.top
    topright = property(get_topright, set_topright)

    def set_topleft(self, xy):
        self.left = xy[0]
        self.top = xy[1]
    def get_topleft(self):
        return self.left, self.top
    topleft = property(get_topleft, set_topleft)

    def __add__(self, other):
        left = min(self.left, other.left)
        top = min(self.top, other.top)
        right = max(self.right, other.right)
        bottom = max(self.bottom, other.bottom)
        return ScreenRect((left, top, right - left, bottom - top))

    def add(self, other):
        """
        Add another rect to this rect, expanding as needed.
        """
        self.left = min(self.left, other.left)
        self.top = min(self.top, other.top)
        self.width = max(self.right, other.right) - self.left
        self.height = max(self.bottom, other.bottom) - self.top

    @classmethod
    def sum(cls, others):
        """
        Return a rect which covers all rects in others.
        """
        others = list(others)
        left, top, width, height = others.pop()
        right = left + width
        bottom = top + height
        for other in others:
            if other.left < left: left = other.left
            if other.top < top: top = other.top
            if other.right > right: right = other.right
            if other.bottom > bottom: bottom = other.bottom
        return cls((left, top, right - left, bottom - top))

    def collidepoint(self, xy):
        """
        Test if a point intersects with this rect.
        """
        x, y = xy
        return x >= self.left and x <= (self.left + self.width) and y >= self.top and y <= (self.top + self.height)

    def intersects(self, other):
        """
        Test if a rect intersects with this rect.
        """
        if self.left > other.left + other.width: return False
        if self.top > other.top + other.height: return False
        if self.left + self.width < other.left: return False
        if self.top + self.height < other.top: return False
        return True 

    def get_area(self):
        return self.width * self.height
    area = property(get_area)

    def intersection(self, other):
        """
        Return the intersection of this rect and other rect.
        Return None if no intersection.
        """
        left = max((self.left, other.left))
        top = max((self.top, other.top))
        right = min((self.left + self.width, other.left + other.width))
        bottom = min((self.top + self.height, other.top + other.height))
        if left > right or bottom < top: return None
        return ScreenRect((left, top, right - left, bottom - top))

    def contains(self, other):
        """
        Return True if other contains self
        """
        if other.left >= self.left and other.right <= self.right:
            if other.bottom <= self.bottom and other.top >= self.top:
                return True
        return False

    def fits(self, other):
        return self.width >= other.width and self.height >= other.height

    ####################################################################
    # new methods
    ####################################################################
    def __getitem__(self, i):
        x = (self.left, self.top, self.right, self.bottom)
        return x[i]

    @classmethod
    def from_points(cls, obj):
        """
        create from points:
        (left,top,right,bottom)
        """
        return cls((obj[0], obj[1], obj[2] - obj[0], obj[3] - obj[1]))

    def __len__(self):
        return 4
    
    def move(self, vector):
        self.left += vector[0]
        self.top += vector[1]
    
    def __eq__(self, other):
        x = (self.left, self.top, self.right, self.bottom)
        y = (other.left, other.top, other.right, other.bottom)        
        return all(a == b for a, b in zip(x, y))
    
    def point_inside(self, point):
        """
        Return True if self contains point
        """
        if point[0] >= self.left and point[0] <= self.right:
            if point[1] <= self.bottom and point[1] >= self.top:
                return True
        return False

    def add_border(self, border=1):
        """
        Return Rect
        """
        new = ScreenRect(self)
        new.left -= border
        new.top -= border
        new.width += 2 * border
        new.height += 2 * border
        return new

    
    
    
    
    
    
    
