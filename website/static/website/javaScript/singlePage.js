const page = path.split("/").pop();

let counter = 0;

let quantity = 20;

if(page === "index") {
    quantity = 5;
}

document.addEventListener('DOMContentLoaded', load);

function add_post_Page(contents) {
                const post = document.createElement('ul');
                post.className = 'post';

                const letra = document.createElement('a');
                letra.href = "#";
                letra.onclick = function () {
                   showNews(contents);
                };

                const tipoletra = document.createElement('h1');
                tipoletra.innerHTML = contents['title'];

                const frase = document.createElement('p');
                frase.innerHTML = "Actor: " + contents['Actor'];

                letra.append(h1);
                letra.append(p);
                letra.append(image);
                post.append(a);

                // Add post to DOM
                document.querySelector('#agenciaViagem').append(post);
            };

//pedir set de posts
function load() {

    const inicio = counter
    const fim = inicio + quantity - 1;
    counter = fim + 1;

    fetch(`/setions?start=${inicio}&end=${fim}`)
    .then(response => response.json())
    .then(data => {
        data.seccoes.forEach(add_post);
    });
};

function add_post(contents) {
   document.getElementById(contents).style.display = "block";
};