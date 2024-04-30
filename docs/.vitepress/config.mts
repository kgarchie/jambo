import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
    title: "Jambo Docs",
    description: "Documentation for Jambo Customer Management REST API",
    base: "/jambo/",
    themeConfig: {
        // https://vitepress.dev/reference/default-theme-config
        nav: [
            { text: 'Home', link: '/' },
            { text: 'Examples', link: '/api/examples' }
        ],
        sidebar: [
            {
                text: 'Getting Started',
                items: [
                    { text: 'Installation', link: '/api/quickstart' },
                    {
                        text: 'REST API', items: [
                            { text: 'Customers', link: '/api/customer' },
                            { text: 'Businesses', link: '/api/business' },
                            { text: 'Location', link: '/api/location' },
                            { text: 'Status', link: '/api/status' }
                        ]
                    }
                ],
            }
        ],

        socialLinks: [
            { icon: 'github', link: 'https://github.com/kgarchie' },
            { icon: 'linkedin', link: 'https://www.linkedin.com/in/allan-bosire/' }
        ]
    },
    lang: 'en-US',
    head: [
        ['link', { rel: 'icon', href: 'https://raw.githubusercontent.com/kgarchie/jambo/main/docs/favicon.ico' }],
        ['script', {src: 'https://www.googletagmanager.com/gtag/js?id=G-QWXHWYF3Z6', async: 'async'}],
        ['script', {}, `
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
        
            gtag('config', 'G-QWXHWYF3Z6');`
        ]
    ],
    ignoreDeadLinks: [
        // ignore exact url "/playground"
        '/playground',
        // ignore all localhost links
        /^https?:\/\/localhost/,
        // ignore all links include "/repl/""
        /\/repl\//,
        // custom function, ignore all links include "ignore"
        (url) => {
            return url.toLowerCase().includes('ignore')
        }
    ]
})
