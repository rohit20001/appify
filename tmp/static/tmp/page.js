$(document).ready(function(){
$('.icon').click(function(){
    $('.togle').toggle();
});
$('.king').click(function(){
    $('.togle').hide();
});
// Animation for feedback
    $('#scrleft').click(function(){
        $(".sub5").fadeOut();
         $(".dsub5").animate({
            height:'20px',
            width: '5%',
            overflow:'visible',
        });
        $(".dsub5").animate({
            right: "-100%"
        });
    });
    $('#scrright').click(function(){
        $(".sub5").fadeOut();
        $(".dsub5").animate({
            height:'20px',
            width: '5%',
            overflow:'visible',
        });
        $(".dsub5").animate({
            left: "-100%"
        });
    });
});