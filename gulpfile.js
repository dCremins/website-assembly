
const gulp = require('gulp')
const del = require('del')
const gzip = require('gulp-gzip')
const log = require('fancy-log')
const plumber = require('gulp-plumber')
const minimist = require('minimist')

const HubRegistry = require('gulp-hub');
const hub = new HubRegistry(['tasks/*.js']);

gulp.registry(hub);

const knownOptions = {
  string: 'root',
  string: 'home',
  default: {
    root: 'default',
    home: 'itredatalab.org'
  }
}
const options = minimist(process.argv.slice(2), knownOptions)

const tasks = {
  style: true,
  script: true,
  blog: true,
  images: true,
  favicon: true,
  gzip: false
}
gulp.task('skip', (done) => {
  done()
})

gulp.task('gzip', () => {
	return gulp.src([
    options.root+'/build/*.js',
    options.root+'/build/*.html',
    options.root+'/build/css/*.css'
  ])
		.pipe(plumber())
    .pipe(gzip())
		.pipe(gulp.dest(options.root+'/build'))
})

gulp.task('compile', gulp.series(
  ()=>{ return del(options.root+'/build') },
  tasks.script ? 'javascript' : 'skip',
  tasks.style ? 'css' : 'skip',
  tasks.images ? 'images' : 'skip',
  tasks.images ? 'imageMin' : 'skip',
  tasks.favicon ? 'favicon' : 'skip',
  tasks.blog ? 'markdown' : 'html',
  tasks.gzip ? 'gzip' : 'skip'
))

gulp.task('compile-pretty', gulp.series(
  ()=>{ return del(options.root+'/build') },
  'javascript',
  'css',
  'images',
  'imageMin',
  'favicon',
  'html-pretty'
))

gulp.task('quick-compile', gulp.series(()=>{
  return del([
    options.root+'/build/css',
    options.root+'/build/*.html',
    options.root+'/build/*.js'
  ])
}, 'html', 'javascript', 'css'))

gulp.task('build', gulp.series('compile', 'serve'))
