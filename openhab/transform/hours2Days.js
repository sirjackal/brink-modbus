(function(hours) {
    return Math.floor(hours / 24);
    //return Math.floor(hours / 24).toString() + ' dni ' + (hours % 24).toString() + ' h';
})(input)
