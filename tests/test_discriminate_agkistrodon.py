#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_discriminate_agkistrodon
----------------------------------
Tests for `discriminate_agkistrodon` module.
"""

import pytest
import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner

from discriminate_agkistrodon import cli

@pytest.fixture
def response():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument.
    """
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string



def test_command_line_interface():
    runner = CliRunner()
    result = runner.invoke(cli.main)
    return
    assert result.exit_code == 0
    assert 'discriminate_agkistrodon.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output

class TestDiscriminate_agkistrodon(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        return
        assert result.exit_code == 0
        assert 'discriminate_agkistrodon.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
