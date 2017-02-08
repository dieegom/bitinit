$(document).ready(function(){
    $('.parallax').parallax();
    $('.collapsible').collapsible();
    $('#firef').fadeTo("opacity",0);
    var options = [
        {selector: '#firef', offset: 200, callback: function(el)  {
             Materialize.fadeInImage($(el));
        } }
    ];
    Materialize.scrollFire(options);
});

