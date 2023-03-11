
# 从0配置Linux开发环境，以为debian为例


```bash
# 更新权限，sudo不用输入密码
sudo echo "liujun ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
```

##  更新为国内源

```bash
sudo cp /etc/apt/sources.list /etc/apt/sources.list_bak
#中国科技大学
sudo sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
#网易云163
sudo sed -i 's/deb.debian.org/mirrors.163.com/g' /etc/apt/sources.list
#阿里云
sudo sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list
#清华同方
sudo sed -i 's/deb.debian.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list
sudo apt-get update # 更新索引
```

## 安装基本开发工具
```bash
sudo apt-get install vim # git gcc g++
```



```bash
#  ~/.bashrc
# 别称
# 上下键历史命令
if [[ $- == *i* ]]
then
    bind '"\e[A": history-search-backward'
    bind '"\e[B": history-search-forward'
fi

```

```bash
# git配置文件 ~/.gitconfig
[user]
        name = LiuJun
        email = liujun001217@gmail.com
[i18n]
    logoutputencoding = utf-8
    commitencoding = utf-8
[gui]
    encoding = utf-8
[diff]
    tool = vimdiff
[difftool]
    prompt = false
[alias]
    co = checkout
    ci = commit
    br = branch
    st = status
    s = status -s
    l3 = log -3
    l10 = log -10

        l = log --oneline -10 --color --graph --pretty=format:'%Cgreen(%ci) %Cred%h -%C(yellow)%d %s %C(bold blue) <%an>' --abbrev-commit
        d = difftool
    lg = log --color --graph --pretty=format:'%Cred%h -%C(yellow)%d %s %Cgreen(%ci) %C(bold blue) <%an>' --abbrev-commit

[color]
    ui = true
[core]
    filemode = false
[filter "lfs"]
        smudge = git-lfs smudge -- %f
        process = git-lfs filter-process
        required = true
        clean = git-lfs clean -- %f


```






