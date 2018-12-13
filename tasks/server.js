const gulp = require('gulp')
const plumber = require('gulp-plumber')
const browserSync = require('browser-sync').create()
const minimist = require('minimist')

const knownOptions = {
  string: 'root',
  string: 'home',
  default: {
    root: 'default',
    home: 'itredatalab.org'
  }
}
const options = minimist(process.argv.slice(2), knownOptions)


gulp.task('serve', function(done) {
  browserSync.init({
    server: {
      baseDir: options.root+'/build'
    }
  }, function (err, bs) {
    bs.addMiddleware("*", require('connect-gzip-static')(options.root+'/build'), {
      override: true
    })
  })
  gulp.watch(options.root+'/src/scripts/**/*', gulp.series('javascript', 'reload'))
  gulp.watch(options.root+'/src/styles/**/*', gulp.series('css', 'reload'))
  gulp.watch(options.root+'/src/**/*.nunjucks', gulp.series('html', 'reload'))
  gulp.watch(options.root+'/src/nunjucks/data.json', gulp.series('html', 'reload'))
  done();
})

gulp.task('reload', (done)=> {
  browserSync.reload()
  done();
})
