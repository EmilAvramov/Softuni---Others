function hashTag(phrase) {
    let words = phrase.split(' ')
    var regExp = /[a-zA-Z]/g

    words.forEach(word => {
        if (word.startsWith('#') && regExp.test(word)) {
            let redacted = word.replace('#', '')
            console.log(redacted)
        }
    })
}

hashTag('Nowadays everyone uses # to tag a #special word in #socialMedia')
hashTag('The symbol # is known #variously in English-speaking #regions as the #number sign')