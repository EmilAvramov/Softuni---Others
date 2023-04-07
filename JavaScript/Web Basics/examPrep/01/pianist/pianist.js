function pianist(args) {
    function checkPiece(array, item) {
        return array.hasOwnProperty(item)
    }

    let piece, pieces, composer, key, newKey, tokens, command
    const collection = {}

    pieces = Number(args.shift())
    args.pop()
    
    for (let i = 0; i < pieces; i++) {
        tokens = args[i].split("|")
        piece = tokens[0]
        composer = tokens[1]
        key = tokens[2]
        collection[piece] = [composer, key]
    }

    args.forEach(element => {
        tokens = element.split("|")
        command = tokens[0]
        piece = tokens[1]

        if (command === "Add") {
            composer = tokens[2]
            key = tokens[3]
            if (checkPiece(collection, piece)) {
                console.log(`${piece} is already in the collection!`)
            } else {
                collection[piece] = [composer, key]
                console.log(`${piece} by ${composer} in ${key} added to the collection!`)
            }
        } else if (command === "Remove") {
            if (checkPiece(collection, piece)) {
                delete collection[piece]
                console.log(`Successfully removed ${piece}!`)
            } else {
                console.log(`Invalid operation! ${piece} does not exist in the collection.`)
            }
        } else if (command === "ChangeKey") {
            newKey = tokens[2]
            if (checkPiece(collection, piece)) {
                collection[piece].pop()
                collection[piece].push(newKey)
                console.log(`Changed the key of ${piece} to ${newKey}!`)
            } else {
                console.log(`Invalid operation! ${piece} does not exist in the collection.`)
            }
        }
    });

    for (const property in collection) {
        console.log(`${property} -> Composer: ${collection[property][0]}, Key: ${collection[property][1]}`)
    }
    
}

pianist([
    '3',
    'Fur Elise|Beethoven|A Minor',
    'Moonlight Sonata|Beethoven|C# Minor',
    'Clair de Lune|Debussy|C# Minor',
    'Add|Sonata No.2|Chopin|B Minor',
    'Add|Hungarian Rhapsody No.2|Liszt|C# Minor',
    'Add|Fur Elise|Beethoven|C# Minor',
    'Remove|Clair de Lune',
    'ChangeKey|Moonlight Sonata|C# Major',
    'Stop'  
  ])