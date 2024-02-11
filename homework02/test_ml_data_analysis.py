from ml_data_analysis import summary_stats
from ml_data_analysis import remove_nulls
from ml_data_analysis import calculate_distance

import pytest

def test_summary_stats():
    list_of_dicts = [{'a':1},{'a':2}]
    assert summary_stats(list_of_dicts, 'a') == {"Mean":1.5,"Median":1.5}

def test_summary_stats_exceptions():
    list_of_dicts = [{'a':1},{'a':2}]
    with pytest.raises(IndexError):
        summary_stats([],'a')
    with pytest.raises(KeyError):
        summary_stats([{'a': 1}, {'b': 1}], 'a')             # dictionaries not uniform
    with pytest.raises(ValueError):
        summary_stats([{'a': 1}, {'a': 'x'}], 'a')           # value not a float
    with pytest.raises(KeyError):
        summary_stats([{'a': 1}, {'a': 2}], 'b')

def test_remove_nulls():
    assert remove_nulls([{'a':""},{'a':3},{'a':None}],'a') == [{'a':3}]


def test_calculate_distance():
    lod = [{'lat':1,'long':1},{'lat':5,'long':2},{'lat':10,'long':20},{'lat':30.0,'long':-30.0}]
    assert calculate_distance(lod,'lat','long',0,1) == 458.42598304975684
    assert calculate_distance(lod,'lat','long',2,3) == 5623.93255411118


