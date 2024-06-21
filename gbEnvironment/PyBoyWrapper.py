from pyboy import PyBoy
from gbEnvironment.GymEnvironment import GymEnvironment
from rewardsSystem.RewardsCalculator import RewardsCalculator

class PyBoyWrapper:
    
    def __init__(self, rom, maxActions):
        self.isRunningGame = False
        self.pyboy = PyBoy(rom)
        self.pyboy.set_emulation_speed(0)
        self.gym = GymEnvironment(self.pyboy, RewardsCalculator(maxActions))

        self.runGame(self.gym)

    def runGame(self, env):
        isRunningGame = True
        while(isRunningGame):
            action = env.action_space.sample()
            observation, reward, terminated, truncated, info = env.step(action)

            if terminated:
                env.close()
                isRunningGame = False