import { defineConfig } from 'vitepress'

export default defineConfig({
	title: "nekoside",
	description: "",
	base: "/docs/",
	themeConfig: {
		sidebar: [
			{

			}
		],
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
				{ text: 'File', link: '/IDE-Shortcuts/File/' },
				{ text: 'Tools', link: '/IDE-Shortcuts/Tools/' },
				{ text: 'Code', link: '/IDE-Shortcuts/Code/' },
				{ text: 'Project', link: '/IDE-Shortcuts/Project/' }
			]
		}
	]
}