import sys
sys.path.append("C:\\cygwin\\home\\Programming\\Pokemon-Python\\src")

from InputProcessor import commands

from InputProcessor.input_processor import InputProcessor
from MainMenu.main_menu import MainMenu
from Screen.GUI.screen import Screen
from Screen.GUI.MainMenu.main_menu_view import MainMenuScreen


class MainMenuController:
    """ Controller for the main menu """
    
    def __init__(self, screen, inputProcessor):
        """ Builds the Main Menu Controller """
        self.menu = MainMenu()
        self.screen = screen
        self.menuScreen = MainMenuScreen(self.menu)
        self.screen.setScreen(self.menuScreen)
        self.cmds = {commands.UP:self.menuScreen.up,
                           commands.DOWN:self.menuScreen.down,
                           commands.EXIT:self.quit}
        self.inputProcessor = inputProcessor
        
    def run(self):
        """ Runs the game loop """
        while self.menu.running:
            self.screen.update()
            self.inputProcessor.processInputs(self.cmds)
            self.screen.draw()
            
    def quit(self):
        """ Quits the game """
        self.menu.running = False
                
if __name__ == "__main__":
    screen = Screen()
    inputProcessor = InputProcessor()
    main_controller = MainMenuController(screen, inputProcessor)
    main_controller.run()