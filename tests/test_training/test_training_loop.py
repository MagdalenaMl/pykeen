# -*- coding: utf-8 -*-

"""Test for sLCWA and LCWA."""

from pykeen.losses import CrossEntropyLoss, MarginRankingLoss, NSSALoss
from pykeen.sampling.filtering import BloomFilterer, PythonSetFilterer
from pykeen.training import LCWATrainingLoop, SLCWATrainingLoop
from tests.test_training import cases


class MRUnfilteredSLCWATrainingLoopTestCase(cases.SLCWATrainingLoopTestCase):
    """Test sLCWA with unfiltered negative sampling with margin ranking loss."""

    cls = SLCWATrainingLoop
    filterer = None
    loss = MarginRankingLoss


class NSSAUnfilteredSLCWATrainingLoopTestCase(cases.SLCWATrainingLoopTestCase):
    """Test sLCWA with unfiltered negative sampling with NSSA loss."""

    cls = SLCWATrainingLoop
    filterer = None
    loss = NSSALoss


class CEUnfilteredSLCWATrainingLoopTestCase(cases.SLCWATrainingLoopTestCase):
    """Test sLCWA with unfiltered negative sampling with cross entropy loss."""

    cls = SLCWATrainingLoop
    filterer = None
    loss = CrossEntropyLoss


class MRSetFilteredSLCWATrainingLoopTestCase(cases.SLCWATrainingLoopTestCase):
    """Test sLCWA with set filtered negative sampling with margin ranking loss."""

    cls = SLCWATrainingLoop
    filterer = PythonSetFilterer
    loss = MarginRankingLoss


class NSSASetFilteredSLCWATrainingLoopTestCase(cases.SLCWATrainingLoopTestCase):
    """Test sLCWA with set filtered negative sampling with NSSA loss."""

    cls = SLCWATrainingLoop
    filterer = PythonSetFilterer
    loss = NSSALoss


class CESetFilteredSLCWATrainingLoopTestCase(cases.SLCWATrainingLoopTestCase):
    """Test sLCWA with set filtered negative sampling with cross entropy loss."""

    cls = SLCWATrainingLoop
    filterer = PythonSetFilterer
    loss = CrossEntropyLoss


# Multiple permutations of loss not necessary for bloom filter since it's more of a
# filter vs. no filter thing.
class BloomFilteredSLCWATrainingLoopTestCase(cases.SLCWATrainingLoopTestCase):
    """Test sLCWA with bloom filtered negative sampling."""

    cls = SLCWATrainingLoop
    filterer = BloomFilterer


class MRLossLCWATrainingLoopTestCase(cases.TrainingLoopTestCase):
    """Test LCWA with margin ranking loss."""

    cls = LCWATrainingLoop
    loss = MarginRankingLoss


class NSSALossLCWATrainingLoopTestCase(cases.TrainingLoopTestCase):
    """Test LCWA with NSSA loss."""

    cls = LCWATrainingLoop
    loss = NSSALoss


class CELCWATrainingLoopTestCase(cases.TrainingLoopTestCase):
    """Test LCWA with cross entropy loss."""

    cls = LCWATrainingLoop
    loss = CrossEntropyLoss
