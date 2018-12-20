const gulp = require('gulp')
const concat = require('gulp-concat')
const minimist = require('minimist')
const optimizejs = require('gulp-optimize-js')
const plumber = require('gulp-plumber')
const rename = require('gulp-rename')
const sourcemaps = require('gulp-sourcemaps')
const composer = require('gulp-uglify/composer')
const uglify = require('uglify-es')
const minify = composer(uglify, console)

const knownOptions = {
  string: 'root',
  string: 'home',
  default: {
    root: 'default',
    home: 'itredatalab.org'
  }
}
const options = minimist(process.argv.slice(2), knownOptions)

gulp.task('javascript', () => {
	return gulp.src(options.root+'/src/scripts/*.js')
		.pipe(plumber())
		.pipe(concat('bundled.js'))
		.pipe(minify())
    .pipe(optimizejs())
		.pipe(rename('bundled.min.js'))
		.pipe(gulp.dest(options.root+'/build'))
})

gulp.task('javascript-python', () => {
	return gulp.src(options.root+'/src/scripts/*.js')
		.pipe(plumber())
		.pipe(concat('bundled.js'))
		.pipe(minify())
    .pipe(optimizejs())
		.pipe(rename('bundled.min.js'))
		.pipe(gulp.dest(options.root+'/build/assets'))
})
