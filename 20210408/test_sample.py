# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/9 18:13
# @Author  : Jeffrey
# @File    : test_sample.py

import pytest


def func(x):
    return x + 1


@pytest.mark.login
def test_answer():
    assert func(3) == 5
    assert func(4) == 5
