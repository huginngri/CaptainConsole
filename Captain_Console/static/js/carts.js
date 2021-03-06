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
    /*
    this function sends a post request to the server requesting
    to add the provided product to the cart of the user that called the function
     */
    $.ajax({
        type: "POST",
        method: 'POST',
        url: '/carts/',
        data: {
            product_id: product
        },
        success: function (response) {
            if (response.count === undefined) {
                window.location = '/carts/view';
            }
            else {
                /*
                the amount in the cart is changed if the request was successful
                 */
                let cart_number = document.getElementById("cart_count");
                cart_number.textContent = response.count;
            }
        },
        error: function (xhr, status, error) {
            console.log('error')
        }
    });
}

function calculate_cart() {
    /*
    this function sends a get request to the server requesting
    th ecount of the items in the cart of the user that called the function
     */
    $.ajax({
        type: "GET",
        url: '/carts',
        success: function (response) {
            /*
            if the request is successful, the count is displayed
             */
            let cart_number = document.getElementById("cart_count");
            cart_number.textContent = response.count;
        },
        error: function (xhr, status, error) {
            console.log('Request failed')
        }
    });
}

function place_order(order) {
    /*
    this function is used to confirm an order of a user, the order is provided as a
    parameter and sent to the server in the request
     */
    $.ajax({
        type: "POST",
        method: 'POST',
        url: '/orders/checkout/overview',
        data: {
            order: order
        },
        success: function (response) {
            console.log('sucess')
            if (response['message'] == 'out of stock'){
                /*
                if some product is out of stock, the corresponding message is displayed
                 */
                let header = document.getElementById('order_header')
                header.textContent = 'Order denied.\nItem: "' + response['product'] + '" out of stock, only ' + response['items_left'] + ' items left.'
                header.setAttribute('class', 'alert alert-danger')
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
            }
            else {
                /*
                if the order was successfully confirmed, a confirmation message is displayed
                 */
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
            }
        },
        error: function (xhr, status, error) {
            console.log('error')
        }
    });
}


function remove_from_cart(product_id, child) {
    /*
    this function sends a request to the server to remove a provided product
    from the users cart
     */
    let deletediv = child.parentNode
    $.ajax({
        type: "DELETE",
        method: 'DELETE',
        url: '/carts/' + product_id,
        success: function (response) {
            /*
            if the cart is now empty, the page is reloaded to display the correct message
             */
            if (response['total_price'] === 0) {
                location.reload()
            }
            else {
                /*
                if the  product is successfully removed from the cart, the div containing the product
                is removed from the DOM and the new total price and cart count are displayed
                 */
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
            console.log('error');

        }
    });
}


function change_quantity(product_id) {
    /*
    this function sends a POSt request to a server requesting to
    change the quantity of some product in the users  cart.
     */
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
            /*
            if the request is successful the new total price and cart count are displayed
             */
            let price = document.getElementById('cart_total');
            let total = parseFloat(response['total_price']);
            price.textContent = 'Total price: ' + total + '$';

            calculate_cart()
        },
        error: function (xhr, status, error) {
            console.log('error');
        }
    });
}

/*
* This is the order by or sort by. It takes the select element as a parameter. Then it finds the container for the
* products. 2 arrays are initialized and 3 other variables. name_or_price is in what order the products should be,
* n_o_p is to store that as an integer 1 or 2 and that relates to the div it is in. r is just to say if it is in reversed or not.
* Then a reverse check is done and localeCompare returns 0 if it is a match.
*
* */
function sortit(sel) {
    let all_products = document.getElementById("container_for_products")
    let the_arr = []
    let keep_arr =[]
    let name_or_price = sel.options[sel.selectedIndex].value
    let n_o_p = 1
    let r = 0
    let reverse_check = name_or_price.localeCompare("name_reverse") * name_or_price.localeCompare("price_reverse")
    if (reverse_check === 0){
        r = 1
    }
    let k = name_or_price.localeCompare("price") * name_or_price.localeCompare("price_reverse")
    if (k === 0) {
        n_o_p = 2
    }
    /*
    * Loop through all children in all products and push it to keep_arr.
    * Then i either add the price or name to the_arr and make sure it is float or uppercase and that is for the sorting */
    for (let x = 0; x<all_products.children.length; x++){
        keep_arr.push(all_products.children[x])
        let j = all_products.children[x].children[0].children[1].children[0].children[n_o_p].getAttribute("name")
        if (n_o_p ===2){
            the_arr.push(parseFloat(j))
        }
        else {
            the_arr.push(j.toUpperCase())
        }
    }
    let new_arr = []
    /*
    * I create a copy of the the_arr and sort it and if it should be reversed i reverse it */
    for (let x = 0; x<the_arr.length; x++){
        new_arr.push(the_arr[x])
    }
    if (n_o_p === 2) {
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
    /*
    * Remove all child from the product container */
    let order_arr = []
    while (all_products.firstChild){
        all_products.removeChild(all_products.lastChild)
    }
    /*
    * since the_arr and new_arr have the same values but at different location
    * order arr gets the index of the div that should come first in the keep_arr
    * and so on and the append the div to the product container*/
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
    background = document.getElementById("background_"+orderNumber);
    the_product_list_element = document.getElementById("list_for_"+orderNumber);

    the_product_list_element.classList.add("popupsmall","absolute","ccwhite");
    background.classList.add("cover");
}

//this function closes a window that pops up when user has done somthingwrong.
function closeDiv(orderNumber) {
    background = document.getElementById("background_" + orderNumber);
    the_product_list_element = document.getElementById("list_for_" + orderNumber);
    the_product_list_element.classList.remove("popupsmall", "absolute", "ccwhite");
    background.classList.remove("cover");
}

//this function calculates how many full and empty star should be displayed.
function calculateRating(id, rating) {
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
        }


}
//this function calculates how many full and empty star should be displayed but takes in the item that the star should be placed into as an argument.
function calculateRatingHome(star_div, rating, count) {
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
        }
        let text = document.createElement("p");
        text.setAttribute("class", "inline ccbluesmall");
        text.setAttribute("id", "padding-xsmall");
        text.textContent ="  " + count
        star_div.appendChild(text);
}

//this function closes a window that pops up when user has done some error..
function closeErrorDiv() {

    let background = document.getElementById("error_background")
    let the_product_list_element = document.getElementById("error_div")
    the_product_list_element.style = "display:none"
    background.classList.remove("cover")

}

function display_checkout(todisplay, toclose){
    itemtodisplay1 = document.getElementById(todisplay+"1");
    itemtodisplay2 = document.getElementById(todisplay+"2");
    itemtoclose1 = document.getElementById(toclose+"1");
    itemtoclose2 = document.getElementById(toclose+"2");
    itemtodisplay1.classList.remove("display-none");
    itemtodisplay2.classList.remove("display-none");
    itemtoclose1.classList.add("class", "display-none" );
    itemtoclose2.classList.add("class", "display-none" );


}
