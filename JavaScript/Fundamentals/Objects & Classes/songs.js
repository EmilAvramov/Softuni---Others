function songs(arr = []) {
    const count = arr.shift();
    const typeList = arr.pop();
    var songs = [];
    class Song {
        constructor(typeList, name, time) {
            this.typeList = typeList;
            this.name = name;
            this.time = time;
        }
    }
    arr.forEach((song) => {
        let temp = song.split("_");
        songs.push(new Song(temp[0], temp[1], temp[2]));
    });

    songs.forEach((song) => {
        if (typeList === "all") {
            console.log(song.name);
        } else if (song.typeList === typeList) {
            console.log(song.name);
        }
    });
}

songs([
    3,
    "favourite_DownTown_3:14",
    "favourite_Kiss_4:16",
    "favourite_Smooth Criminal_4:01",
    "favourite",
]);
