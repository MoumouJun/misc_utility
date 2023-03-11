#!/usr/bin/python3

import sys
import os
import subprocess
import json5


def sh(cmd: str) -> list:
    print(cmd)
    err, out = subprocess.getstatusoutput(cmd)
    print(out)
    return [err, out]


class Study3Lib():
    def __init__(self, path: str = './study_thirdLib.json') -> None:
        '''第三方库学习'''
        self._repo = self._init_repo(path)
        pass

    def _init_repo(self, path) -> dict:
        repo = {}
        with open(path) as f:
            repo_ori = json5.load(f)
            for k, v in repo_ori['repo'].items():
                for i in v:
                    repo[i['name']] = [i['ssh'], i['local_path']]
        print(repo)
        return repo

    def _clone(self):
        '''克隆各个仓库到指定目录'''
        for repo in self._repo.values():
            if repo[1] == '':
                continue
            sh('cd %s;git  clone %s' % (repo[1], repo[0]))

    def _fetch_rebase(self):
        pass

    def run(self):
        self._clone()


stu = Study3Lib()
stu.run()
