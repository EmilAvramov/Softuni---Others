function filterEmployees(data, criteria) {
    let pData = JSON.parse(data),
        newArray = [],
        parameter,
        value;

    pData.forEach((employee) => {
        if (criteria === "all") {
            newArray.push(toPrint(newArray.length, employee));
        } else {
            parameter = criteria.split("-")[0];
            value = criteria.split("-")[1];
            if (employee[parameter] === value) {
                newArray.push(toPrint(newArray.length, employee));
            }
        }
    });

    function toPrint(index, obj) {
        return `${index}. ${obj.first_name} ${obj.last_name} - ${obj.email}`;
    }

    console.log(newArray.join("\n"));
}

filterEmployees(
    `[{
    "id": "1",
    "first_name": "Ardine",
    "last_name": "Bassam",
    "email": "abassam0@cnn.com",
    "gender": "Female"
  }, {
    "id": "2",
    "first_name": "Kizzee",
    "last_name": "Jost",
    "email": "kjost1@forbes.com",
    "gender": "Female"
  },  
{
    "id": "3",
    "first_name": "Evanne",
    "last_name": "Maldin",
    "email": "emaldin2@hostgator.com",
    "gender": "Male"
  }]`,
    "id-2"
);

filterEmployees(
    `[{
    "id": "1",
    "first_name": "Kaylee",
    "last_name": "Johnson",
    "email": "k0@cnn.com",
    "gender": "Female"
  }, {
    "id": "2",
    "first_name": "Kizzee",
    "last_name": "Johnson",
    "email": "kjost1@forbes.com",
    "gender": "Female"
  }, {
    "id": "3",
    "first_name": "Evanne",
    "last_name": "Maldin",
    "email": "emaldin2@hostgator.com",
    "gender": "Male"
  }, {
    "id": "4",
    "first_name": "Evanne",
    "last_name": "Johnson",
    "email": "ev2@hostgator.com",
    "gender": "Male"
  }]`,
    "last_name-Johnson"
);
