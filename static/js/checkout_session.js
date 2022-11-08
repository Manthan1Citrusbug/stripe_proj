const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
const product_id = document.querySelector('#product_id').value;
$('#checkout-button').click(function(){
    $.ajax({
        url : '../create-checkout-session/',
        type : 'POST',
        headers: {'X-CSRFToken': csrftoken},
        data : {'id':product_id},
        success : function(data, textStatus, jqXHR)
        {
            window.location.replace(data['url']);
        },
    });
});