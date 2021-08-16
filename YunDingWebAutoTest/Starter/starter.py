"""
AUTHOR: Seamus
DATE: 2020/09/16
DESCRIPTION:
"""

# Options of --tb
import pytest

TB_SHORT = 'short'
TB_NO = 'no'
TB_LINE = 'line'


class Starter(object):
    verbose = False  # -v, show all the detail info
    stdout = False  # -s, show all stdout info
    durations = None  # --duration=<N>, show the most slowly cases
    traceback = None  # --tb=<arg>, arg must choose from 'short', 'no', 'line'. show trace back info
    auto_stop = False  # -x, stop test when the first failure occured
    reruns = 1  # --reruns=<N>, retry times when case failed
    reruns_delay = 3  # --reruns-delay=<N>, delay of returns
    marker = None  # -m, marker of cases to run
    test_paths = []  # case paths
    nodes = []  # nodes to be run
    additions = []

    def get_commands(self):
        cmds = []

        if self.verbose:
            cmds.append('-v')

        if self.stdout:
            cmds.append('-s')

        if self.durations is not None and self.durations > 0:
            opt = '--durations=%s' % self.durations
            cmds.append(opt)

        if self.traceback is not None:
            opt = '--tb=%s' % self.traceback
            cmds.append(opt)

        if self.auto_stop:
            cmds.append('-x')

        if self.reruns > 0:
            opt = '--reruns=%s' % self.reruns
            cmds.append(opt)
            if self.reruns_delay > 0:
                c = '--reruns-delay=%s' % self.reruns_delay
                cmds.append(c)

        if self.marker is not None:
            cmds.append('-m')
            cmds.append(self.marker)

        if len(self.test_paths) > 0:
            for path in self.test_paths:
                cmds.append(path)

        if len(self.nodes) > 0:
            for node in self.nodes:
                cmds.append(node)

        if len(self.additions) > 0:
            for add in self.additions:
                cmds.append(add)

        return cmds

    def start(self):
        commands = self.get_commands()
        print('commands: %s' % commands)
        exit_code = pytest.main(commands)
        return exit_code



