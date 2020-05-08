
function add_to_cart_js(product) {
    console.log(product)
    $.ajax({
        type: "GET",
        url: '/carts',
        data: {product_id: product},
        success: function (response) {
            console.log(response.count)

            let cart_number = document.getElementById("cart_count");
            cart_number.textContent = response.count;
        },
        error: function (xhr, status, error) {
            console.log('Þóranna er belja')
        }
    });
}

