const links = document.querySelectorAll(".watch-link");

const url1 = 'http://localhost:8000/api/v1/top_headlines/';
const a = [...links];
a.map((el, ind) => {

    el.addEventListener("mousedown", (e) => {
        e.preventDefault();
        let id = el.dataset.buttonId.toString();
        const respField = document.querySelector("#views" + id);
        let endpoint = url1 + id;
        endpoint = endpoint + '/watch/';
        fetch(endpoint).then(response => {
            if (response.ok) {
                return response.json()
            }
            throw new Error('GET request failed');
        }).then(jsonResponse => {
            console.log("here all is ok ");
            let num = jsonResponse["views"];
            if(num>=1000)
                respField.innerHTML = `${(num/1000).toFixed(1)}`+'k';
            else
                respField.innerHTML = `${num}`;
        }, networkError => console.log(networkError.message))
    })
});