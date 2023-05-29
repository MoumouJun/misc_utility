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
        # {"仓库名称":["地址","本地路径"]}
        self._repo = self._init_repo(path)
        pass

    def _init_repo(self, path) -> dict:
        repo = {}
        with open(path) as f:
            repo_ori = json5.load(f)
            for k, v in repo_ori['repo'].items():
                for i in v:
                    repo[i['name']] = [i['ssh'], i['local_path'], i['branch']]
        print(repo)
        return repo

    def _clone(self):
        '''克隆各个仓库到指定目录'''
        for k, v in self._repo.items():
            if v[1] == '':
                continue
            if os.path.exists("./%s/%s" % (v[1], k)):
                print("%s仓库已经下载" % k)
                #TODO
                self._fetch_rebase()
            else:
                sh('cd %s;git  clone %s' % (v[1], v[0]))

    def _fetch_rebase(self):
        '''更新仓库'''
        pass

    def run(self):
        self._clone()


stu = Study3Lib()
stu.run()
