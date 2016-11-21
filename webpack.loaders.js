module.exports = [
	// {
	// 	test: /\.jsx?$/,
	// 	exclude: /(node_modules|bower_components|bundles)/,
	// 	loaders: ['react-hot-loader/webpack']
	// },
	{
		test: /\.jsx?$/,
		exclude: /(node_modules|bower_components|bundles)/,
		loaders: ['react-hot-loader/webpack', 'babel?presets[]=react,presets[]=es2015,plugins[]=transform-decorators-legacy,plugins[]=transform-class-properties'],
		// query: {
		//   presets: ['es2015', 'react'],
		//   plugins: ['transform-runtime', 'transform-decorators-legacy', 'transform-class-properties'],
		// }
	},
	{
		test: /\.(ttf|eot|svg|woff(2)?)(\?[a-z0-9=&.]+)?$/,
		loader: 'file-loader'
	},
	// {
	// 	test: /\.eot(\?v=\d+\.\d+\.\d+)?$/,
	// 	exclude: /(node_modules|bower_components)/,
	// 	loader: "file"
	// },
	// {
	// 	test: /\.(woff|woff2)$/,
	// 	exclude: /(node_modules|bower_components)/,
	// 	loader: "url?prefix=font/&limit=5000"
	// },
	// {
	// 	test: /\.ttf(\?v=\d+\.\d+\.\d+)?$/,
	// 	exclude: /(node_modules|bower_components)/,
	// 	loader: "url?limit=10000&mimetype=application/octet-stream"
	// },
	// {
	// 	test: /\.svg(\?v=\d+\.\d+\.\d+)?$/,
	// 	exclude: /(node_modules|bower_components)/,
	// 	loader: "url?limit=10000&mimetype=image/svg+xml"
	// },
	{
		test: /\.gif/,
		exclude: /(node_modules|bower_components)/,
		loader: "url-loader?limit=10000&mimetype=image/gif"
	},
	{
		test: /\.jpg/,
		exclude: /(node_modules|bower_components)/,
		loader: "url-loader?limit=10000&mimetype=image/jpg"
	},
	{
		test: /\.png/,
		exclude: /(node_modules|bower_components)/,
		loader: "url-loader?limit=10000&mimetype=image/png"
	}
];
