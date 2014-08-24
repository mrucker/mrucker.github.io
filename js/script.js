$(function() {
    $('.include').each(function() {
        var $include = $(this);
        $.get($include.data('src'), function(content) {
            $include.html(content);
        });
    });
});