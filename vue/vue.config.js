module.exports = {
  //关闭es6
  lintOnSave: true,
  chainWebpack: config => {
    config
      .plugin('html')
      .tap(args => {
        args[0].title='CTGU自动安全上报'
        return args
      })
  }
}