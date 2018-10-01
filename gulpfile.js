const gulp = require('gulp')

const browserSync = require('browser-sync').create()
const cleanCSS = require('gulp-clean-css')
const concat = require('gulp-concat')
const del = require('del')
const minimist = require('minimist')
const optimizejs = require('gulp-optimize-js')
const plumber = require('gulp-plumber')
const rename = require('gulp-rename')
const imagemin = require('gulp-imagemin')
const responsive = require('gulp-responsive')
const sass = require('gulp-sass')
const sourcemaps = require('gulp-sourcemaps')
const uglify = require('uglify-es')

const composer = require('gulp-uglify/composer')
const minify = composer(uglify, console)

const knownOptions = {
  string: 'root',
  default: { root: '.'}
};

const options = minimist(process.argv.slice(2), knownOptions)

gulp.task('serve', function(done) {
  browserSync.init({
    server: {
      baseDir: options.root+'/build'
    }
  })
  gulp.watch(options.root+'/src/**/*', gulp.series('quick-compile', 'reload'))
  done();
})

gulp.task('reload', function(done) {
  browserSync.reload()
  done();
})

gulp.task('javascript', () => {
	return gulp.src(options.root+'/src/scripts/*.js')
		.pipe(plumber())
		.pipe(concat('bundled.js'))
		.pipe(minify())
    .pipe(optimizejs())
		.pipe(rename('bundled.min.js'))
		.pipe(gulp.dest(options.root+'/build'))
})

gulp.task('css', function() {
  return gulp.src(options.root+'/src/styles/main.scss')
	  .pipe(plumber())
		.pipe(sourcemaps.init())
	  .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
		.pipe(sourcemaps.write())
		.pipe(cleanCSS({compatibility: 'ie8'}))
		.pipe(rename('main.css'))
    .pipe(gulp.dest(options.root+'/build/css'))
    .pipe(browserSync.stream())
})

gulp.task('images', () => {
	return gulp.src(options.root+'/src/assets/*.{png,jpg,jpeg}')
		.pipe(plumber())
    .pipe(responsive({
      'staff-*': {
        width: 150,
        format: 'webp',
        rename: {extname: ".webp"}
      },
      'icon-*': {
        width: 150,
        format: 'webp',
        rename: {extname: ".webp"}
      },
      'logo-*': {
        format: 'webp',
        rename: {extname: ".webp"}
      },
      'misc-*': {
        format: 'webp',
        rename: {extname: ".webp"}
      },
    }))
		.pipe(imagemin())
		.pipe(gulp.dest(options.root+'/build/assets'))
})

gulp.task('html', () => {
	return gulp.src(options.root+'/src/*.html')
		.pipe(plumber())
		.pipe(gulp.dest(options.root+'/build'))
})

gulp.task('compile', gulp.series(()=>{return del(options.root+'/build')}, 'javascript', 'css', 'images', 'html'))
gulp.task('quick-compile', gulp.series('javascript', 'css', 'html'))

gulp.task('build', gulp.series('compile', 'serve'))
gulp.task('build-images', gulp.series(()=>{return del(options.root+'/build/assets')}, 'images'))

/*
gulp.task('javascript', () => {
	return gulp.src('./src/js/*.js')
		.pipe(plumber())
		.pipe(concat('bundled.js'))
		.pipe(uglify())
    .pipe(optimizejs())
		.pipe(rename('bundled.min.js'))
		.pipe(gulp.dest('./build'))
})

gulp.task('css', function() {
  return gulp.src('./src/scss/main.scss')
	  .pipe(plumber())
		.pipe(sourcemaps.init())
	  .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
		.pipe(sourcemaps.write())
		.pipe(cleanCSS({compatibility: 'ie8'}))
		.pipe(rename('main.css'))
    .pipe(gulp.dest('./build/css'));
})

gulp.task('html', () => {
	return gulp.src('./src/*.html')
		.pipe(plumber())
		.pipe(htmlmin({collapseWhitespace: true}))
		.pipe(gulp.dest('./build'))
})
gulp.task('images', () => {
	return gulp.src('./src/assets/*')
		.pipe(plumber())
		.pipe(imagemin())
		.pipe(gulp.dest('./build'))
})

gulp.task('clean', () => {
	return del(['build'])
})

gulp.task('default', gulp.series('javascript', 'css', 'html', 'images'))

gulp.task('build', gulp.series('clean', 'default'))
*/
