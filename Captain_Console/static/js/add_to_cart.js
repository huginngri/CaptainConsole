
function add_to_cart_js(product) {
    console.log(product)

    $.ajax({
        type: "POST",
        method: 'POST',
        url: '/carts/',
        data: {
            product_id: product,
            username: $("#username").val(),
            csrfmiddlewaretoken: $('[name="csrfmiddlewaretoken"]').val()
        },
        success: function (response) {
            console.log(response.count)
            console.log('virkar')
            let cart_number = document.getElementById("cart_count");
            cart_number.textContent = response.count;
        },
        error: function (xhr, status, error) {
            console.log('eitthvað vilaust')
        }
    });
}

