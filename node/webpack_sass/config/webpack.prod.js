const merge = require('webpack-merge');
const common = require('./webpack.common.js');
const webpack = require('webpack');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = merge(common, {
    mode: 'production',
    devtool: 'source-map',
    module: {
        rules: [
            {
                test: /\.css$/i,
                use: ['style-loader', MiniCssExtractPlugin.loader, 'css-loader']
            },
            {
                test: /\.scss$/i,
                use: ['style-loader', MiniCssExtractPlugin.loader, 'css-loader', 'sass-loader'],
            },
            {
                test: /\.(gif|png|jpe?g|svg)$/i,
                use: ['url-loader?limit=8192&outputPath=img', 'image-webpack-loader']
            }
        ]
    },
    plugins: [
        new MiniCssExtractPlugin({ filename: '[name].buddle.css' }),
        new webpack.DefinePlugin({ 'process.env.NODE_ENV': JSON.stringify('production') })
    ]
});
