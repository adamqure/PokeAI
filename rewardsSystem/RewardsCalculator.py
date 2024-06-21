class RewardsCalculator:
    def __init__(self, maxActions):
        self.maxActions = maxActions
        self.actionCount = 0

    def calculateRewards(self, pyboy, action):
        print(f'Taking action {action} as action number {self.actionCount}')
        self.actionCount += 1

        # return 0, self.actionCount == self.maxActions
        return 0, False