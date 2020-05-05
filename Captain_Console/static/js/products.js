$(document).ready(function() {
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        console.log(searchText)
        $.ajax({
            url: '/products?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {

                var newHtml = resp.data.map(d => {
                    return `<div class="well product">
                            <a href="/products$(d.id)">
                                <h4>$(d.name)</h4>
                                <p>$(d.description)</p>
                            </a>
                        </div>`
                });
                $('.products').html(newHtml.join(''));
                $('#search-box').val('');

                console.log('success')
                console.log(resp.data)
                return newHtml
            },
            error: function(xhr, status, error) {
                console.log('error')
                console.error(error)
            }
        })
    })
})