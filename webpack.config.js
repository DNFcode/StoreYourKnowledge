"use strict";
var webpack = require('webpack');
var path = require('path');
var loaders = require('./webpack.loaders');

const HOST = process.env.HOST || "127.0.0.1";
const PORT = process.env.PORT || "8888";

// global css
loaders.push({
	test: /[\/\\](node_modules|global)[\/\\].*\.css$/,
	loaders: [
		'style?sourceMap',
		'css'
	]
});
// local scss modules
loaders.push({
	test: /[\/\\]assets[\/\\].*\.scss/,
	exclude: /(node_modules|bower_components|bundles)/,
	loaders: [
		'style?sourceMap',
		'css',
		// 'postcss',
		'sass'
	]
});

// local css modules
loaders.push({
	test: /[\/\\]assets[\/\\].*\.css/,
	exclude: /(node_modules|bower_components|bundles)/,
	loaders: [
		'style?sourceMap',
		'css?modules&importLoaders=1&localIdentName=[path]___[name]__[local]___[hash:base64:5]1'
	]
});

module.exports = {
	entry: [
    `webpack-dev-server/client?http://${HOST}:${PORT}`,
		`webpack/hot/only-dev-server`,
    './assets/js/index'
	],
	devtool: process.env.WEBPACK_DEVTOOL || 'cheap-module-source-map',
	output: {
		path: path.join(__dirname, 'assets/bundles'),
		filename: 'bundle.js',
    publicPath: '/static/'
	},
	resolve: {
		extensions: ['', '.js', '.jsx'],
    alias: {
      css: path.join(__dirname, 'assets/css')
    }
	},
	module: {
		loaders
	},
	devServer: {
		contentBase: "./assets/bundles",
		// do not print bundle build stats
		// noInfo: true,
		// enable HMR
		hot: true,
		// embed the webpack-dev-server runtime into the bundle
		inline: true,
		// serve index.html in place of 404 responses to allow HTML5 history
		historyApiFallback: true,
		port: PORT,
		host: HOST,

		proxy: {
      '*': {
        target: 'http://127.0.0.1:8000',
        secure: false
      }
    }
	},
	plugins: [
		// new webpack.NoErrorsPlugin(),
		new webpack.HotModuleReplacementPlugin()
	]
};
