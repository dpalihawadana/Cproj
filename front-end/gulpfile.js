(function () {
    'use strict';

    var gulp = require('gulp');
    require('require-dir')('gulp');

    gulp.task('default', function () {
        gulp.start('build-and-run');
    });
})();
