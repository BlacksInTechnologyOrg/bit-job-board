const path = require('path');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
  chainWebpack: webpackConfig => {
    if (process.env.NODE_ENV === 'production') {
      const inlineLimit = 10000;
      const assetsPath = 'static/assets';

      webpackConfig
        .output
        .filename(path.join(assetsPath, 'js/[name].[chunkhash:8].js'))
        .chunkFilename(path.join(assetsPath, '/js/chunk[id].[chunkhash:8].js'))

      webpackConfig.plugin('extract-css')
        .use(MiniCssExtractPlugin, [{
          filename: path.join(assetsPath, 'css/[name].[contenthash:8].css'),
          chunkFilename: "[id].[contenthash:8].css"
        }])

      webpackConfig.module
        .rule('images')
        .test(/\.(png|jpe?g|gif)(\?.*)?$/)
        .use('url-loader')
        .loader('url-loader')
        .options({
          limit: inlineLimit,
          name: path.join(assetsPath, 'img/[name].[hash:8].[ext]')
        })

      webpackConfig.module
        .rule('fonts')
        .test(/\.(woff2?|eot|ttf|otf)(\?.*)?$/i)
        .use('url-loader')
        .loader('url-loader')
        .options({
          limit: inlineLimit,
          name: path.join(assetsPath, 'fonts/[name].[hash:8].[ext]')
        })
    }
  }
}