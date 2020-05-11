function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
    });

function add_to_cart_js(product) {


    $.ajax({
        type: "POST",
        method: 'POST',
        url: '/carts/',
        data: {
            product_id: product
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

function calculate_cart(user_id) {
    $.ajax({
        type: "GET",
        url: '/carts',
        data: {
            user_id: user_id
        },
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

function place_order(billing, payment) {
    console.log('hallo')
    $.ajax({
        type: "POST",
        method: 'POST',
        url: '/orders/checkout/overview',
        data: {
            billing: billing,
            payment: payment
        },
        success: function (response) {
            console.log('virkar')
            let header = document.getElementById('order_header')
            header.textContent = 'Order confirmed'
            let back_button = document.getElementById('edit_order')
            let confirm_button = document.getElementById('confirm_order')
            back_button.remove()
            confirm_button.remove()
            let a = document.createElement('a')
            a.setAttribute('href', '/')
            a.textContent = 'Close'
            let div = document.getElementById('order_review_div')
            div.appendChild(a)
        },
        error: function (xhr, status, error) {
            console.log('eitthvað vilaust')
        }
    });
}

function go_back(billing, payment) {
    $.ajax({
        type: "GET",
        method: 'GET',
        url: '/orders/checkout/update',
        data: {
            billing: billing,
            payment: payment
        },
        success: function (response) {
            console.log(response)
            console.log('hallo')
            window.location = "/"
        },
        error: function (xhr, status, error) {
            console.log('eitthvað vilaust')
        }
    });
}
