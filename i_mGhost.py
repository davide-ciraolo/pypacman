from tkinter import *
from time import sleep
from threading import Thread

GHOST_SPEED = 3.25
GHOST_COLOR_PINK = 0
GHOST_COLOR_ORANGE = 4
GHOST_COLOR_BLUE = 8
GHOST_COLOR_RED = 12

GHOST_POINT = 200
ghost_mult = 1

class Ghost():

    def __init__(self, master, tileSet, c_type, AI_func):
        self._c_type = c_type
        self._vel = GHOST_SPEED
        self._isVulnerable = False
        self._isAlive = False
        self._isDead = False
        self._AIfunc = AI_func
        self._Enemy = None

        self._dir = 0
        self._last_dir = 2

        self._pos_x = 0.0
        self._pos_y = 0.0
        self._spawn_x = 0.0
        self._spawn_y = 0.0
        self._spawn_tile = -1
        self._actTile = 0
        self._actFrame = c_type

        self._tileSet = tileSet
        self._palette = tileSet._palette
        self._frame = {}

        #pink_ghost
        #destra(0)
        self._frame[0] = self._tileSet._tiles[25]
        #giù(1)
        self._frame[1] = self._tileSet._tiles[22]
        #sinistra(2)
        self._frame[2] = self._tileSet._tiles[24]
        #su(3)
        self._frame[3] = self._tileSet._tiles[23]

        #orange_ghost
        #destra(0)
        self._frame[4] = self._tileSet._tiles[36]
        #giù(1)
        self._frame[5] = self._tileSet._tiles[33]
        #sinistra(2)
        self._frame[6] = self._tileSet._tiles[35]
        #su(3)
        self._frame[7] = self._tileSet._tiles[34]

        #blue_ghost
        #destra(0)
        self._frame[8] = self._tileSet._tiles[47]
        #giù(1)
        self._frame[9] = self._tileSet._tiles[44]
        #sinistra(2)
        self._frame[10] = self._tileSet._tiles[46]
        #su(3)
        self._frame[11] = self._tileSet._tiles[45]

        #red_ghost
        #destra(0)
        self._frame[12] = self._tileSet._tiles[58]
        #giù(1)
        self._frame[13] = self._tileSet._tiles[55]
        #sinistra(2)
        self._frame[14] = self._tileSet._tiles[57]
        #su(3)
        self._frame[15] = self._tileSet._tiles[56]

        #vulnerable
        self._frame[16] = self._tileSet._tiles[14]

        #died_ghost
        #destra(0)
        self._frame[17] = self._tileSet._tiles[64]
        #giù(1)
        self._frame[18] = self._tileSet._tiles[61]
        #sinistra(2)
        self._frame[19] = self._tileSet._tiles[63]
        #su(3)
        self._frame[20] = self._tileSet._tiles[62]

        self._ghostCanvas = Canvas(master=master._mapFrame,width=self._tileSet.get_wsize(), height=self._tileSet.get_hsize(),bd=0, highlightthickness=0, relief='ridge')
        self._g_obj = self._ghostCanvas.create_image(self._frame[self._actFrame].get_x(), self._frame[self._actFrame].get_y(),image=self._palette,anchor=NW)
        self._map = master

        self.get_spawn()

    def set_c_type(self, color = 0):
        self._c_type = color

    def get_c_type(self):
        return self._c_type

    def set_vel(self, vel = 1.0):
        self._vel = vel

    def get_vel(self):
        return self._vel

    def set_isVulnerable(self, bool = False):
        self._isVulnerable = bool

    def get_isVulnerable(self):
        return self._isVulnerable

    def set_isAlive(self, bool = False):
        self._isAlive = bool

    def get_isAlive(self):
        return self._isAlive

    def set_isDead(self, dead = False):
        self._isDead = dead

    def get_isDead(self):
        return self._isDead

    def set_AIfunc(self, func = None):
        self._AIfunc = func

    def get_AIfunc(self):
        return self._AIfunc

    def set_Enemy(self, enemy = None):
        self._Enemy = enemy

    def get_Enemy(self):
        return self._Enemy

    def set_dir(self, dir = 0):
        self._dir = dir

    def get_dir(self):
        return self._dir

    def set_last_dir(self, dir = 0):
        self._last_dir = dir

    def get_last_dir(self):
        return self._last_dir

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

    def set_actTile(self, t_id = 0):
        self._actTile = t_id

    def get_actTile(self):
        return self._actTile

    def set_actFrame(self, f_id = 0):
        self._actFrame = f_id

    def get_actFrame(self):
        return self._actFrame

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

    def set_ghostCanvas(self, canvas = None):
        self._ghostCanvas = canvas

    def get_ghostCanvas(self):
        return self._ghostCanvas

    def set_g_obj(self, g_obj = 0):
        self._g_obj = g_obj

    def get_g_obj(self):
        return self._g_obj

    def set_map(self, map = None):
        self._map = map

    def get_map(self):
        return self._map

    def reset_spawn(self):
        self._spawn_tile = -1
        self.get_spawn()

    def thread_ghost(self):

        while self._isAlive == False:
            sleep(0.05)

        self._AIfunc(self)

        while self._isAlive == True:
            sleep(0.05)
            self._render()

    def get_spawn(self):

        for i in range(0, self._map._t_count_y):
            for j in range(0, self._map._t_count_x):
                if self._map._TileFrame[(i * self._map._t_count_x) + j].get_t_id() == 43:
                    self._map.set_tile((i * self._map._t_count_x) + j, 65)
                    self._spawn_tile = (i * self._map._t_count_x) + j
                    self._spawn_x = self._tileSet.get_wsize() * j
                    self._spawn_y = self._tileSet.get_hsize() * i
                    break
            if self._spawn_tile != -1:
                break

        self._pos_x = self._spawn_x
        self._pos_y = self._spawn_y

        self._actFrame = self._c_type

        self._actTile = self._spawn_tile

        self._ghostCanvas.delete(self._g_obj)
        self._g_obj = self._ghostCanvas.create_image(self._frame[self._actFrame].get_x(),self._frame[self._actFrame].get_y(),image=self._palette,anchor=NW)

        self._ghostCanvas.place(x = self._spawn_x, y = self._spawn_y)

    def spawn(self):
        self.get_spawn()
        self._ghostThread = Thread(target = self.thread_ghost, args = ())
        self._ghostThread.setDaemon(daemonic = True)
        self._ghostThread.start()
        self._actFrame = self._c_type
        self._actTile = self._spawn_tile
        self._dir = 0
        self._last_dir = 2
        self._isAlive = True

    def check_EnemyCollision(self):
        global ghost_mult

        if self._pos_x >= self._Enemy._pos_x + 13 and self._pos_x <= self._Enemy._pos_x + 26 and (self._pos_y >= self._Enemy._pos_y and self._pos_y <= self._Enemy._pos_y + 26):
            if self._isVulnerable == False:
                if self._Enemy._dir != 5:
                    self._Enemy.Dead()
            else:
                if self._isDead == False:
                    self._Enemy.add_score(int(GHOST_POINT * ghost_mult))
                    ghost_mult = ghost_mult * 2
                    if ghost_mult > 4 * 2:
                        ghost_mult = 1
                    self.set_isDead(True)
                    self.set_pos_x(int(self._map._TileFrame[self._actTile].get_x()))
                    self.set_pos_y(int(self._map._TileFrame[self._actTile].get_y()))
                    self._refresh_speed()

            return

        if self._pos_x + 26 >= self._Enemy._pos_x + 13 and self._pos_x + 26 <= self._Enemy._pos_x + 26 and (self._pos_y >= self._Enemy._pos_y and self._pos_y <= self._Enemy._pos_y + 26):
            if self._isVulnerable == False:
                if self._Enemy._dir != 5:
                    self._Enemy.Dead()
            else:

                if self._isDead == False:
                    self._Enemy.add_score(int(GHOST_POINT * ghost_mult))
                    ghost_mult = ghost_mult * 2
                    if ghost_mult > 4 * 2:
                        ghost_mult = 1
                    self.set_isDead(True)
                    self.set_pos_x(int(self._map._TileFrame[self._actTile].get_x()))
                    self.set_pos_y(int(self._map._TileFrame[self._actTile].get_y()))
                    self._refresh_speed()

            return

        if self._pos_y >= self._Enemy._pos_y + 13 and self._pos_y <= self._Enemy._pos_y + 26 and (self._pos_x >= self._Enemy._pos_x and self._pos_x <= self._Enemy._pos_x + 26):
            if self._isVulnerable == False:
                if self._Enemy._dir != 5:
                    self._Enemy.Dead()

            else:
                if self._isDead == False:
                    self._Enemy.add_score(int(GHOST_POINT * ghost_mult))
                    ghost_mult = ghost_mult * 2
                    if ghost_mult > 4 * 2:
                        ghost_mult = 1
                    self.set_isDead(True)
                    self.set_pos_x(int(self._map._TileFrame[self._actTile].get_x()))
                    self.set_pos_y(int(self._map._TileFrame[self._actTile].get_y()))
                    self._refresh_speed()

            return

        if self._pos_y + 26 >= self._Enemy._pos_y + 13 and self._pos_y + 26 <= self._Enemy._pos_y + 26 and (self._pos_x >= self._Enemy._pos_x and self._pos_x <= self._Enemy._pos_x + 26):
            if self._isVulnerable == False:
                if self._Enemy._dir != 5:
                    self._Enemy.Dead()
            else:
                if self._isDead == False:
                    self._Enemy.add_score(int(GHOST_POINT * ghost_mult))
                    ghost_mult = ghost_mult * 2
                    if ghost_mult > 4 * 2:
                        ghost_mult = 1
                    self.set_isDead(True)
                    self.set_pos_x(int(self._map._TileFrame[self._actTile].get_x()))
                    self.set_pos_y(int(self._map._TileFrame[self._actTile].get_y()))
                    self._refresh_speed()

            return

    def check_walkable(self, t_id):
        a = self._map._TileFrame[t_id].get_t_id()
        if a >= 0 and a <= 5 or a == 65:
            return 1
        else:
            return 0

    def change_dir(self, n_dir):

        a = -1

        if n_dir == self._dir:
            return -1

        if self._dir == 0 or self._dir == 2:

            if n_dir == 1:
                a = self._actTile + self._map._t_count_x
            elif n_dir == 3:
                a = self._actTile - self._map._t_count_x

        elif self._dir == 1 or self._dir ==3:

            if n_dir == 0:
                a = self._actTile + 1
            elif n_dir == 2:
                a = self._actTile - 1

        if a != -1:
            if self.check_walkable(a) == 1:
                self._last_dir = self._dir
                self._dir = n_dir
            else:
                return -1
        elif a == -1:
            self._last_dir = self._dir
            self._dir = n_dir

    def _refresh_speed(self):
        if self._isVulnerable == False and self._isDead == False:
            self.set_vel(GHOST_SPEED)
        elif self._isVulnerable == True and self._isDead == False:
            self.set_vel(GHOST_SPEED / 2)
        elif self._isDead == True:
            self.set_vel(GHOST_SPEED * 2)

    def revive(self, t_id = 0):

            if self.get_pos_x() < self.get_spawn_x():
                self._pos_x += self._vel

            elif self.get_pos_x() > self.get_spawn_x():
                self._pos_x -= self._vel

            if self.get_pos_y() < self.get_spawn_y():
                self._pos_y += self._vel

            elif self.get_pos_y() > self.get_spawn_y():
                self._pos_y -= self._vel

            #if self.get_pos_x() + 13 >= self.get_spawn_x() and self.get_pos_x() <= self.get_spawn_x() + 13:
            #    self.set_pos_x(int(self.get_spawn_x()))

            #if self.get_pos_y() + 13 >= self.get_spawn_y() and self.get_pos_y() <= self.get_spawn_y() + 13:
            #   self.set_pos_y(int(self.get_spawn_y()))

            if self.get_pos_x() == self.get_spawn_x() and self.get_pos_y() == self.get_spawn_y():
                self.set_actTile(int(self.get_spawn_tile()))
                self.set_isDead(False)
                self.set_isVulnerable(False)

    def _refresh_actTile(self, t_id):
        if self._pos_x == self._map._TileFrame[t_id].get_x() and self._pos_y == self._map._TileFrame[t_id].get_y():#((self._actTile % self._map._t_count_x) + 1) * self._tileSet.get_wsize():
            self.set_actTile(t_id)
            self._refresh_speed()
            self._AIfunc(self)

    def _render(self):

        global ghost_mult

        if self._isDead == False:

            if self._dir == 0:
                a = self._actTile + 1

                if self.check_walkable(a) == 1:
                    self._pos_x += self._vel
                    self._refresh_actTile(a)

                else:
                    self._AIfunc(self)

            elif self._dir == 1:
                a = self._actTile + self._map._t_count_x

                if self.check_walkable(a) == 1:
                    self._pos_y += self._vel
                    self._refresh_actTile(a)

                else:
                    self._AIfunc(self)

            elif self._dir == 2:
                a = self._actTile - 1

                if self.check_walkable(a) == 1:
                    self._pos_x -= self._vel
                    self._refresh_actTile(a)

                else:
                    self._AIfunc(self)

            elif self._dir == 3:
                a = self._actTile - self._map._t_count_x

                if self.check_walkable(a) == 1:
                    self._pos_y -= self._vel
                    self._refresh_actTile(a)

                else:
                    self._AIfunc(self)

        else:
            self.revive(self._spawn_tile)

        if self._isVulnerable == False and self._isDead == False:
            self._actFrame = self._c_type + self._dir
        elif self._isVulnerable == True and self._isDead == False:
            self._actFrame = 16
        elif self._isDead == True:
            self._actFrame = 17 + self._dir

        if self._Enemy.get_isInvincible() == False:
            ghost_mult = 1

        if self._Enemy.get_startInvincible() == True:
            ghost_mult = 1

        a = self._ghostCanvas.create_image(self._frame[self._actFrame].get_x(), self._frame[self._actFrame].get_y(),image=self._palette,anchor=NW)
        self._ghostCanvas.delete(self._g_obj)
        self._g_obj = a

        self._ghostCanvas.place_configure(x=self._pos_x, y=self._pos_y)
        self.check_EnemyCollision()