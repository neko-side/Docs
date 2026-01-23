from subprocess import run

print('切换到 main 分支')
run('git checkout main', check=True)

print('拉取远程仓库')
run('git pull', check=True)

print('安装 npm 包')
run('pnpm install', check=True)

print('开始构建')
run('pnpm build', check=True)

print('添加构建产物到 stash')
run('git add docs/.vitepress/dist/ -f', check=True)
# run('git stash push -m "Update"')

print('切换到 deploy 分支')
run('git checkout deploy', check=True)

print('拉取远程仓库')
run('git pull', check=True)

print('清空 deploy 分支')
# run('git rm -rf ')
run('git clean -fdx', check=True)
# run('git stash pop stash@{0}')
# run('git add .')

print('拷贝构建产物到根目录')
run('cp docs\\.vitepress\\dist\\* .\\', check=True)
run('rm docs -r',check=True)

print('提交 stash')
run('git commit -m "Update"', check=True)

print('push 到远程仓库')
run('git push deploy', check=True)

print('切换到 main 分支')
run('git checkout main', check=True)