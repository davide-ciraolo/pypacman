import random

def AI_p_ghost(self):

        random.seed(version=2)

        d = {}

        d[0] = False
        d[1] = False
        d[2] = False
        d[3] = False
        d[4] = False
        d[5] = False

        p = {}

        k = 0

        a = self._actTile + 1

        if self.check_walkable(a) == 1:
            d[0] = True
            p[k] = 0
            k += 1

        a = self._actTile + self._map._t_count_x

        if self.check_walkable(a) == 1:
            d[1] = True
            p[k] = 1
            k += 1

        a = self._actTile - 1

        if self.check_walkable(a) == 1:
            d[2] = True
            p[k] = 2
            k += 1

        a = self._actTile - self._map._t_count_x

        if self.check_walkable(a) == 1:
            d[3] = True
            p[k] = 3
            k += 1

        if k == 1:
            a = p[0]
        else:
            a = random.randrange(p[0], p[k - 1])

        g = random.randint(0, 100)

        if (self._Enemy._dir == 0 or self._Enemy._dir == 2) and d[self._Enemy._dir] == True:
            a = self._Enemy._dir
        else:
            if g >= 0 and g <= 50 and d[self._Enemy._dir] == True and self._Enemy._dir != 5:
                a = self._Enemy._dir
            elif g > 50 and g <= 90 and d[self._dir] == True:
                a = self._dir
            else:
                for i in range(0, 3):
                    if d[i] == True:
                        a = i
                        break

        self.change_dir(a)

def AI_o_ghost(self):

        random.seed(version=2)

        d = {}

        d[0] = False
        d[1] = False
        d[2] = False
        d[3] = False
        d[4] = False
        d[5] = False

        p = {}

        k = 0

        a = self._actTile + 1

        if self.check_walkable(a) == 1:
            d[0] = True
            p[k] = 0
            k += 1

        a = self._actTile + self._map._t_count_x

        if self.check_walkable(a) == 1:
            d[1] = True
            p[k] = 1
            k += 1

        a = self._actTile - 1

        if self.check_walkable(a) == 1:
            d[2] = True
            p[k] = 2
            k += 1

        a = self._actTile - self._map._t_count_x

        if self.check_walkable(a) == 1:
            d[3] = True
            p[k] = 3
            k += 1
        if k == 1:
            a = p[0]
        else:
            a = random.randrange(p[0], p[k - 1])

        g = random.randint(0, 100)

        if (self._Enemy._dir == 1 or self._Enemy._dir == 3) and d[self._Enemy._dir] == True:
            a = self._Enemy._dir
        else:
            if g >= 0 and g <= 50 and d[self._Enemy._dir] == True and self._Enemy._dir != 5:
                a = self._Enemy._dir
            elif g > 50 and g <= 75 and d[self._dir] == True:
                a = self._dir
            else:
                for i in range(0, 3):
                    if d[i] == True:
                        a = i
                        break

        self.change_dir(a)

def AI_b_ghost(self):

        random.seed(version=2)

        d = {}

        d[0] = False
        d[1] = False
        d[2] = False
        d[3] = False
        d[4] = False
        d[5] = False

        p = {}

        k = 0

        a = self._actTile + 1

        if self.check_walkable(a) == 1:
            d[0] = True
            p[k] = 0
            k += 1

        a = self._actTile + self._map._t_count_x

        if self.check_walkable(a) == 1:
            d[1] = True
            p[k] = 1
            k += 1

        a = self._actTile - 1

        if self.check_walkable(a) == 1:
            d[2] = True
            p[k] = 2
            k += 1

        a = self._actTile - self._map._t_count_x

        if self.check_walkable(a) == 1:
            d[3] = True
            p[k] = 3
            k += 1

        if k == 1:
            a = p[0]
        else:
            a = random.randrange(p[0], p[k - 1])

        g = random.randint(0, 100)

        if (self._Enemy._dir == 0 or self._Enemy._dir == 2) and d[self._Enemy._dir + 1] == True:
            a = self._Enemy._dir + 1
        else:
            if g >= 0 and g <= 50 and d[self._Enemy._dir] == True and self._Enemy._dir != 5:
                a = self._Enemy._dir
            elif g > 50 and g <= 90 and d[self._dir] == True:
                a = self._dir
            else:
                for i in range(0, 3):
                    if d[i] == True:
                        a = i
                        break

        self.change_dir(a)

def AI_r_ghost(self):

        random.seed(version=2)

        d = {}

        d[0] = False
        d[1] = False
        d[2] = False
        d[3] = False
        d[4] = False
        d[5] = False

        p = {}

        k = 0

        a = self._actTile + 1

        if self.check_walkable(a) == 1:
            d[0] = True
            p[k] = 0
            k += 1

        a = self._actTile + self._map._t_count_x

        if self.check_walkable(a) == 1:
            d[1] = True
            p[k] = 1
            k += 1

        a = self._actTile - 1

        if self.check_walkable(a) == 1:
            d[2] = True
            p[k] = 2
            k += 1

        a = self._actTile - self._map._t_count_x

        if self.check_walkable(a) == 1:
            d[3] = True
            p[k] = 3
            k += 1

        if k == 1:
            a = p[0]
        else:
            a = random.randrange(p[0], p[k - 1])

        g = random.randint(0, 100)

        if self._Enemy._dir != 5 and d[self._Enemy._dir] == True:
            a = self._Enemy._dir
        else:
            if g >= 0 and g <= 80 and d[self._Enemy._dir] == True and self._Enemy._dir != 5:
                a = self._Enemy._dir
            elif g > 80 and g <= 90 and d[self._dir] == True:
                a = self._dir
            else:
                for i in range(0, 3):
                    if d[i] == True:
                        a = i
                        break

        self.change_dir(a)