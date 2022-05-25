function path(string = "") {
    let toCheck = string.split("\\").pop();
    if (toCheck.split(".").length === 2) {
        console.log(`File name: ${toCheck.split(".")[0]}`);
        console.log(`File extension: ${toCheck.split(".")[1]}`);
    } else {
        console.log(
            `File name: ${toCheck.split(".")[0] + "." + toCheck.split(".")[1]}`
        );
        console.log(`File extension: ${toCheck.split(".")[2]}`);
    }
}

path("C:\\Internal\\training-internal\\Template.pptx");
path("C:\\Projects\\Data-Structures\\LinkedList.cs.cs");
