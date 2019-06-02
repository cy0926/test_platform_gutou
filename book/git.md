### git基本命令
```shell
# 克隆代码
> git clone https://github.com/xxx/xxx

# 查看更新
> git status

# 更新内容
> git add .   # 添加全部有变更的内容
> git add test.py
> git add abc/

# add 撤销
> git reset HEAD
> git reset HEAD test.py

# 提交更新
>git commit -m "update xxx"

# 同步到远程master分支
> git push origin master

# 从远程master分支拉取代码到本地
> git pull origin master

```

### 分支操作
```shell
# 查看全部分支（远程和本地的）
> git brach -a

# 创建分支dev
> git branch dev

# 切换分支
> git checkout dev

# 合并分支（把dev分支合并到当前分支）
> git merge dev


```