from Orange.base import SklModel
from Orange.ensembles import (
    SklAdaBoostClassificationLearner, SklAdaBoostRegressionLearner
)
from Orange.modelling import Fitter

__all__ = ['SklAdaBoostLearner']


class SklAdaBoostLearner(Fitter):
    __fits__ = {'classification': SklAdaBoostClassificationLearner,
                'regression': SklAdaBoostRegressionLearner}

    __returns__ = SklModel
