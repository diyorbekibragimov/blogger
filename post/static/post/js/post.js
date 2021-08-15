const like_action = document.querySelector('.likes');
let liked = false

if (liked) {
    like_action.addEventListener('click', like_post());
} else {
    like_action.addEventListener('click', undo_like_post())
}

function undo_like_post() {
    const postId = document.querySelector(".likes").getAttribute('data-post-id');;
    const undoLikeUrl = "/" + postId +  "/undo_ike_post";
    const csrfToken = getCookie('csrftoken');

    fetch(undoLikeUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        }
    })
    .then(response => {
        return response.json();
    })
    .then(data => {
        if (data['liked'] == false) {
            const likeDiv = document.querySelector('.like');
            const i = likeDiv.getElementsByTagName('i')[0];
            i.classList.remove('bi-heart-fill');
            i.classList.add('bi-heart');
            window.liked = false
        }
    })
}
function like_post() {
    const postId = document.querySelector(".likes").getAttribute('data-post-id');;
    const likePostUrl = "/" + postId +  "/like_post";
    const csrfToken = getCookie('csrftoken');

    fetch(likePostUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        }
    })
    .then(response => {
        return response.json();
    })
    .then(data => {
        if (data['ok']) {
            const likeDiv = document.querySelector('.like');
            const i = likeDiv.getElementsByTagName('i')[0];
            i.style.backgroundColor = "red";
            window.liked = true;
        }
    })
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}