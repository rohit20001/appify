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
        });
        $(".dsub5").animate({
            right: "-100%"
        },'slow',function(){
            $(".dsub5").css("right","100%");
        });
        $(".dsub5").animate({
            right: "0%"
        });
        $(".dsub5").animate({
            height:'250px',
            width: '20%',
        });
        $('.sub5').fadeIn();

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
        },'slow',function(){
           $(".dsub5").css("left","100%");  
        });
        $(".dsub5").animate({
            left: "0%"
        });
        $(".dsub5").animate({
            height:'250px',
            width: '20%',
        });
        $('.sub5').fadeIn();
    });
});