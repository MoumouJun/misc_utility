#!/usr/bin/python3

import sys
import os
import subprocess


def sh(cmd: str) -> list:
    err, out = subprocess.getstatusoutput(cmd)
    print(out)
    return [err, out]


usage = {
    'ps': '',
    'du': '',
}


class BaseObject():
    def __init__(self) -> None:
        pass


class CBash(BaseObject):
    def __init__(self) -> None:
        pass

    def ps(self):
        sh("ps ux | grep -Ev 'vscode|sleep|bash|ps'")

    def du(self, path: str = "./"):
        if len(sys.argv) > 2 and os.path.exists(sys.argv[2]):
            path = sys.argv[2]
        sh("du --max-depth=1 -h ./ %s;free -h" % (path))


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] in usage.keys():
        f = getattr(CBash(), sys.argv[1])
        f()
    else:
        print("支持的命令："+str(usage.keys()))
