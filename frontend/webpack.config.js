const HtmlWebPackPlugin = require('html-webpack-plugin');
const htmlPlugin = new HtmlWebPackPlugin({
    template: './src/index.html',
    filename: './index.html'
});
const Dotenv = require('dotenv-webpack');


module.exports = {
    mode: 'development',
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: ['babel-loader'],
            },
            {
                test: /\.(scss|css)$/,
                use: [
                    'style-loader',
                    'css-loader',
                ]
            }
        ],
       
    },
    resolve: {
        extensions: ['*', '.js', '.jsx', '.css'],
        fallback: {
            "fs": false,
            "os": false,
            "path": false
          },
    },
    plugins: [
        htmlPlugin,
        new Dotenv()
    ],
    
};