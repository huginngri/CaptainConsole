$(document).ready(function() {
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        var url = '/products?search_filter=' + searchText
        $.ajax({
            url: '/products?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                console.log(resp)
                console.log(resp.data)
                var id = resp.data[0].id
                console.log(id)
                window.location = '/products/'+id
                var newHtml = resp.data.map(d => {
                    return `<div class="well product">
                            <a href="/products/$(d.id)">
                            <img class="product-img" src="${d.image}"/>
                            <h4>{{ product.name }}</h4>
                            <p>{{ product.description }}</p>
                            <p>{{ product.manufacturer }}</p>
                            <p>{{ product.console_type }}</p>
                            <p>{{ product.price }} $</p>
                            <p>{{ product.rating }}</p>
                            </a>
                        </div>`
                });

                $('.products').html(newHtml.join(''));
                $('#search-box').val('');
                return newHtml
            },

            error: function(xhr, status, error) {
                console.log('error')
                console.error(error)
            }
        })
    })
})