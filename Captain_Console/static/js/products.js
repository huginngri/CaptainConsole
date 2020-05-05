$(document).ready(function() {
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax({
            url: '/products' + searchText,
            type: 'GET',
            success: function(resp) {
                console.log('success')
            },
            error: function(xhr, status, error) {
                console.error(error)
            }
        })
    })
})