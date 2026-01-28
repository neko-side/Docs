from subprocess import run
from tomllib import load

with open('settings.toml', 'rb') as file:
    settings = load(file)

website = settings['info']['website']
key = settings['info']['key']
id = settings['info']['id']

run('pnpm build')

run('pnpm npx halo-static-pages-deploy-cli deploy -e ' + website + ' -i ' + id + ' -t ' + key + ' -f ./docs/.vitepress/dist')