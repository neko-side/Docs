import { defineConfig } from 'vitepress'

export default defineConfig({
	title: "nekoside",
	description: "",
	base: "/docs/",
	themeConfig: {
		sidebar: {
			'/IDE-Shortcuts/': { base: '/IDE-Shortcuts/', items: sideBarIDE() }
		},
		siteTitle: false,
		nav: [
			{
				text: '博客',
				link: 'https://nekoside.com/',
				target: '_self'
			},
			{
				text: '文档',
				link: '/',
				target: '_self'
			}
		]
	}
})

function sideBarIDE() {
	return [
		{
			items: [
				{ text: 'File', link: '/File/' },
				{ text: 'Tools', link: '/Tools/' },
				{ text: 'Code', link: '/Code/' },
				{ text: 'Project', link: '/Project/' }
			]
		}
	]
}