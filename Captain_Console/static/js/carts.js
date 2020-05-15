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

function calculate_cart() {
    $.ajax({
        type: "GET",
        url: '/carts',
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

function place_order(order) {
    $.ajax({
        type: "POST",
        method: 'POST',
        url: '/orders/checkout/overview',
        data: {
            order: order
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
            a.setAttribute("class", "btn btn-danger login-btn");
            a.setAttribute('href', '/')
            a.textContent = 'Close'
            let div = document.getElementById('order_review_div')
            div.appendChild(a)
            window.scrollTo(0, 0);
            calculate_cart()
        },
        error: function (xhr, status, error) {
            console.log('error')
        }
    });
}


function remove_from_cart(product_id, child) {
    console.log('hilmar er belja')
    let deletediv = child.parentNode.parentNode.parentNode
    $.ajax({
        type: "DELETE",
        method: 'DELETE',
        url: '/carts/' + product_id,
        success: function (response) {
            console.log(response);
            console.log(response['total_price'])
            if (response['total_price'] === 0) {
                location.reload()
            }
            else {

                let container = document.getElementById("cart_products")
                for (let x = 0; x < container.children.length; x++){
                    if (container.children[x] === deletediv){
                        container.removeChild(container.children[x]);
                        break;
                    }
                }
                calculate_cart()
                let price = document.getElementById('cart_total');
                let total = parseFloat(response['total_price']);
                price.textContent = 'Total price: ' + total + '$';

            }
        },
        error: function (xhr, status, error) {
            console.log('eitthvað bla');

        }
    });
}

function change_quantity(product_id) {
    console.log(product_id)
    let inp = document.getElementById(product_id)
    let new_amount = inp.value
    $.ajax({
        type: "POST",
        method: 'POST',
        url: '/carts/change_amount/' + product_id,
        data: {
            new_amount: new_amount
        },
        success: function (response) {
            let price = document.getElementById('cart_total');
            let total = parseFloat(response['total_price']);
            price.textContent = 'Total price: ' + total + '$';

            calculate_cart()
        },
        error: function (xhr, status, error) {
            console.log('eitthvað vilaust');
        }
    });
}


function sortit(sel) {
    let all_products = document.getElementById("container_for_products")
    let the_arr = []
    let keep_arr =[]
    let name_or_price = sel.options[sel.selectedIndex].value
    let n_o_p = 0
    let r = 0
    let reverse_check = name_or_price.localeCompare("name_reverse") * name_or_price.localeCompare("price_reverse")
    if (reverse_check === 0){
        r = 1
    }
    let k = name_or_price.localeCompare("price") * name_or_price.localeCompare("price_reverse")
    if (k === 0) {
        n_o_p = 1
    }
    for (let x = 0; x<all_products.children.length; x++){
        keep_arr.push(all_products.children[x])
        let j = all_products.children[x].children[0].children[1].children[0].children[n_o_p].getAttribute("name")
        if (n_o_p ===1){
            j = parseFloat(j)
        }
        the_arr.push(j.toUpperCase())
    }
    let new_arr = []
    for (let x = 0; x<the_arr.length; x++){
        new_arr.push(the_arr[x])
    }
    if (n_o_p === 1) {
        new_arr.sort(function (a, b) {
            return a - b;
        });
    }
    else {
        new_arr.sort()
    }
    if (r === 1){
        new_arr.reverse()
    }
    let order_arr = []
    while (all_products.firstChild){
        all_products.removeChild(all_products.lastChild)
    }
    for (let x=0; x<new_arr.length; x++){
        order_arr.push(the_arr.indexOf(new_arr[x]))
    }
    for (let x=0; x<order_arr.length;x++){
        all_products.appendChild(keep_arr[order_arr[x]])
    }
}

function buy_product(product_id) {
    add_to_cart_js(product_id);
    setTimeout(function(){ window.location = '/carts/view'; }, 1000);
}

function viewOrderDetail(orderNumber){
    console.log("in function")
    background = document.getElementById("background_"+orderNumber)
    the_product_list_element = document.getElementById("list_for_"+orderNumber)

    the_product_list_element.classList.add("popupsmall","absolute","ccwhite")
    background.classList.add("cover")
}

function closeDiv(orderNumber) {
    background = document.getElementById("background_" + orderNumber)
    the_product_list_element = document.getElementById("list_for_" + orderNumber)
    the_product_list_element.classList.remove("popupsmall", "absolute", "ccwhite")
    background.classList.remove("cover")
}


function calculateRating(id, rating) {
        console.log("here1")
        star_div = document.getElementById("star_" + id);
        while (star_div.hasChildNodes()) {
            star_div.removeChild(star_div.firstChild);
        }
        // <span class="glyphicon glyphicon-shopping-cart" aria-hidden="true"></span>
        let total_rating = 5;
        while (rating > 0) {
            let star = document.createElement("span");
             star.setAttribute("class", "glyphicon glyphicon-star");
            star_div.appendChild(star);
            total_rating -= 1;
            rating -= 1;
        }
        while (total_rating > 0) {
            let empty_star = document.createElement("span");
            empty_star.setAttribute("class", "glyphicon glyphicon-star-empty");
            star_div.appendChild(empty_star);
            total_rating -= 1;
            console.log("here 3")
        }
}

function closeErrorDiv() {
    background = document.getElementById("error_background")
    the_product_list_element = document.getElementById("error_div")
    the_product_list_element.style = "display:none"
    background.classList.remove("cover")
}

