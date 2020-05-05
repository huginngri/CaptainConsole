$(document).ready(function() {
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        console.log(searchText)
        $.ajax({
            url: '/products?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data
                console.log('success')
                console.log(searchText)
            },
            error: function(xhr, status, error) {
                console.log('error')
                console.error(error)
            }
        })
    })
})