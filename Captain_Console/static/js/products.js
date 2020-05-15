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
                    if (d.on_sale === true) {

                        x= `
                            <div class=" product_boxes box ccwhite">
                                <a class=" product_boxes_inside box_inside" href="/products/${d.id}">
                                    <div class="containerimage">
                                        <img class = "mediumimages" src="${d.image}" style="height:150px;" onload="calculateRatingHome(this.parentNode.parentNode.children[1].children[0].children[0], ${d.rating}, ${d.review_count})">
                                    </div>
                                    <div class="button_and_text">
                                        <div class="info">
                                            <h4 class="cc2psmall no-margin rating no-margin" "></h4>
                                            <h4 class="name ccbluemedium center no-margin" " name="${d.name}">${d.name}</h4>
                                            <p class="price ccbluesmall center no-margin" " name="${d.discount_price}">${d.discount_price} $ (-${d.discount}%)</p>
                                        </div>
                                    </div>
                                </a>
                        `
                    } else {
                        x = `
                            <div class=" product_boxes box ccwhite">
                                <a class=" product_boxes_inside box_inside" href="/products/${d.id}">
                                         <div class="containerimage">
                                        <img class = "mediumimages" src="${d.image}" style="height:150px;" onload="calculateRatingHome(this.parentNode.parentNode.children[1].children[0].children[0], ${d.rating}, ${d.review_count})">
                                    </div>
                                    <div class="button_and_text">
                                        <div class="info">
                                            <h4 class="cc2psmall no-margin rating no-margin" "></h4>
                                            <h4 class="name ccbluemedium center no-margin" " name="${d.name}">${d.name}</h4>
                                            <p class="price ccbluesmall center no-margin" " name="${d.price}">${d.price} $</p>
                                        </div>
                                       
                                    </div>
                                </a>
                        `
                    }
                    if (d.stock > 0) {

                            return x +`<div class="below_box">
                                          <button type="button" class="product-btn buy ccbluemedium" onclick="buy_product(${d.id })">Buy</button>
                                          <button type="button" class="product-btn cart ccbluemedium" onclick="add_to_cart_js(${d.id })">  <span class="glyphicon glyphicon-shopping-cart" aria-hidden="true"></span></button>
                                    </div>
                                     </div>`
                        }
                        else {
                            return x +`
                        
                            <div class="out_of_stock">
                                        <p class = "ccbluemedium bold center">Out of stock</p>
                            </div>

                            </div>
                           
                            `
                        }
                })






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

if ($("#recent-views").length>0) {
        $("#recent-views").ready(function () {


        $.ajax({
            url: "/products/recent",
            type: "GET",
            success: function (response) {
                if (response.data.length > 0) {
                    var recentproducts = response.data.map(d => {
                        x =`
                                <a class=" product_boxes box ccwhite" href="/products/${d.id}">
                                    <img class = "mediumimages" src="${d.image}" style="height:150px;">
                                <div class="button_and_text">
                                    <div class="info">
                                        <h4 class="name" name="${d.name}">${d.name}</h4>
                                        `
                        if(d.on_sale === true) {
                            return x + `
                        
                                        <p class="price" >${d.discount_price} $ (-${d.discount}%)</p>

                                    </div>
                                    </div>
                                </a>`
                        }
                        else{
                            return x + `
                        
                                        <p class="price" >${d.price} $</p>

                                    </div>
                                    </div>
                                </a>`

                        }


                        })
                        recentproducts[0] = `<div class=product_container>` + recentproducts[0]
                        recentproducts[-1] += `</div>`
                        $("#recent-views").html(recentproducts.join(""))

                    }
                },
                error: function (xhr, status, error) {
                    console.log('error')
                    console.error(error)
                }
            })
        })
    }

    if ($("#give_review_button").length > 0) {
        $("#give_review_button").ready(function () {
        let review_button = document.getElementById('give_review_button');
        let product_id = review_button.name
        $.ajax({
            type: 'GET',
            method: 'GET',
            url: '/orders/can_review/'+ product_id,
            success: function (response) {
                console.log(response['can_review'])
                if (response['can_review'] == true){
                    review_button.style= 'display: inline-block';
                }
            },
            error: function (xhr, status, error) {
                console.log('eitthvað vilaust');
            }
        });
        })
    }
})







