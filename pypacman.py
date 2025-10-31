from pathlib import Path
from tkinter import *
from i_mTimer import Timer
from i_mMap import *
from i_mPacMan import *
from i_mGhost import *
from i_mAI import *

root = Tk()
root.title("Pacman")
root.geometry("800x600+-7+0")

VULNERABLE_TIME = 250

TILE_SIZE_W = 26
TILE_SIZE_H = 26
TILE_SIZE_WB = 1
TILE_SIZE_HB = 1

class Application():

    def __init__(self, appRoot = None):
        self.MainFrame = Frame(master = appRoot, bg = "black")
        self.MainFrame.place(relwidth = 1, relheight = 1)
        self._Win = False
        self._vulnerable_time = 0
        self.control_init()

    def set_Win(self, bool):
        self._Win = bool

    def get_Win(self):
        return self._Win

    def set_vulnerable_time(self, x = 0):
        self._vulnerable_time = x

    def get_vulnerable_time(self):
        return self._vulnerable_time

    def KeyBoard_Event(self, key):

        if self.pacman.get_dir() != 5 and self.pacman.get_isAlive() == True:

            if key.char == 'd':
                self.pacman.changedir(0)
            elif key.char == 's':
                self.pacman.changedir(1)
            elif key.char == 'a':
                self.pacman.changedir(2)
            elif key.char == 'w':
                self.pacman.changedir(3)
            else:
                if self.pacman.get_isAlive() == True:
                    return

        if self.pacman.get_dir() == 5 and self.pacman.get_isAlive() == True:
            return

        elif self.pacman.get_isAlive() == False and self.pacman.get_Lives() >= 0 and self.get_Win() == False:
            self.pressLabel.destroy()

            self.p_ghost.set_isVulnerable(False)
            self.o_ghost.set_isVulnerable(False)
            self.b_ghost.set_isVulnerable(False)
            self.r_ghost.set_isVulnerable(False)
            self.pacman.set_isInvincible(False)
            self.set_vulnerable_time(0)

            self.pacman.spawn()
            self.p_ghost.spawn()
            self.o_ghost.spawn()
            self.b_ghost.spawn()
            self.r_ghost.spawn()

        elif self.pacman.get_isAlive() == False and self.pacman.get_Lives() == -2:
            self.pacman.reset_score()
            self.pacman.reset_lives()
            self.RefreshScore()
            self.Reset()

        elif self.pacman.get_isAlive() == False and self.get_Win() == True:
            self.Reset()
            self.set_Win(False)

    def GameWin(self):
        self.p_ghost.set_isAlive(False)
        self.o_ghost.set_isAlive(False)
        self.b_ghost.set_isAlive(False)
        self.r_ghost.set_isAlive(False)

        self.pacman.set_isAlive(False)

        self.set_Win(True)

        if self.pacman.get_dir() == 0:
            self.pacman.set_actFrame(0)
        elif self.pacman.get_dir() == 1:
            self.pacman.set_actFrame(3)
        elif self.pacman.get_dir() == 2:
            self.pacman.set_actFrame(7)
        elif self.pacman.get_dir() == 3:
            self.pacman.set_actFrame(5)

        self.pacman.RefreshFrame()

        self.pressLabel = Label(master = self._gameMap.get_mapFrame(), bg = "black", fg = "white", font = "Helvetica", text = "YOU WIN!")
        self.pressLabel.place(anchor = CENTER, relx = 0.5, rely = 0.522, width = 120, height = 26)

        self.set_vulnerable_time(VULNERABLE_TIME)

    def GameOver(self):
        self.pressLabel = Label(self._gameMap.get_mapFrame(), bg = "black", fg = "white", font = "Helvetica", text = "GAME OVER!")
        self.pressLabel.place(anchor = CENTER, relx = 0.5, rely = 0.522, width = 120, height = 26)

    def RefreshScore(self):
        self.ScoreBoard['text'] = "SCORE: " + str(self.pacman.get_score())

    def Reset(self):
        self.pressLabel.destroy()

        self.pressLabel = Label(self._gameMap.get_mapFrame(), bg = "black", fg = "white", font = "Helvetica", text = "READY!")
        self.pressLabel.place(anchor = CENTER, relx = 0.5, rely = 0.522, width = 180, height = 26)

        self._gameMap.reset_map()
        self._gameMap.reset_mapPoints()

        self.pacman.reset_spawn()
        self.p_ghost.reset_spawn()
        self.o_ghost.reset_spawn()
        self.b_ghost.reset_spawn()
        self.r_ghost.reset_spawn()

        self.p_ghost.set_isVulnerable(False)
        self.o_ghost.set_isVulnerable(False)
        self.b_ghost.set_isVulnerable(False)
        self.r_ghost.set_isVulnerable(False)
        self.pacman.set_isInvincible(False)
        self.set_vulnerable_time(0)

    def control_init(self):
        self.GameFrame = Frame(master = self.MainFrame, bg = "grey")
        self.GameFrame.place(relx = 0.15, rely = 0, relwidth = 0.7, relheight = 1)

        #self._tileSet = TileSet(path = "textures/pacman1.png", t_w = TILE_SIZE_W, t_h = TILE_SIZE_H, t_wb = TILE_SIZE_WB, t_hb = TILE_SIZE_HB)

        self._gameMap = Map(master = self.GameFrame, path = Path("maps\standard_map.txt"))

        self.ScoreBoard = Label(self._gameMap.get_mapFrame(), bg = "black", fg = "white", font = "Helvetica")
        self.ScoreBoard.place(anchor = CENTER, relx = 0.8, rely = 0.96, height = 26)
        self.ScoreBoard['text'] = "SCORE: 0"

        self.p_ghost = Ghost(self._gameMap, self._gameMap.get_tileSet(), GHOST_COLOR_PINK, AI_p_ghost)
        self.o_ghost = Ghost(self._gameMap, self._gameMap.get_tileSet(), GHOST_COLOR_ORANGE, AI_o_ghost)
        self.b_ghost = Ghost(self._gameMap, self._gameMap.get_tileSet(), GHOST_COLOR_BLUE, AI_b_ghost)
        self.r_ghost = Ghost(self._gameMap, self._gameMap.get_tileSet(), GHOST_COLOR_RED, AI_r_ghost)

        self.pacman = Pacman(self._gameMap, self._gameMap.get_tileSet())

        self.p_ghost.set_Enemy(self.pacman)
        self.o_ghost.set_Enemy(self.pacman)
        self.b_ghost.set_Enemy(self.pacman)
        self.r_ghost.set_Enemy(self.pacman)

        self.pressLabel = Label(self._gameMap.get_mapFrame(), bg = "black", fg = "white", font = "Helvetica", text = "READY!")

        self.pressLabel.place(anchor = CENTER, relx = 0.5, rely = 0.522, width = 180, height = 26)

        self.GameFrame.bind("<KeyPress>", self.KeyBoard_Event)

        self.GameFrame.focus_set()

        self.pacTimer = Timer(interval = 0.05, func = self.Timer1_func, f_args = ())
        self.pacTimer.start()

    def Timer1_func(self):
        if self._gameMap.get_fruit_spawned() == False and self.pacman.get_isAlive() == True:
            self._gameMap.fruit_spawn(self.pacTimer.get_sec())

        self.pacman._render()
        self.RefreshScore()

        if self._gameMap.get_mapPoints() <= 0 and self.get_Win() == False:
            self.GameWin()

        if self.pacman.get_dir() == 5:
            self.p_ghost.set_isAlive(False)
            self.o_ghost.set_isAlive(False)
            self.b_ghost.set_isAlive(False)
            self.r_ghost.set_isAlive(False)
            if self.pacman.get_Lives() == -1:
                self.GameOver()
                self.pacman.set_Lives(self.pacman.get_Lives() - 1)

        if self.pacman.get_startInvincible() == True:
            self.set_vulnerable_time(0)
            self.pacman.set_isInvincible(True)
            self.p_ghost.set_isVulnerable(True)
            self.o_ghost.set_isVulnerable(True)
            self.b_ghost.set_isVulnerable(True)
            self.r_ghost.set_isVulnerable(True)

            self.pacman.set_startInvincible(False)

        if self.pacman.get_isInvincible() == True:
            self.set_vulnerable_time(self.get_vulnerable_time() + 1)

            if self.get_vulnerable_time() == VULNERABLE_TIME:
                self.p_ghost.set_isVulnerable(False)
                self.o_ghost.set_isVulnerable(False)
                self.b_ghost.set_isVulnerable(False)
                self.r_ghost.set_isVulnerable(False)
                self.pacman.set_isInvincible(False)
                self.set_vulnerable_time(0)

app = Application(root)

root.mainloop()
