import os

class SolidBarnacleAPI(object):

    @staticmethod
    def translate_features(feature_path, step_path=None):
        """
        Translates all the feature files into step files. Duplicate method will be
        constructed for lines in features that are in different files.
        (i.e. feature files are considered independently.)
        :param feature_path: String path the the feature folder
        :param step_path: String path to the desired folder for step files. If None,
            will be placed in a new folder "../step" relative to the feature_path
        """
        pass
        # for file in os.listdir(feature_path):
