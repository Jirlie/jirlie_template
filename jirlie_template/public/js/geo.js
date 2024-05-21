function getVisitorInfo() {
    if ('geolocation' in navigator) {
        navigator.geolocation.getCurrentPosition(function (position) {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;
            console.log(latitude, longitude)
            fetch(`https://nominatim.openstreetmap.org/reverse?lat=${latitude}&lon=${longitude}&format=json`)
                .then(function (response) {
                    return response.json();
                })
                .then(function (data) {
                    const country = data.address.country;
                    const countryCode = data.address.country_code;
                    console.log(country)
                    fetch(`https://countriesnow.space/api/v0.1/countries/currency`, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ country: country })
                    })
                        .then(function (response) {
                            return response.json();
                        })
                        .then(function (countryData) {
                            const currencyCode = countryData.data.currency;
                            

                            console.log(countryData)
                            console.log(currencyCode)
                            const currency = document.querySelectorAll("#currency");
                            currency.textContent = `GBP`;
                            currency.forEach(currency => {
                                currency.textContent = currencyCode;
                            });
                            const price1 = document.getElementById("price1")
                            const price2 = document.getElementById("price2")
                            const price3 = document.getElementById("price3")
                            const currency1 = document.getElementById("currency1")
                            const currency2 = document.getElementById("currency2")
                            let price4;
                            let price5;
                            
                            fetch(`https://neuocean.com/api/method/neu_ocean_template.api.pricing?currency=${currencyCode}`)
                            .then(response => response.json())
                            .then(r => {
                                price1.innerHTML = (price1.textContent * r.message[0].exchange_rate).toFixed(2);
                                        price2.innerHTML = (price2.textContent * r.message[0].exchange_rate).toFixed(2);
                                        price3.innerHTML = (price3.textContent * r.message[0].exchange_rate).toFixed(2);
                                        price4 = (15 * r.message[0].exchange_rate).toFixed(2);
                                        price5 = (5 * r.message[0].exchange_rate).toFixed(2);
                                        currency1.textContent = `For as low as ${currencyCode} ${price4} per user / month`;
                                        currency2.textContent = `For as low as ${currencyCode} ${price5} per hour`;
                            })
                            
                        })
                        .catch(function (error) {
                            console.error('Error fetching country information:', error);
                        });
                })
                .catch(function (error) {
                    console.error('Error fetching visitor country:', error);
                });
        });
    } else {
        alert('Geolocation is not supported by your browser.');
    }
}



// Call the function when the page loads
getVisitorInfo();

const shareButton = document.getElementById("answer-example-share-button");
shareButton.addEventListener("click", (e) => {
    if (navigator.share) {
        navigator.share({
            title: 'Neu Ocean Technologies | Employee Profile',
            text: 'Take a look at My Digital Card!',
            url: document.location.href,
        })
            .then(() => console.log('Successful share'))
            .catch((error) => console.log('Error sharing', error));
    } else {
        console.log('Share not supported on this browser.');
    }
});

