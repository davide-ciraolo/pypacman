from tkinter import *

PACMAN_TILE_SPAWN = 32
PACMAN_SPEED = 3.25
PACMAN_LIVES = 3

SMALL_POINT = 10
BIG_POINT = 50
FRUIT_CHERRY_POINT = 100
FRUIT_STRAWBERRY_POINT = 200

#directions
DIR_RIGHT = 0
DIR_DOWN = 1
DIR_LEFT = 2
DIR_UP = 3

class Pacman():

    def __init__(self, master, tileSet):

        self._last_pdir = -1
        self._dir = DIR_RIGHT
        self._vel = PACMAN_SPEED
        self._actTile = 0
        self._Lives = PACMAN_LIVES
        self._isAlive = False
        self._score = 0
        self._startInvincible = False
        self._isInvincible = False

        self._spawn_tile = -1
        self._spawn_x = 50
        self._spawn_y = 50

        self._pos_x = 0
        self._pos_y = 0

        self._actFrame = 0

        self._tileSet = tileSet
        self._frame = {}

        self._frame[0] = self._tileSet._tiles[11]

        self._frame[1] = self._tileSet._tiles[12]
        self._frame[2] = self._tileSet._tiles[13]

        self._frame[3] = self._tileSet._tiles[66]
        self._frame[4] = self._tileSet._tiles[67]

        self._frame[5] = self._tileSet._tiles[68]
        self._frame[6] = self._tileSet._tiles[69]

        self._frame[7] = self._tileSet._tiles[70]
        self._frame[8] = self._tileSet._tiles[71]

        self._frame[9] = self._tileSet._tiles[72]
        self._frame[10] = self._tileSet._tiles[73]
        self._frame[11] = self._tileSet._tiles[74]

        self._frame[12] = self._tileSet._tiles[77]
        self._frame[13] = self._tileSet._tiles[76]
        self._frame[14] = self._tileSet._tiles[75]

        self._palette = self._tileSet.get_palette()
        self._pacFrame = Canvas(master = master._mapFrame,width=self._tileSet.get_wsize(), height=self._tileSet.get_hsize(),bg = "black", bd=0, highlightthickness=0, relief='ridge')
        self._p_obj = self._pacFrame.create_image(self._frame[self._actFrame].get_x(),self._frame[self._actFrame].get_y(),image=self._palette,anchor=NW)
        self._map = master

        self._LivesBoard = Frame(master=self._map._mapFrame, width=(self._tileSet.get_wsize() + 2) * self._Lives, height=self._tileSet.get_hsize(), bg="black")
        self._LivesBoard.place(relx = 0.1, rely = 0.935)

        self._LiveCanvas = {}

        self._draw_lives()
        self.get_spawn()

    def get_last_dir(self):
        return self._last_pdir
    def set_last_dir(self, d = DIR_LEFT):
        self._last_pdir = d

    def get_dir(self):
        return self._dir
    def set_dir(self, d = DIR_RIGHT):
        self._dir = d

    def get_vel(self):
        return self._vel
    def set_vel(self, vel = 1.0):
        self._vel = vel

    def get_actTile(self):
        return self._actTile
    def set_actTile(self, id):
        self._actTile = id

    def get_Lives(self):
        return self._Lives
    def set_Lives(self, lives = 1):
        self._Lives = lives
        self._refresh_lives()

    def get_isAlive(self):
        return self._isAlive
    def set_isAlive(self, bool):
        self._isAlive = bool

    def get_score(self):
        return self._score
    def set_score(self, n = 0):
        self._score = n
    def add_score(self, n = 0):
        self._score += n
    def reset_score(self):
        self._score = 0

    def set_actFrame(self, f_id = 0):
        self._actFrame = f_id
    def get_actFrame(self):
        return self._actFrame

    def set_startInvincible(self, bool):
        self._startInvincible = bool
    def get_startInvincible(self):
        return self._startInvincible

    def set_isInvincible(self, bool):
        self._isInvincible = bool
    def get_isInvincible(self):
        return self._isInvincible

    def set_pos_x(self, x = 0.0):
        self._pos_x = x
    def get_pos_x(self):
        return self._pos_x

    def set_pos_y(self, y = 0.0):
        self._pos_y = y
    def get_pos_y(self):
        return self._pos_y

    def set_spawn_x(self, x = 0.0):
        self._spawn_x = x
    def get_spawn_x(self):
        return self._spawn_x

    def set_spawn_y(self, y = 0.0):
        self._spawn_y = y
    def get_spawn_y(self):
        return self._spawn_y

    def set_spawn_tile(self, t_id):
        self._spawn_tile = t_id
    def get_spawn_tile(self):
        return self._spawn_tile

    def set_tileSet(self, tileSet = None):
        self._tileSet = tileSet

    def get_tileSet(self):
        return self._tileSet

    def set_palette(self, palette = None):
        self._palette = palette

    def get_palette(self):
        return self._palette

    def set_frame(self, f_id, n_frame = None):
        if f_id >= 0 and f_id <= len(self._frame):
                self._frame[f_id] = n_frame

    def get_frame(self, f_id):
        return self._frame[f_id]

    def set_p_obj(self, p_obj = 0):
        self._p_obj = p_obj

    def get_p_obj(self):
        return self._p_obj

    def set_map(self, map = None):
        self._map = map

    def get_map(self):
        return self._map

    def get_pacFrame(self):
        return self._pacFrame

    def set_pacFrame(self, canvas):
        self._pacFrame = canvas

    def get_LivesBoard(self):
        return self._LivesBoard

    def set_LivesBoard(self, frame):
        self._LivesBoard = frame

    def get_LiveCanvas(self, id):
        return self._LiveCanvas[id]

    def set_LiveCanvas(self, id, canvas):
        self._LiveCanvas[id] = canvas

    def reset_lives(self):
        self._Lives = PACMAN_LIVES
        self._refresh_lives()

    def _refresh_lives(self):
        self._delete_lives()
        self._draw_lives()

    def _delete_lives(self):
        for i in range(0, self._Lives):
            self._LiveCanvas[i].destroy()

    def _draw_lives(self):
        for i in range(0, self._Lives):
            self._LiveCanvas[i] = Canvas(master=self._LivesBoard, width= self._tileSet.get_wsize(), height=self._tileSet.get_hsize(),bg="black", bd=0, highlightthickness=0, relief='ridge')
            self._LiveCanvas[i].create_image(self._frame[2].get_x(), self._frame[2].get_y(), image=self._palette, anchor=NW)
            self._LiveCanvas[i].place(x=i*(self._tileSet.get_wsize() + 2), y=0)

    def Dead(self):
        if self._Lives - 1 > - 1:
            self._LiveCanvas[self._Lives - 1].destroy()
        if self._dir != 5:
            self._Lives = self._Lives - 1
            self._actFrame = 0
            self._dir = 5

    def reset_spawn(self):
        self._spawn_tile = -1
        self.get_spawn()

    def get_spawn(self):
        for i in range(0, self._map._t_count_y):
            for j in range(0, self._map._t_count_x):
                if self._map._TileFrame[(i * self._map._t_count_x) + j].get_t_id() == PACMAN_TILE_SPAWN:
                    self._spawn_x = self._tileSet.get_wsize() * j
                    self._spawn_y = self._tileSet.get_hsize() * i
                    self._map.set_tile(((i * self._map._t_count_x) + j), 4)
                    self._spawn_tile = (i * self._map._t_count_x) + j
                    break
            if self._spawn_tile != -1:
                break

        self._pos_x = self._spawn_x
        self._pos_y = self._spawn_y

        self._actFrame = 0

        self._pacFrame.delete(self._p_obj)
        self._p_obj = self._pacFrame.create_image(self._frame[self._actFrame].get_x(),self._frame[self._actFrame].get_y(),image=self._palette,anchor=NW)

        self._pacFrame.place(x = self._spawn_x, y = self._spawn_y)

    def spawn(self):
        self.get_spawn()
        self._actFrame = 0
        self._actTile = self._spawn_tile
        self._dir = 0
        self._isAlive = True

    def changedir(self, n_dir):

        self._last_pdir = n_dir

        if self._isAlive == True:
            if n_dir != self._dir:

                if n_dir == 0:
                    a = self._actTile + 1

                    if self.check_walkable(a) == 1:
                        if self._dir == 1 or self._dir == 3:
                            if self._pos_x == (self._actTile % self._map._t_count_x) * self._tileSet.get_wsize() and self._pos_y == int(self._actTile / self._map._t_count_x) * self._tileSet.get_hsize():
                                self._dir = n_dir
                                self._last_pdir = -1
                        else:
                            self._dir = n_dir
                            self._last_pdir = -1
                elif n_dir == 1:
                    a = self._actTile + self._map._t_count_x

                    if self.check_walkable(a) == 1:
                        if self._dir == 0 or self._dir == 2:
                            if self._pos_x == (self._actTile % self._map._t_count_x) * self._tileSet.get_wsize() and self._pos_y == int(self._actTile / self._map._t_count_x) * self._tileSet.get_hsize():
                                self._dir = n_dir
                                self._last_pdir = -1
                        else:
                            self._dir = n_dir
                            self._last_pdir = -1
                elif n_dir == 2:
                    a = self._actTile -1

                    if self.check_walkable(a) == 1:
                        if self._dir == 1 or self._dir == 3:
                            if self._pos_x == (self._actTile % self._map._t_count_x) * self._tileSet.get_wsize() and self._pos_y == int(self._actTile / self._map._t_count_x) * self._tileSet.get_hsize():
                                self._dir = n_dir
                                self._last_pdir = -1
                        else:
                            self._dir = n_dir
                            self._last_pdir = -1
                elif n_dir == 3:
                    a = self._actTile - self._map._t_count_x

                    if self.check_walkable(a) == 1:
                        if self._dir == 0 or self._dir == 2:
                            if self._pos_x == (self._actTile % self._map._t_count_x) * self._tileSet.get_wsize() and self._pos_y == int(self._actTile / self._map._t_count_x) * self._tileSet.get_hsize():
                                self._dir = n_dir
                                self._last_pdir = -1
                        else:
                            self._dir = n_dir
                            self._last_pdir = -1

                if self._dir == 0:
                    self._actFrame = 0
                elif self._dir == 1:
                    self._actFrame = 12
                elif self._dir == 2:
                    self._actFrame = 13
                elif self._dir == 3:
                    self._actFrame = 14
                elif self._dir == 5:
                    self._actFrame = 0

    def check_tile(self, t_id):

        a = self._map._TileFrame[t_id].get_t_id()

        if a == 4:
            return
        elif a == 0:
            self._score += SMALL_POINT
            self._map.set_tile(t_id, 4)
            self._map._mapPoints -= 1
        elif a == 1:
            self._score += BIG_POINT
            self._map.set_tile(t_id, 4)
            self._map._mapPoints -= 1
            self._startInvincible = True
            #self._isInvincible = True
        elif a == 2:
            self._score += FRUIT_STRAWBERRY_POINT
            self._map.set_tile(t_id, 5)
            self._map._fruit_spawned = False
        elif a == 3:
            self._score += FRUIT_CHERRY_POINT
            self._map.set_tile(t_id, 5)
            self._map._fruit_spawned = False
        elif a == 54:
            if self._dir == 0:
                self._pos_x =  ((t_id - (self._map._t_count_x - 2)) % self._map._t_count_x) * self._tileSet.get_wsize()
                self._pos_y =  int((t_id - (self._map._t_count_x - 2)) / self._map._t_count_x) * self._tileSet.get_hsize()
                self._actTile = t_id - (self._map._t_count_x - 2)
            elif self._dir == 2:
                self._pos_x =  ((t_id + (self._map._t_count_x - 2)) % self._map._t_count_x) * self._tileSet.get_wsize()
                self._pos_y =  int((t_id + (self._map._t_count_x - 2)) / self._map._t_count_x) * self._tileSet.get_hsize()
                self._actTile = t_id + (self._map._t_count_x - 2)

    def check_walkable(self, t_id):
        a = self._map._TileFrame[t_id].get_t_id()
        if a >= 0 and a <= 5:
            return 1
        else:
            return 0

    def RefreshFrame(self):
        temp = self._pacFrame.create_image(self._frame[self._actFrame].get_x(), self._frame[self._actFrame].get_y(), image=self._palette, anchor = NW)
        self._pacFrame.place_configure(x = self._pos_x, y = self._pos_y)
        self._pacFrame.delete(self._p_obj)
        self._p_obj = temp

    def _render(self):

        if self._isAlive == True:

            if self._dir == 0:
                if self._actFrame == 0:
                    self._actFrame = 1
                elif self._actFrame == 1:
                    self._actFrame = 2
                elif self._actFrame == 2:
                    self._actFrame = 0
            elif self._dir == 1:
                if self._actFrame == 12:
                    self._actFrame = 3
                elif self._actFrame == 3:
                    self._actFrame = 4
                elif self._actFrame == 4:
                    self._actFrame = 12
            elif self._dir == 2:
                if self._actFrame == 13:
                    self._actFrame = 7
                elif self._actFrame == 7:
                    self._actFrame = 8
                elif self._actFrame == 8:
                    self._actFrame = 13
            elif self._dir == 3:
                if self._actFrame == 14:
                    self._actFrame = 5
                elif self._actFrame == 5:
                    self._actFrame = 6
                elif self._actFrame == 6:
                    self._actFrame = 14
            elif self._dir == 5:
                if self._actFrame == 0:
                    self._actFrame = 5
                elif self._actFrame == 5:
                    self._actFrame = 6
                elif self._actFrame == 6:
                    self._actFrame = 9
                elif self._actFrame == 9:
                    self._actFrame = 10
                elif self._actFrame == 10:
                    self._actFrame = 11
                    self._isAlive = False

            if self._dir == 0:
                a = self._actTile + 1

                if self.check_walkable(a) == 1:
                    self._pos_x += self._vel

                    if self._pos_x + 8 >= ((self._actTile % self._map._t_count_x) + 1) * self._tileSet.get_wsize():
                        self.check_tile(self._actTile + 1)

                    if self._pos_x == ((self._actTile % self._map._t_count_x) + 1) * self._tileSet.get_wsize():
                        self._actTile = self._actTile + 1
                        if self._last_pdir != -1:
                            self.changedir(self._last_pdir)

                        self._last_pdir = -1
                else:
                    self.check_tile(self._actTile + 1)


            elif self._dir == 1:
                a = self._actTile + self._map._t_count_x

                if self.check_walkable(a) == 1:
                    self._pos_y += self._vel

                    if self._pos_y + 8 >= (int(self._actTile / self._map._t_count_x) + 1) * self._tileSet.get_hsize():
                        self.check_tile(self._actTile + self._map._t_count_x)

                    if self._pos_y == (int(self._actTile / self._map._t_count_x) + 1) * self._tileSet.get_hsize():
                        self._actTile = self._actTile + self._map._t_count_x
                        if self._last_pdir != -1:
                            self.changedir(self._last_pdir)

                        self._last_pdir = -1

            elif self._dir == 2:
                a = self._actTile -1

                if self.check_walkable(a) == 1:
                    self._pos_x -= self._vel

                    if self._pos_x - 8 <= ((self._actTile % self._map._t_count_x) - 1) * self._tileSet.get_wsize():
                        self.check_tile(self._actTile - 1)

                    if self._pos_x == ((self._actTile % self._map._t_count_x) - 1) * self._tileSet.get_wsize():
                        self._actTile = self._actTile - 1
                        if self._last_pdir != -1:
                            self.changedir(self._last_pdir)

                        self._last_pdir = -1
                else:
                    self.check_tile(self._actTile - 1)

            elif self._dir == 3:
                a = self._actTile - self._map._t_count_x

                if self.check_walkable(a) == 1:
                    self._pos_y -= self._vel

                    if self._pos_y - 8 <= (int(self._actTile / self._map._t_count_x) - 1) * self._tileSet.get_hsize():
                        self.check_tile(self._actTile - self._map._t_count_x)

                    if self._pos_y == (int(self._actTile / self._map._t_count_x) - 1) * self._tileSet.get_hsize():
                        self._actTile = self._actTile - self._map._t_count_x
                        if self._last_pdir != -1:
                            self.changedir(self._last_pdir)

                        self._last_pdir = -1

            self.RefreshFrame()