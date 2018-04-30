from .BehaviourDSLBuilder import  BehaviourDSLBuilder


class GherkinBuilder(BehaviourDSLBuilder):
    """
    A set of builders that take in various parts of a gherkin file and return models
    of varying details to be queried for source code generation. The resulting data
    structures can be found in the models module.
    """

    @staticmethod
    def build_feature(gherkinFeature):
        pass

    @staticmethod
    def build_scenario(gherkinScenario):
        pass

    @staticmethod
    def build_step(gherkinStep):
        pass

    @staticmethod
    def build_step_text(gherkinText):
        pass

    @staticmethod
    def build_step_table(gherkinTable):
        pass