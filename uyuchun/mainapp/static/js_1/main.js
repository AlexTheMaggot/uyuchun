$(window).on('load', function () {
    // Plug
    $('.window').removeClass('window_loading');
    setTimeout(function() {
        $('.main-block').removeClass('main-block_loading');
    }, 500);
    $('#main-block__submit').on('click', function() {
        $('#form-block').removeClass('form-block_none');
        $('#main-block').addClass('main-block_closed');
        setTimeout(function() {
            $('#form-block').removeClass('form-block_closed');
            $('#main-block').addClass('main-block_none');
        }, 500);
    });
    // End Plug

    $('body').css({'opacity': '1', 'background': '#333333'});
    $('#burger').on('click', function () {
        if ($('.burger__strip_1').hasClass('burger__strip_1_rotated')) {
            $('.menu__col').addClass('menu__col_closed');
            $('.burger__strip_1').removeClass('burger__strip_1_rotated');
            $('.burger__strip_2').removeClass('burger__strip_2_rotated');
            $('.burger__strip_3').removeClass('burger__strip_3_rotated');
            $('.burger__strip').addClass('burger__strip_onestrip');
            setTimeout(function () {
                $('.burger__strip').removeClass('burger__strip_onestrip');
            }, 100);
        } else {
            $('.menu__col').removeClass('menu__col_closed');
            $('.burger__strip').addClass('burger__strip_onestrip');
            setTimeout(function () {
                $('.burger__strip_1').addClass('burger__strip_1_rotated');
                $('.burger__strip_2').addClass('burger__strip_2_rotated');
                $('.burger__strip_3').addClass('burger__strip_3_rotated');
                $('.burger__strip').removeClass('burger__strip_onestrip');
            }, 100);
        }
    });
    $('#menu_categories').on('click', function () {
        if ($(this).hasClass('clicked')) {
            $(this).removeClass('clicked');
            $('#menu_arrow').removeClass('menu__arrow_opened');
        }
        else {
            $(this).addClass('clicked');
            $('#menu_arrow').addClass('menu__arrow_opened');
        }
    });
});