class TunedClassifier():
    def __init__(self, classifier=None, score=None):
        if classifier is None:
            self.classifier = None
        else:
            self.classifier = classifier

        if score is None:
            self.score = 0.0
        else:
            self.score = score

    def __str__(self):
        return "score: %.4f \n %s" % (self.score, str(self.classifier))