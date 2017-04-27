$(() => {
    $(".menu-button").hover(() => {
        $(".menu-items").fadeIn(400);
    });

    $(".menu").hover(null, () => {
        $(".menu-items").fadeOut(400);
    });

    var TRANSLATION_HOVER_SPEED_OUT = 100;
    var TRANSLATION_HOVER_SPEED_IN = 300;
    $(".menu-items a").hover(function() {
        var $a = $(this);
        var $span = $(this).find("span");
        var jp = $(this).data("jp");
        $span.fadeOut(TRANSLATION_HOVER_SPEED_OUT, function() {
            $(".menu-items").addClass("up");
            $a.addClass("menu-jp");
            $(this).text(jp);
            $(this).fadeIn(TRANSLATION_HOVER_SPEED_IN);
        });

        // $(this).text($(this).data("jp"));
    }, function() {
        var $a = $(this);
        var $span = $(this).find("span");
        var en = $(this).data("en");
        $span.fadeOut(TRANSLATION_HOVER_SPEED_OUT, function() {
            $(".menu-items").removeClass("up");
            $a.removeClass("menu-jp");
            $(this).text(en);
            $(this).fadeIn(TRANSLATION_HOVER_SPEED_IN);
        });
    });

    var set = false;
    $("input.clear").on("input", function() {
        console.log($(this).val());
        if ($(this).val() != "") {
            if (!set) {
                $(".enter-box").fadeIn(1000);
            }
            set = true;
        }
        else {
            setTimeout(function() {
                if ($("input.clear").val() == "") {
                    $(".enter-box").fadeOut(1000);
                    set = false;
                }
            }, 200);
        }
    });
});