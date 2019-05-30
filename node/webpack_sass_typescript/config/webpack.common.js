const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');

module.exports = {
    entry: {
        index: path.resolve(__dirname, '..', 'src', 'index.js')
    },
    output: {
        filename: '[name].bundle.js',
        path: path.resolve(__dirname, '..', 'dist')
    },
    resolve: {
        extensions: [".ts", ".tsx", ".js"]
    },
    module: {
        rules: [
            { test: /\.tsx?$/, loader: "ts-loader" }
        ]
    },
    plugins: [
        new CleanWebpackPlugin(),
        new HtmlWebpackPlugin({
            inject: false,
            template: require('html-webpack-template'),
            lang: 'cmn-hans',
            mobile: true,
            title: 'Demo',
            // meta: [
            //     {
            //         name: 'description',
            //         content: 'A better default template for html-webpack-plugin.'
            //     }
            // ],
            // links: [
            //     {
            //         href: '/favicon-32x32.png',
            //         rel: 'icon',
            //         sizes: '32x32',
            //         type: 'image/png'
            //     }
            // ],
            // scripts: [
            //     'http://example.com/somescript.js',
            //     {
            //         src: '/myModule.js',
            //         type: 'module'
            //     }
            // ],
            // bodyHtmlSnippet: '<div id="id1"></div><div id="id2"></div>'
        })
    ]
};
