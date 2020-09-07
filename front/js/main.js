$(function () {
    $('.multiple-items').slick({
        infinite: true,
        slidesToShow: 5,
        slidesToScroll: 1,
        autoplay: false,
        autoplaySpeed: 2000,
        dots: false,
        centerMode: true,
        centerPadding: '0',
        responsive: [
            {
              breakpoint: 1024,
              settings: {
                slidesToShow: 3,
                slidesToScroll: 1
              }
            },
            {
              breakpoint: 768,
              settings: {
                slidesToShow: 2,
                slidesToScroll: 1
              }
            }
          ]
    });
});

        var posY;
        $(document).ready(function() {
           $("#gologin").on("click", function(){
               $(".wrap").show();
               $(".dim").show();
               $('html').css({'overflow':'hidden', 'height':'100%'});
               $('html').on('scroll touchmove mousewheel', function(event){
                   event.preventDefault();
                   event.stopPropagation();
                   return false;
               })

               $("#sign").on("click", function() {
                   $(".siwrap").show();
                   $(".dim").show();
                   $(".wrap").hide();
                   
                   });
                   $(".wrap .close").on("click", function() {
                       $(".wrap").hide();
                       $(".dim").hide();
                   })
           });
           });

           $(".siwrap .close").on("click", function() {
               $(".siwrap").hide();
               $(".dim").hide();
           });

           var posY;
        $(document).ready(function() {
           $("#gosignup").on("click", function(){
               $(".siwrap").show();
               $(".dim").show();
               $('html').css({'overflow':'hidden', 'height':'100%'});
               $('html').on('scroll touchmove mousewheel', function(event){
                   event.preventDefault();
                   event.stopPropagation();
                   return false;
               })

    
                   $(".siwrap .close").on("click", function() {
                       $(".siwrap").hide();
                       $(".dim").hide();
                   })
           });
           });


            $('#email-input').on('input', validButton);
            $('#password-input').on('input', validButton);
            
            function validButton() {
            if (($('#email-input').val() === '') || ($('#password-input').val() === '')) {
                $('.submit').css('background-color', '#9B9B9B');
            } else {
                $('.submit').css('background-color', 'white');
            }
            }

            $('#signemail-input').on('input', validinButton);
            $('#signpassword-input').on('input', validinButton);
            $('#signpassword-reinput').on('input', validinButton);
            
            function validinButton() {
            if (($('#signemail-input').val() !== '') && ($('#signpassword-input').val() !== '') && ($('#signpassword-reinput').val() !== '')) {
                $('.submit').css('background-color', 'white');
            } else {
                $('.submit').css('background-color', '#9B9B9B');
            }
            }