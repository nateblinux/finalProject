const cardContainer = $('#results').val();

function favoriteClick(id) {
    console.log(id);
    const csrftoken = Cookies.get('csrftoken');
    $.ajax({
        type: "POST",
        url: '/favorite/',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        mode: 'same-origin',
        data: {
            "id": id,
        },
        dataType: "json",
        success: function (data) {
            console.log("data sent");
            if (data.action === "delete") {
                $(`#${id}`).html(`
                     <path d="M2.866 14.85c-.078.444.36.791.746.593l4.39-2.256 4.389 2.256c.386.198.824-.149.746-.592l-.83-4.73 3.522-3.356c.33-.314.16-.888-.282-.95l-4.898-.696L8.465.792a.513.513 0 0 0-.927 0L5.354 5.12l-4.898.696c-.441.062-.612.636-.283.95l3.523 3.356-.83 4.73zm4.905-2.767-3.686 1.894.694-3.957a.565.565 0 0 0-.163-.505L1.71 6.745l4.052-.576a.525.525 0 0 0 .393-.288L8 2.223l1.847 3.658a.525.525 0 0 0 .393.288l4.052.575-2.906 2.77a.565.565 0 0 0-.163.506l.694 3.957-3.686-1.894a.503.503 0 0 0-.461 0z"/>
                `);
            } else {
                $(`#${id}`).html(`
                     <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                `);
            }
        }
    })
}

if (cardContainer === '') {
    $('body').css('margin-bottom', '10%');
} else {
    $('body').css('margin-bottom', '40%');
}


let hiddenValue = $('#hidden-value').text();
console.log(hiddenValue);
if (hiddenValue === 'music') {
    $('#navbar-icon').append('<i class=" icons fa-solid fa-headphones pe-3"></i>');
    $('body').css('background-image', 'linear-gradient(#6A5259, #D5BB9A)')
} else if (hiddenValue === 'dance') {
    $('#navbar-icon').append('<i class="icons fa-solid fa-person-falling pe-3"></i>');
    $('body').css('background-image', 'linear-gradient(#2B7591, #FEF9DD)')

} else {
    $('#navbar-icon').append('<i class="icons fa-solid fa-icons fa-xl pe-3"></i>');
}

$(window).scroll(function () {
    $('.icons').addClass('fa-bounce');
    setTimeout(function () {
        $('.icons').removeClass('fa-bounce');
    }, 2000);

})


//
//     function(event) {
//   const scrollTop = $(window).scrollTop();
//   const previousScrollTop = $(this).data('previousScrollTop');
//
//   if (scrollTop < previousScrollTop) {
//     console.log('Scrolling up');
//   } else if (scrollTop > previousScrollTop) {
//     console.log('Scrolling down');
//   }
//
//   $(this).data('previousScrollTop', scrollTop);
// });