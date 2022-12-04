from tkinter import *
from tkinter import ttk
import random
import numpy as np
root = Tk()

class Player:
    health = 100.0
    bleedturns = 0
    isbleeding = False


class Enemy:
    health = 100.0
    bleedturns = 0
    isbleeding = False


class Main:

    def __init__(self, root):
        # Create GUI
        root.title("Text Fight")

        # Framework
        mainframe = ttk.Frame(root, relief='raised')
        mainframe.grid(column=0, row=0, sticky='N, W, E, S')

        consoleframe = ttk.Frame(mainframe, relief='sunken')
        consoleframe.grid(column=0, columnspan=2, row=0, padx=5, pady=5, sticky='N, W, E, S')

        buttonframe = ttk.Frame(mainframe, relief='sunken')
        buttonframe.grid(column=2, columnspan=2, row=0, padx=5, pady=5, sticky='N, W, E, S')

        healthframe = ttk.Frame(mainframe, relief='sunken')
        healthframe.grid(column=0, row=1, padx=5, pady=5, sticky='N, W, E, S')

        healthframe2 = ttk.Frame(mainframe, relief='sunken')
        healthframe2.grid(column=1, row=1, padx=5, pady=5, sticky='N, W, E, S')

        healthframe3 = ttk.Frame(mainframe, relief='sunken')
        healthframe3.grid(column=2, row=1, padx=5, pady=5, sticky='N, W, E, S')

        healthframe4 = ttk.Frame(mainframe, relief='sunken')
        healthframe4.grid(column=3, row=1, padx=5, pady=5, sticky='N, W, E, S')

        # Console, labels, & other widgets
        self.console = Text(consoleframe, state='disabled', bg='black', fg='white', wrap='word')
        self.console.grid(column=0, row=0)

        self.playerhealthstr = StringVar()
        self.playerhealthstr.set(str(Player.health))

        self.playerhealthlbl = ttk.Label(healthframe, textvariable=self.playerhealthstr)
        self.playerhealthlbl.grid(column=1, row=0, padx=5, pady=5)

        playerhealthlbl2 = ttk.Label(healthframe, text="Your Health: ")
        playerhealthlbl2.grid(column=0, row=0, padx=5, pady=5)

        self.playerbleedstr = StringVar()

        self.playerbleedinglbl = ttk.Label(healthframe2, textvariable=self.playerbleedstr)
        self.playerbleedinglbl.grid(column=0, row=0, padx=5, pady=5)

        self.enemyhealthstr = StringVar()
        self.enemyhealthstr.set(str(Enemy.health))

        self.enemyhealthlbl = ttk.Label(healthframe3, textvariable=self.enemyhealthstr)
        self.enemyhealthlbl.grid(column=1, row=0, padx=5, pady=5)

        enemyhealthlbl2 = ttk.Label(healthframe3, text="Enemy Health: ")
        enemyhealthlbl2.grid(column=0, row=0, padx=5, pady=5)

        self.enemybleedstr = StringVar()

        self.enemybleedlbl = ttk.Label(healthframe4, textvariable=self.enemybleedstr)
        self.enemybleedlbl.grid(column=0, row=0, padx=5, pady=5)

        # Buttons
        startbtn = ttk.Button(buttonframe, text="Start!", command=self.startup)
        startbtn.grid(column=0, row=0, padx=10, pady=10)

        self.punchbtn = ttk.Button(buttonframe, text="Punch", command=self.player_punch, state='disabled')
        self.punchbtn.grid(column=1, row=0, padx=10, pady=10)

        self.kickbtn = ttk.Button(buttonframe, text="Kick", state='disabled')
        self.kickbtn.grid(column=0, row=1, padx=10, pady=10)

        self.dodgebtn = ttk.Button(buttonframe, text="Dodge", state='disabled')
        self.dodgebtn.grid(column=1, row=1, padx=10, pady=10)

        self.blockbtn = ttk.Button(buttonframe, text="Block", state='disabled')
        self.blockbtn.grid(column=0, row=2, padx=10, pady=10)

    def writeToConsole(self, msg):
        numlines = int(self.console.index('end - 1 line').split('.')[0])
        self.console['state'] = 'normal'
        if numlines == 24:
            self.console.delete(1.0, 2.0)
        if self.console.index('end-1c') != '1.0':
            self.console.insert('end', '\n')
        self.console.insert('end', msg)
        self.console['state'] = 'disabled'

    def startup(self):
        self.writeToConsole(msg="Welcome to Text Fight!")
        self.writeToConsole(msg="")
        self.writeToConsole(msg="Initialising...")
        self.writeToConsole(msg="")

        Player.health = 100.0
        Enemy.health = 100.0

        Player.bleedturns = 0
        Enemy.bleedturns = 0

        Player.isbleeding = False
        Enemy.isbleeding = False

        #Player.l_arm = {key: False for key in Player.l_arm}
        #Player.r_arm = {key: False for key in Player.r_arm}
        #Player.l_leg = {key: False for key in Player.l_leg}
        #Player.r_leg = {key: False for key in Player.r_leg}
        #Player.torso = {key: False for key in Player.torso}
        #Player.head = {key: False for key in Player.head}

        self.playerhealthstr.set(str(Player.health))
        self.enemyhealthstr.set(str(Enemy.health))

        self.writeToConsole(msg="Health restored. Injuries healed. Prepare to fight!")

        self.punchbtn['state'] = 'enabled'
        self.kickbtn['state'] = 'enabled'

    def player_punch(self):
        chance = random.randint(1, 3)

        if chance == 1:
            self.writeToConsole(msg="You punch the enemy and it hits square!")
            self.hurtenemy(10)
            if Enemy.health >= 1:
                self.enemy_punch()
        elif chance == 2:
            self.writeToConsole(msg="You punch the enemy, but it doesn't land right!")
            self.hurtenemy(5)
            if Enemy.health >= 1:
                self.enemy_punch()
        elif chance == 3:
            self.writeToConsole(msg="You miss!")
            if Enemy.health >= 1:
                self.enemy_punch()

    def enemy_punch(self):
        chance = random.randint(1, 3)

        if chance == 1:
            self.writeToConsole(msg="The enemy punches you back!")
            self.hurtplayer(7)
        elif chance == 2:
            self.writeToConsole(msg="The enemy punches you back, but you manage to deflect most of it!")
            self.hurtplayer(4)
        elif chance == 3:
            self.writeToConsole(msg="The enemy misses!")

    def hurtenemy(self, dmg):
        Enemy.health -= dmg
        bleedchance = random.randint(1, 5)

        self.deathcheck()

        if not Enemy.isbleeding and bleedchance == 3:
            Enemy.bleedturns = 4
            Enemy.isbleeding = True
            self.writeToConsole(msg="The enemy is bleeding!")

        self.bleedcheck()

        self.enemyhealthstr.set(str(Enemy.health))

    def bleedenemy(self, dmg):
        Enemy.health -= dmg
        self.deathcheck()
        self.writeToConsole(msg="Blood drips from the enemy's wound!")
        self.enemyhealthstr.set(str(Enemy.health))

    def hurtplayer(self, dmg):
        Player.health -= dmg
        bleedchance = random.randint(1, 5)

        self.deathcheck()

        if not Player.isbleeding and bleedchance == 3:
            Player.bleedturns = 4
            Player.isbleeding = True
            self.writeToConsole(msg="The enemy is bleeding!")

        self.bleedcheck()

        self.playerhealthstr.set(str(Player.health))

    def bleedplayer(self, dmg):
        Player.health -= dmg
        self.deathcheck()
        self.writeToConsole(msg="Blood drips from your wound!")
        self.playerhealthstr.set(str(Player.health))

    def bleedcheck(self):
        if Player.isbleeding and Player.bleedturns >= 1:
            self.bleedplayer(3)
            Player.bleedturns -= 1
        elif Player.bleedturns < 1:
            Player.isbleeding = False

        if Enemy.isbleeding and Enemy.bleedturns >= 1:
            self.bleedenemy(3)
            Enemy.bleedturns -= 1
        elif Enemy.bleedturns < 1:
            Enemy.isbleeding = False

    def deathcheck(self):

        if Player.health <= 0.1:
            self.writeToConsole(msg="")
            self.writeToConsole(msg="You have been defeated!")
            self.writeToConsole(msg="Press 'Start' to reset the fight...")
            self.writeToConsole(msg="")
            self.punchbtn['state'] = 'disabled'

        if Enemy.health <= 0.1:
            self.writeToConsole(msg="")
            self.writeToConsole(msg="You have defeated the enemy! Congratulations!")
            self.writeToConsole(msg="Press 'Start' to reset the fight...")
            self.writeToConsole(msg="")
            self.punchbtn['state'] = 'disabled'
            




Main(root)
root.mainloop()