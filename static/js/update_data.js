// const url_endpoint = 'http://127.0.0.1:5000/api'
const url_endpoint = 'https://news-api-axtr.onrender.com/api/'

function getData() {


    $.ajax({
        url: url_endpoint,
        type: 'GET',
        beforeSend: () => {
            $('.news-list').empty();
            $('.news-list').append('loading');

        },
        success: (data) => {
            console.log(data)
            $('.news-list').empty();
            const headlines = data['headlines']
            for (const item in headlines) {
                console.log(headlines[item])
                headlines[item].forEach(news => {

                    $('.news-list').append(`<div class="card">
                <img src="${news.image_url}" alt="" class="card-image">
                <div class="card-content">

            <div class="card-title">
            
            <p> ${news.title}</p>
            <a target="_blank" href="${news.link}" class="more">Voir plus</a>

            </div>
                <div class="card-subtitle">
                <div class="date"> <i class="fa fa-calendar"></i> ${news.date}</div>
                <div class="source"> <i class="fa fa-newspaper-o"></i>${item}</div>
                </div>
                </div>
                </div>`);
                });
            }
        }
    })

}
getData();
// fetch('http://127.0.0.1:5000/api/').then((response)=>{
//     response.json()
// }).then((json) => {
//     console.log(json)
// })

$(document).ready(() => {

})