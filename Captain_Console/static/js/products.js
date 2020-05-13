$(document).ready(function() {
    $('#search-bt').on('click', function (e) {
        e.preventDefault();
        var searchText = $('#search').val();
        $.ajax({
            url: '/products?search_filter=' + searchText,
            type: 'GET',
            success: function (resp) {

                if (resp.data.length == 0) {
                    console.log("in this if statement")
                    window.location.replace("http://127.0.0.1:8000/products/search_no_response");
                }

                let newHtml = resp.data.map(d => {
                    return `
                                <a class=" product_boxes box ccwhite" href="/products/${d.id}">
                                        <img class = "mediumimages" src="${d.image}" style="height:150px;">
                                    <div class="button_and_text">
                                        <div class="info">
                                            <h4 class="name" name="${d.name}">${d.name}</h4>
                                            <p class="price" name="${d.price}">${d.price} $</p>
                                        </div>
                                        <div class="btn-group buy-button" role="group" aria-label="...">
                                              <button type="button" class="buy-btn">Buy</button>
                                              <button type="button" class="cart-btn ccorange" onclick="add_to_cart_js(${d.id})">  <span class="glyphicon glyphicon-shopping-cart" aria-hidden="true"></span></button>
                                        </div>
                                    </div>
                                </a>
                            `
                });
                newHtml[0] = `<select  id="sort" onchange="sortit(this)">
            <option value="name">name (ascending)</option>
            <option value="name_reverse">name (descending)</option>
            <option value="price">price (ascending)</option>
            <option value="price_reverse">price (descending)</option>
        </select><div class=product_container id="container_for_products">` + newHtml[0]
                newHtml[-1] += `</div>`
                console.log("This is the newHtml")
                console.log(newHtml)
                $('main').html(newHtml.join(''));
                $('#search-box').val('');

            },

            error: function (xhr, status, error) {
                console.log('error')
                console.error(error)
            }
        })
    })


    $("#recent-views").ajax({
        url: "/products/recent",
        type: "GET",
        success: function (response) {
            var recentproducts = response.data.map(d => {
                return `
                                    <a class=" product_boxes box ccwhite" href="/products/${d.id}">
                                        <img class = "mediumimages" src="${d.image}" style="height:150px;">
                                    <div class="button_and_text">
                                        <div class="info">
                                            <h4 class="name" name="${d.name}">${d.name}</h4>
                                            <p class="price" >${d.price} $</p>
                                        </div>
                                    </div>
                                </a>
                            `
            })
            recentproducts[0] = `<div class=product_container>` + recentproducts[0]
            recentproducts[-1] += `</div>`
            console.log(recentproducts)
            $("#recent-views").html(recentproducts.join(""))
        },
        error: function (xhr, status, error) {
            console.log('error')
            console.error(error)
        }
    })
    // if ($("#star*")) {
    //     $("#star*").ready(function () {
    //         console.log("what");
    //         star_div = document.getElementById("star_" + orderNumber);
    //         let star = document.createElement("span");
    //         star.setAttribute("class", "glyphicon glyphicon-star");
    //         let empty_star = document.createElement("span");
    //         empty_star.setAttribute("class", "glyphicon glyphicon-star-empty");
    //         // <span class="glyphicon glyphicon-shopping-cart" aria-hidden="true"></span>
    //         let total_rating = 5;
    //         while (rating > 0) {
    //             star_div.appendChild(star);
    //             total_rating -= 1;
    //             rating -= 1;
    //         }
    //         while (total_rating > 0) {
    //             star_div.appendChild(empty_star);
    //             total_rating -= 1;
    //
    //         }
    //     })
    // }
})


