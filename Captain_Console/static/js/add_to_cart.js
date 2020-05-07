
function add_to_cart_js(product) {
    console.log(product)
    $.ajax({
        type: "GET",
        url: '/carts',
        data: {product_id: product},
        success: function (response) {
            console.log(response.data['count'])
        },
        error: function (xhr, status, error) {
            console.log('Þóranna er belja')
        }
    });
}
