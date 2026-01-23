from subprocess import run

print('切换到 main 分支')
run('git checkout main')

print('拉取远程仓库')
run('git pull')

print('安装 npm 包')
run('pnpm install')

print('开始构建')
run('pnpm build')

print('添加构建产物到 stash')
run('git add /docs/.vitepress/dist/ -f')
# run('git stash push -m "Update"')

print('切换到 deploy 分支')
run('git checkout deploy')

print('拉取远程仓库')
run('git pull')

print('清空 deploy 分支')
run('git rm -rf .')
run('git clean -fdx')
# run('git stash pop stash@{0}')
# run('git add .')

print('提交 stash')
run('git commit -m "Update"')

print('push 到远程仓库')
run('git push')

print('切换到 main 分支')
run('git checkout main')