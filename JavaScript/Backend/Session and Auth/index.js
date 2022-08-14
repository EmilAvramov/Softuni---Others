const express = require('express');
const cookieParser = require('cookie-parser');
const bcrypt = require('bcrypt')

const app = express();
const saltRounds = 10;
const hashedPassword = '$2b$10$GZfRNnkaL6rTSMd0rXV60eSwAq9o..N.Pz0VXJWAyA0IawodLWqV6'

app.use(cookieParser());

app.get('/', (req, res) => {
	res.send('Hello World');
});

app.get('/hash/:password?', async (req, res) => {
    const salt = await bcrypt.genSalt(saltRounds)
    const hash = await bcrypt.hash(req.params.password, salt);

    console.log('salt: ', salt)
    console.log('hash:', hash)
    res.send('Authenticated')
})

app.get('/login/:password', async (req, res) => {
    const matched = await bcrypt.compare(req.params.password, hashedPassword)
	if (matched) {
        res.send('Welcome')
    } else {
        res.send('Not Welcome')
    }
});

app.listen(5000, () => console.log('Server listening in port 5000...'));