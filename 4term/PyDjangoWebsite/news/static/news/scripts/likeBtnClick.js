const btns = document.querySelectorAll(".like-btn");
var csrftoken = Cookies.get('csrftoken');

const url = 'http://localhost:8000/api/v1/top_headlines/';
const arr = [...btns];
arr.map((el, ind) => {

    el.addEventListener("click", (e) => {
        e.preventDefault();
        let id = el.dataset.buttonId.toString();
        const responseField = document.querySelector("#total_likes" + id);
        const likeHeart = document.querySelector("#like-heart" + id);
        let endpoint = url + id;
        endpoint = endpoint + '/like/';
        fetch(endpoint, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            }
        }).then(response => {
            if (response.ok) {
                return response.json()
            }
            throw new Error('POST request failed');
        }).then(jsonResponse => {
            console.log(jsonResponse["is_fan"], "here all is ok ");
            console.log(responseField, 'name of responseField');
            let is_fan = jsonResponse["is_fan"];
            if (is_fan) {
                likeHeart.style = " color: #cc4b37";
            } else {
                likeHeart.style = " color: #8a8a8a";
            }
            responseField.innerHTML = `${jsonResponse["total_likes"]}`;

        }, networkError => console.log(networkError.message))
    })
});