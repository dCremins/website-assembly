const gulp = require('gulp')

const browserSync = require('browser-sync').create()
const cleanCSS = require('gulp-clean-css')
const concat = require('gulp-concat')
const data = require('gulp-data')
const del = require('del')
const favicons = require("favicons").stream
const htmlmin = require('gulp-htmlmin')
const imagemin = require('gulp-imagemin')
const minimist = require('minimist')
const nunjucksRender = require('gulp-nunjucks-render')
const optimizejs = require('gulp-optimize-js')
const plumber = require('gulp-plumber')
const rename = require('gulp-rename')
const responsive = require('gulp-responsive')
const sass = require('gulp-sass')
const sourcemaps = require('gulp-sourcemaps')
const uglify = require('uglify-es')

const composer = require('gulp-uglify/composer')
const minify = composer(uglify, console)

const knownOptions = {
  string: 'root',
  default: { root: 'default'}
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
	return gulp.src(options.root+'/src/assets/*.{png,jpg,jpeg,gif}')
		.pipe(plumber())
    .pipe(responsive({
      'staff-*': [{
        width: 150,
        format: 'webp',
        rename: {extname: ".webp"}
      }, {
        width: 150,
        format: 'png',
        rename: {extname: ".png"}
      }],
      'icon-*': [{
        width: 150,
        format: 'webp',
        rename: {extname: ".webp"}
      }, {
        width: 150,
        format: 'png',
        rename: {extname: ".png"}
      }],
      'logo-*': [{
        format: 'webp',
        rename: {extname: ".webp"}
      }, {
        format: 'png',
        rename: {extname: ".png"}
      }],
      'misc-*': [{
        format: 'webp',
        rename: {extname: ".webp"}
      }, {
        format: 'png',
        rename: {extname: ".png"}
      }],
    }, {
      errorOnUnusedConfig: false
    }))
		.pipe(imagemin())
		.pipe(gulp.dest(options.root+'/build/assets'))
})

gulp.task('favicon', () => {
	return gulp.src(options.root+'/src/assets/logo.png')
		.pipe(plumber())
    .pipe(favicons({
        version: 1.0,
        logging: false,
        replace: true,
        icons: {
          android: false,              // Create Android homescreen icon. `boolean` or `{ offset, background, mask, overlayGlow, overlayShadow }`
          appleIcon: false,            // Create Apple touch icons. `boolean` or `{ offset, background, mask, overlayGlow, overlayShadow }`
          appleStartup: false,         // Create Apple startup images. `boolean` or `{ offset, background, mask, overlayGlow, overlayShadow }`
          coast: false,                // Create Opera Coast icon. `boolean` or `{ offset, background, mask, overlayGlow, overlayShadow }`
          favicons: true,             // Create regular favicons. `boolean` or `{ offset, background, mask, overlayGlow, overlayShadow }`
          firefox: false,              // Create Firefox OS icons. `boolean` or `{ offset, background, mask, overlayGlow, overlayShadow }`
          windows: false,              // Create Windows 8 tile icons. `boolean` or `{ offset, background, mask, overlayGlow, overlayShadow }`
          yandex: false
        }
    }))
		.pipe(gulp.dest(options.root+'/build/'))
})

/*
gulp.task('html', () => {
	return gulp.src(options.root+'/src/*.html')
		.pipe(plumber())
		.pipe(gulp.dest(options.root+'/build'))
})
*//
gulp.task('html', function() {
  return gulp.src(options.root+'/src/*.+(html|nunjucks)')
		.pipe(plumber())
    .pipe(data(() => {
			return require('./'+options.root+'/src/nunjucks/data.json')
		}))
    .pipe(nunjucksRender({
      path: [options.root+'/src/nunjucks/']
    }))
    .pipe(htmlmin(
      {
        collapseWhitespace: true,
        removeComments: true
      }))
    .pipe(gulp.dest(options.root+'/build'))
})

gulp.task('compile', gulp.series(()=>{return del(options.root+'/build')}, 'javascript', 'css', 'images', 'favicon', 'html'))
gulp.task('quick-compile', gulp.series('javascript', 'css', 'html'))

gulp.task('build', gulp.series('compile', 'serve'))
gulp.task('build-images', gulp.series(()=>{return del(options.root+'/build/assets')}, 'images'))
