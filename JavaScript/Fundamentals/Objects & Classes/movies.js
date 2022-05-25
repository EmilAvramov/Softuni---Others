function movies(arr = []) {
    let movies = [],
        movie,
        title,
        director,
        date;
    for (let i = 0; i < arr.length; i++) {
        movie = arr[i].split(" ");
        if (arr[i].indexOf("addMovie") !== -1) {
            movie = movie
                .slice(movie.indexOf("addMovie") + 1, movie.length)
                .join(" ");
            movies.push({ name: movie });
        } else if (arr[i].indexOf("directedBy") !== -1) {
            title = movie.slice(0, movie.indexOf("directedBy")).join(" ");
            director = movie
                .slice(movie.indexOf("directedBy") + 1, movie.length)
                .join(" ");
            movies.forEach((movie) => {
                if (movie.name === title) {
                    movie["director"] = director;
                }
            });
        } else if (arr[i].indexOf("onDate") !== -1) {
            title = movie.slice(0, movie.indexOf("onDate")).join(" ");
            date = movie.slice(movie.indexOf("onDate") + 1, movie.length);
            movies.forEach((movie) => {
                if (movie.name === title) {
                    movie["date"] = date[0];
                }
            });
        }
    }
    movies.forEach((movie) => {
        if (
            movie.hasOwnProperty("name") &&
            movie.hasOwnProperty("director") &&
            movie.hasOwnProperty("date")
        ) {
            console.log(JSON.stringify(movie));
        }
    });
}

movies([
    "addMovie Fast and Furious",
    "addMovie Godfather",
    "Inception directedBy Christopher Nolan",
    "Godfather directedBy Francis Ford Coppola",
    "Godfather onDate 29.07.2018",
    "Fast and Furious onDate 30.07.2018",
    "Batman onDate 01.08.2018",
    "Fast and Furious directedBy Rob Cohen",
]);
