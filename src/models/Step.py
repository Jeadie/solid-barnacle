import re


class Step(object):

    ACCEPTABLE_PREFIXES = ["Given", "When", "Then", "And", "But"]

    def __init__(self, stepLine, data=None):
        if False not in [stepLine.startswith(prefix) for prefix in Step.ACCEPTABLE_PREFIXES]:
            raise TypeError("input parameter stepLine is not a correctly formatted Step."
                            " Must start with {0}".format(Step.ACCEPTABLE_PREFIXES))

        self.stepLine = stepLine
        # Get first word (num=2 to only split once, save time)
        self.prefix = self.stepLine.split(" ", 1)[0]
        if data is not None and stepLine[-1] != ":":
            raise TypeError("Step should not have any data. Step doesn't end in ':'.")

        self.data = data
        variables = re.findall(r'(".*?")|([0-9])', self.stepLine)
        variables = [item for sublist in variables for item in sublist]
        variables = list(filter(None, variables))
        for i in range(len(variables)):
            self.stepLine = self.stepLine.replace('{0}'.format(variables[i]), "{%d}" % i)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash(self.stepLine)

    def __str__(self):
        return self.stepLine