
function calculate_cart() {
    $.ajax({
        type: "GET",
        url: '/carts/',
        success: function (response) {
            console.log(response.count)

            let cart_number = document.getElementById("cart_count");
            cart_number.textContent = response.count;
        },
        error: function (xhr, status, error) {
            console.log('Request failed')
        }
    });
}