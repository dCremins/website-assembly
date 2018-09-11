const gulp = require('gulp')

const cleanCSS = require('gulp-clean-css')
const imagemin = require('gulp-imagemin')
const plumber = require('gulp-plumber')
const sass = require('gulp-sass')
const sourcemaps = require('gulp-sourcemaps')
const minimist = require('minimist');

const knownOptions = {
  string: 'root',
  default: { root: '.'}
};

const options = minimist(process.argv.slice(2), knownOptions)

gulp.task('css', function() {
  return gulp.src(options.root+'/src/css/main.scss')
	  .pipe(plumber())
		.pipe(sourcemaps.init())
	  .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
		.pipe(sourcemaps.write())
		.pipe(cleanCSS({compatibility: 'ie8'}))
    .pipe(gulp.dest(options.root+'/build/css'));
})

gulp.task('images', () => {
	return gulp.src(options.root+'/src/assets/*')
		.pipe(plumber())
		.pipe(imagemin())
		.pipe(gulp.dest(options.root+'/build/assets'))
})

gulp.task('html', () => {
	return gulp.src(options.root+'/src/*.html')
		.pipe(plumber())
		.pipe(gulp.dest(options.root+'/build'))
})


gulp.task('build', gulp.series('css', 'images', 'html'))

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
