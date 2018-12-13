const gulp = require('gulp')
const plumber = require('gulp-plumber')
const autoprefixer = require('gulp-autoprefixer')
const cleanCSS = require('gulp-clean-css')
const rename = require('gulp-rename')
const sass = require('gulp-sass')
const sourcemaps = require('gulp-sourcemaps')
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

gulp.task('sass', ()=> {
  return gulp.src(options.root+'/src/styles/main.scss')
	  .pipe(plumber())
		.pipe(sourcemaps.init())
	  .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
		.pipe(rename('main.css'))
		.pipe(sourcemaps.write())
    .pipe(gulp.dest(options.root+'/build/css'))
})

gulp.task('css', gulp.series('sass', ()=>{
  return gulp.src(options.root+'/build/css/main.css')
	  .pipe(plumber())
		.pipe(sourcemaps.init())
    .pipe(autoprefixer())
		.pipe(cleanCSS({compatibility: 'ie7'}))
		.pipe(sourcemaps.write())
    .pipe(gulp.dest(options.root+'/build/css'))
}))
