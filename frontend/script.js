let liczba1;
let dzialanie;
let liczba2;
let czyWyswietlonoWynik = false;

function wpiszLiczbe(liczba) {
    let ekran = document.getElementById('ekran');

    if (czyWyswietlonoWynik) {
        ekran.value = "";
        czyWyswietlonoWynik = false;
    }

    ekran.value += liczba;
}


function wybierzDzialanie(operator) {
let ekran = document.getElementById("ekran");

liczba1 = ekran.value;
dzialanie = operator;

ekran.value = "";
}





async function oblicz() {
    if (liczba1 === undefined || dzialanie === undefined) {
        return;
    }

    let ekran = document.getElementById('ekran')

    let liczba2 = ekran.value

    let obliczenie = {
        liczba1: liczba1,
        dzialanie: dzialanie,
        liczba2: liczba2
    }

    let odpowiedz = await fetch("/oblicz", {method: "POST", headers: {"Content-Type": "application/json"},body: JSON.stringify(obliczenie)});
    
    let dane = await odpowiedz.json();
    console.log(dane);
    if (odpowiedz.ok) {
        ekran.value = dane.wynik

        liczba1 = undefined;
        dzialanie = undefined;
        czyWyswietlonoWynik = true;

        await pobierzHistorie();
    } else {
        ekran.value = dane.detail
    }

}

function wpiszKropke() {
    let ekran = document.getElementById('ekran')
    if (!ekran.value.includes('.')) {
        ekran.value += '.'
    }

}




function wyczysc() {
let ekran = document.getElementById("ekran");

ekran.value = "";
liczba1 = undefined;
dzialanie = undefined;
czyWyswietlonoWynik = false;
}


document.addEventListener('keydown', function(event) {
if ('0123456789'.includes(event.key)) {
    wpiszLiczbe(event.key)
} else if ('c' === event.key || 'C' === event.key) {
    wyczysc()
} else if ('^%//*+-'.includes(event.key)) {
    wybierzDzialanie(event.key)
} else if ('Enter' === event.key) {
    oblicz()
} else if ('.' === event.key) {
    wpiszKropke()
}
});

let przyciskiLiczb = document.querySelectorAll('[data-number]');

przyciskiLiczb.forEach(function(przycisk) {

przycisk.addEventListener('click', function() {

wpiszLiczbe(przycisk.dataset.number);

});

})  

let przyciskiOperatorow = document.querySelectorAll('[data-operator]');

przyciskiOperatorow.forEach(function(przycisk) {
    przycisk.addEventListener('click', function() {
        if ('^%//*+-'.includes(przycisk.dataset.operator)) {
            wybierzDzialanie(przycisk.dataset.operator)
        }   else if (przycisk.dataset.operator === '=') {
            oblicz()
        }   else if (przycisk.dataset.operator === 'C') {
            wyczysc()
        }   else if (przycisk.dataset.operator === '.') {
            wpiszKropke()
        }    
    })
})

async function pobierzHistorie() {
    let odpowiedz = await fetch("/historia");
    let historia = await odpowiedz.json();

    let listaHistorii = document.getElementById("history-list");

    listaHistorii.innerHTML = "";

    if (historia.length === 0) {
        listaHistorii.innerHTML = `
            <p class="empty-history">Brak obliczeń</p>
        `;

        return;
    }

    historia.forEach(function(obliczenie) {
        let element = document.createElement("div");

        element.classList.add("history-item");

        element.innerHTML = `
            <span class="history-calculation">
                ${obliczenie.liczba1}
                ${obliczenie.dzialanie}
                ${obliczenie.liczba2}
                =
                ${obliczenie.wynik}
            </span>

            <span class="history-date">
                ${obliczenie.utworzono}
            </span>
        `;

        listaHistorii.appendChild(element);
    });
}


let przyciskCzyszczeniaHistorii =
    document.getElementById("clear-history");

przyciskCzyszczeniaHistorii.addEventListener(
    "click",
    wyczyscHistorie()
);

async function wyczyscHistorie() {
    let czyUsunac = confirm(
        "Czy na pewno chcesz wyczyscic cala historie?"
    );

    if (!czyUsunac) {
        return;
    }

    let odpowiedz = await fetch("/historia", {
        method: "DELETE"
    });

    if (odpowiedz.ok) {
        await pobierzHistorie();
    }
}