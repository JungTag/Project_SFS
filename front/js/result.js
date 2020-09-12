const $grid = $('.result').masonry({
    itemSelector: '.item',
    fitwidth: true,
    horizontalOrder: true,
    percentPosition: true
});

$grid.imagesLoaded().progress(function() {
$grid.masonry('layout');
});