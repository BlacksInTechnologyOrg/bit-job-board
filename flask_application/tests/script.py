import nose
import sys

from flask_script import Command


class RunTests(Command):
    """Runs the unittests"""
    def run(self, *args, **kwargs):
        nose.run(argv=[sys.argv[0]])
