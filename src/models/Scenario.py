from src.models.Step import Step


class Scenario(object):

    def __init__(self, scenarioParagraph):
        self.scenario = scenarioParagraph
        self.steps = []

        lines = self.scenario.split("\n")
        self.title = lines.pop(0)

        for line in lines:
            self.steps.append(Step(line))


if __name__ == '__main__':
    scen = Scenario("""
    Scenario: Wilson posts to his own blog
    Given I am logged in as Wilson
    When I try to post to "Expensive Therapy"
    Then I should see "Your article was published." """)
    [print(i) for i in scen.steps]
    print(scen.title)

