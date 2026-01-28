import { defineConfig } from 'vitepress'

export default defineConfig({
    title: "nekoside",
    description: "",
    base: "/docs/",
    themeConfig: {
        siteTitle: false,
        nav: [
            {
                text: '博客',
                link: 'https://nekoside.com/',
                target: '_self'
            },
            {
                text: '文档',
                link: 'https://nekoside.com/docs/',
                target: '_self'
            }
        ]
    }
})
