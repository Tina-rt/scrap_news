$('.news-list').on('click','.news-item', (e) => {
    alert($(e.target).attr('link'))
})