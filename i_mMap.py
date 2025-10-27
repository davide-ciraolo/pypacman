from tkinter import *
from i_mString import *

class Tile():

    def __init__(self, x = 0.0, y = 0.0, t_id = 0):
        self._x = x
        self._y = y

        self._t_id = t_id

    def get_x(self):
        return self._x

    def set_x(self, x = 0.0):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y = 0.0):
        self._y = y

    def get_t_id(self):
        return self._t_id

    def set_t_id(self, t_id = 0):
        self._t_id = t_id

class TileSet():

    def __init__(self, master = None, path = "", t_w = 1, t_h = 1, t_wb = 1, t_hb = 1):

        self._t_wsize = t_w
        self._t_hsize = t_h
        self._t_wborder = t_wb
        self._t_hborder = t_hb

        self._path = path
        self._palette = None

        self._tiles = {}

        self._master = master

        if path != "":
            self._load_tiles()

    def _load_tiles(self):

        try:
            self._palette = PhotoImage(master = self._master, file = correct_path(self._path))
        except:
            print("Errore caricamento tileSet.", self._path)
            exit()

        w = int(self._palette.width() / (self._t_wsize + self._t_wborder))
        h = int(self._palette.height() / (self._t_hsize + self._t_hborder))

        for i in range(0, h):
            for j in range(0, w):
                self._tiles[int((i * w) + j)] = Tile(x = (-(j*(self._t_wsize + self._t_wborder))), y =(-(i*(self._t_hsize + self._t_hborder))), t_id = (i * w) + j)

    def get_wsize(self):
        return int(self._t_wsize)

    def set_wsize(self, width = 0):
        self._t_wsize = width

    def get_hsize(self):
        return int(self._t_hsize)

    def set_hsize(self, height = 0):
        self._t_hsize = height

    def get_wborder(self):
        return self._t_wborder

    def set_wborder(self, border = 0):
        self._t_wborder = border

    def get_hborder(self):
        return self._t_hborder

    def set_hborder(self, border = 0):
        self._t_hborder = border

    def get_master(self):
        return self._master

    def set_master(self, master = None):
        self._master = master

    def get_path(self):
        return self._path

    def set_path(self, path = ""):
        self._path = path
        self._load_tiles()

    def get_palette(self):
        return self._palette

    def set_palette(self, palette = PhotoImage):
        self._palette = palette

    def get_tile(self, t_id = 0):
        if t_id >= 0 and t_id <= len(self._tiles):
            return self._tiles[t_id]

    def set_tile(self, t_id = 0, n_tile = None):
        if t_id >= 0 and t_id <= len(self._tiles):
                self._tiles[t_id] = n_tile

class Map():

    def __init__(self, master = None, path = ""):
        self._fruit_spawned = False
        self._fruit_s_type = 0
        self._fruit_delay = 0
        self._mapPath = path
        self._mapName = ""
        self._mapFrame = None
        self._mapPoints_backup = 0
        self._mapPoints = 0
        self._master = master
        self._tileSet = TileSet(master=self._master)
        self._t_count_x = 0
        self._t_count_y = 0

        self._TileCanvas = {}
        self._mapIsLoaded = False

        self._TileFrame_backup = {}
        self._TileFrame = {}

        self.load_map()

        self.draw_map()

    def set_fruit_spawned(self, bool):
        self._fruit_spawned = bool

    def get_fruit_spawned(self):
        return self._fruit_spawned

    def set_fruit_s_type(self, f_id):
        self._fruit_s_type = f_id

    def get_fruit_s_type(self):
        return self._fruit_s_type

    def set_fruit_delay(self, delay = 0):
        self._fruit_delay = delay

    def get_fruit_delay(self):
        return self._fruit_delay

    def set_mapPath(self, path = ""):
        self._mapPath = path

    def get_mapPath(self):
        return self._mapPath

    def set_mapName(self, name = ""):
        self._mapName = name

    def get_mapName(self):
        return self._mapName

    def set_mapFrame(self, frame = None):
        self._mapFrame = frame

    def get_mapFrame(self):
        return self._mapFrame

    def set_mapPoints(self, number = 0):
        self._mapPoints = number

    def get_mapPoints(self):
        return self._mapPoints

    def reset_mapPoints(self):
        self._mapPoints = self._mapPoints_backup

    def set_master(self, master = None):
        self._master = master

    def get_master(self):
        return self._master

    def set_tileSet(self, tileSet = None):
        self._tileSet = tileSet

    def get_tileSet(self):
        return self._tileSet

    def get_map_isLoaded(self):
        return self._mapIsLoaded

    def set_t_count_x(self, count = 0):
        self._t_count_x = count

    def get_t_count_x(self):
        return self._t_count_x

    def set_t_count_y(self, count = 0):
        self._t_count_y = count

    def get_t_count_y(self):
        return self._t_count_y

    def reset_map(self):
        for i in range(0, len(self._TileFrame)):
            self._TileFrame[i].set_t_id(self._TileFrame_backup[i].get_t_id())

        self.refresh_allTiles()

    def load_map(self):

        mapFile = load_textFile(self._mapPath)

        if mapFile == -1:
            self._mapIsLoaded = False
            return

        pos = 0

        pos = mapFile.find("@name = ", pos) + len("@name = ")
        self._mapName = mapFile[pos:mapFile.find(";", pos)]

        pos = mapFile.find("@count_x = ", pos) + len("@count_x = ")
        self._t_count_x = int(mapFile[pos:mapFile.find(";", pos)])

        pos = mapFile.find("@count_y = ", pos) + len("@count_x = ")
        self._t_count_y = int(mapFile[pos:mapFile.find(";", pos)])

        pos = mapFile.find("@tile_w = ", pos) + len("@tile_w = ")
        self._tileSet.set_wsize(int(mapFile[pos:mapFile.find(";", pos)]))

        pos = mapFile.find("@tile_h = ", pos) + len("@tile_h = ")
        self._tileSet.set_hsize(int(mapFile[pos:mapFile.find(";", pos)]))

        pos = mapFile.find("@tile_wb = ", pos) + len("@tile_wb = ")
        self._tileSet.set_wborder(int(mapFile[pos:mapFile.find(";", pos)]))

        pos = mapFile.find("@tile_hb = ", pos) + len("@tile_hb = ")
        self._tileSet.set_hborder(int(mapFile[pos:mapFile.find(";", pos)]))

        pos = mapFile.find("@tileset_path = ", pos) + len("@tileset_path = ")
        self._tileSet.set_path(mapFile[pos:mapFile.find(";", pos)])

        pos = mapFile.find("@tiles = {", pos) + len("@tiles = {")
        i = 0
        j = 0
        w = self._tileSet.get_wsize()
        h = self._tileSet.get_hsize()

        while mapFile.find(":", pos) != -1:
            pos = mapFile.find(":", pos) + 1
            self._TileFrame[(i * self._t_count_x) + j] = Tile(x = j * w, y = i * h, t_id = int(mapFile[pos:mapFile.find(",", pos)]))
            self._TileFrame_backup[(i * self._t_count_x) + j] = Tile(x = j * w, y = i * h, t_id = int(mapFile[pos:mapFile.find(",", pos)]))
            j += 1
            if j == self._t_count_x:
                i += 1
                j = 0
            if i > self._t_count_y:
                break

        self._mapFrame = Frame( master = self._master, width = (self._t_count_x * w), height = (self._t_count_y * h) + h, bg='black')
        self._mapFrame.place(anchor=CENTER, relx = 0.5, rely = 0.5)

        self._mapIsLoaded = True

    def draw_map(self):

        if self._mapIsLoaded == True:

            w = self._tileSet.get_wsize()
            h = self._tileSet.get_hsize()

            for i in range(0, self._t_count_y):
                for j in range(0, self._t_count_x):

                    a = self._TileFrame[(i * self._t_count_x) + j].get_t_id()

                    if a == 0 or a == 1:
                        self._mapPoints +=1

                    b = self._tileSet._tiles[a].get_x()
                    c = self._tileSet._tiles[a].get_y()

                    self._TileCanvas[(i * self._t_count_x) + j] = Canvas(master=self._mapFrame,width=w, height=h,bd=0, highlightthickness=0, relief='ridge')
                    self._TileCanvas[(i * self._t_count_x) + j].img_id = self._TileCanvas[(i * self._t_count_x) + j].create_image(b,c,image=self._tileSet.get_palette(),anchor=NW)
                    self._TileCanvas[(i * self._t_count_x) + j].place(x = j * w, y = i * h )

            self._mapPoints_backup = self._mapPoints

    def set_tile(self, id, pal_id):

        self._TileFrame[id].set_t_id(pal_id)
        self.refresh_tile(id)

    def refresh_tile(self, id):

        a = self._TileFrame[id].get_t_id()

        b = self._tileSet._tiles[a].get_x()
        c = self._tileSet._tiles[a].get_y()

        self._TileCanvas[id].delete(self._TileCanvas[id].img_id)
        self._TileCanvas[id].img_id = self._TileCanvas[id].create_image(b, c, image=self._tileSet.get_palette(), anchor=NW)

    def refresh_allTiles(self):
        for i in range(0, self._t_count_y):
            for j in range(0, self._t_count_x):
                self.refresh_tile((i * self._t_count_x) + j)


    def fruit_spawn(self, seed):

        if self._fruit_delay < 500:
            self._fruit_delay += 1
            return
        else:
            if seed % 2 == 0:
                self._fruit_s_type = 2
            else:
                self._fruit_s_type = 3

            for i in range(0, self._t_count_y):
                for j in range(0, self._t_count_x):
                    if self._TileFrame[(i * self._t_count_x) + j].get_t_id() == 5:
                        self.set_tile((i * self._t_count_x) + j, self._fruit_s_type)
                        self._fruit_spawned = True
                        self._fruit_delay = 0
                        break
                if self._fruit_spawned == True:
                    break