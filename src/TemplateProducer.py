from os import os, path

class TemplateProducer(object):
    """

    Produces and saves step files for an arbitrary format and built from a
    format with an arbitrary builder. Most common case is a gherkin Builder being formatted
    into python behave code stubs but can be from any format (e.g. json, xml) and formatting in
    any potential output (e.g. behave, cucumber, jbehave).

    """

    def __init__(self, builder, formatter):
        self.builder = builder
        self.formatter = formatter

    def produce_code_templates(self, featureFolder, stepFolder = None):
        if stepFolder is None:
            parentFolder = path.abspath(path.join(featureFolder, os.pardir))
            stepFolder = os.path.join(parentFolder, "steps")
            os.mkdir(stepFolder)

        for featureFile in os.listdir(featureFolder):
            with open(featureFile, "r") as feature:
                featureModel = self.builder.buildFeature(feature.read())
                with open(self.get_step_path(featureFile, stepFolder)) as step:
                    step.write(self.formatter.format_feature(featureModel))


    def get_step_path(self, featureFile, stepFolder):
        return os.path.join(stepFolder,
                            os.path.splitext(featureFile)[0],
                            self.formatter.get_format_extension())