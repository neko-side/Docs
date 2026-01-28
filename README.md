# Deploy

```python
from subprocess import run
run('pnpm npx halo-static-pages-deploy-cli deploy -e <halo站点地址> -i <halo静态页面地址> -t <halo令牌> -f ./docs/.vitepress/dist')
```