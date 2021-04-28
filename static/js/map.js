function showMap(cityName) {

    try {

        const path = new Request(`http://localhost:3000/getSvg/${cityName}`);
        const viewBox = new Request(`http://localhost:3000/getViewBox/${cityName}`);

        fetch(viewBox)
            .then(response => {
                return response.json();
            })
            .then(response => {
                document.getElementById('viewbox').setAttribute('viewBox', response[0].getviewbox);
            })
        fetch(path)
            .then(response => {
                return response.json();
            })
            .then(response => {
                document.getElementById('path').setAttribute('d', response[0].st_assvg)
            })

    }
    catch(error){
        window.alert(error)
    }

}