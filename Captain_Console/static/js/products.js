$(document).ready(function() {
    $('#search-bt').on('click', function(e) {
    console.log("in products")
    $('#search-bt').on('click', function (e) {
        e.preventDefault();
        var searchText = $('#search').val();
        $.ajax({
            url: '/products?search_filter=' + searchText,
            type: 'GET',
            success: function (resp) {
                var newHtml = resp.data.map(d => {
                    return `
                                <div class="product_boxes box ccwhite">
                                        <a href="/products/${d.id}"></a>
                                        <img class = "mediumimages" src="${d.image}" style="height:150px;">
                                    
                                    <div class="button_and_text">
                                        <div class="info">
                                            <h4 class="name">${d.name}</h4>
                                            <p class="price">${d.price} $</p>
                                        </div>
                                        <div class="btn-group buy-button" role="group" aria-label="...">
                            
                                              <button type="button" class="buy-btn">Buy</button>
                                              <button type="button" class="cart-btn ccorange" onclick="add_to_cart_js(${d.id})">  <span class="glyphicon glyphicon-shopping-cart" aria-hidden="true"></span></button>
    
                                        </div>
                                    </div>
                                </div>
                            `
                });
                newHtml[0] = `<div class=product_container>` + newHtml[0]
                newHtml[-1] += `</div>`
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
    console.log("flott")

});

$("#recent-views").ready(function () {
        console.log("hello")
        $.ajax({
            url: "/products/recent",
            type: "GET",
            success: function (response) {
                var recentproducts = response.data.map(d => {
                    return `
                                    <div class=" product_boxes box ccwhite">
                                        <a href="/products/${d.id}"></a>
                                        <img class = "mediumimages" src="${d.image}" style="height:150px;">
                                    
                                    <div class="button_and_text">
                                        <div class="info">
                                            <h4 class="name">${d.name}</h4>
                                            <p class="price">${d.price} $</p>
                                        </div>
                                    </div>
                                </div>
                            `
                })
                $("#recent-views").html(recentproducts.join(""))
            },
            error: function (xhr, status, error) {
                console.log('error')
                console.error(error)
            }
        })

    })
})

