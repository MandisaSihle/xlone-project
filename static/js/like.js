$(function(){
    var is_like = false;
    $('.js-like').click(function(){
        var x_id = $(this).data('x-id');
        var like_count_obj = $(this).parent().find('.js-like-count');
        var like_count = Number(like_count_obj.html());
        var heart_icon_obj = $(this).find('img');
        var heart_icon_url = heart_icon_obj.attr('src');
        if(heart_icon_url = JS_ICON_HEART_GREY){
            $.ajax({
                url:'/second/like/' + x_id + '/', 
                type: 'POST',
                data: {},
                headers: {'x-CSRFToken': JS_CSRFTOKEN}
            })
s
            .done((data)=>{
                var new_like_count = like_count + 1;
                like_count_obj.html(new_like_count);
                heart_icon_obj.attr('src', JS_ICON_HEART_BLUE);
            })

            .fail((data)=>{
                alert('error');
                console.log(data);
            })
        }
    })
}) 