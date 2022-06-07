class Contact {
    constructor(firstName, lastName, phone, email) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.phone = phone;
        this.email = email;
        this._online = false;
    }

    eFactory(tag, content = '') {
        const e = document.createElement(tag)
        e.innerHTML = content
        return e
    }

    render(target) {
        this.article = this.eFactory("article");
        this.divTitle = this.eFactory("div", `${this.firstName} ${this.lastName}`);
        this.divTitle.className = this.online ? "title online" : "title"
        this.btn = this.eFactory("button", '&#8505;');
        this.divInfo = this.eFactory("div", `<span>&phone; ${this.phone}</span><span>&#9993; ${this.email}</span>`);
        this.divInfo.className = "info"
        this.divInfo.style.display = "none"
        this.divTitle.appendChild(this.btn)
        this.article.appendChild(this.divTitle)
        this.article.appendChild(this.divInfo)
        document.getElementById(target).appendChild(this.article)
        this.btn.addEventListener("click", () => {
            this.divInfo.style.display = this.divInfo.style.display === "none" ? "block" : "none"
        })
    }

    get online() {
        return this._online;
    }

    set online(input) {
        this._online = input
        if (this.divTitle) {
            this.divTitle.className = this._online? "title online" : "title"
        }
    }
}

let buttons = document.getElementsByTagName("div");

let contacts = [
    new Contact("Ivan", "Ivanov", "0888 123 456", "i.ivanov@gmail.com"),
    new Contact("Maria", "Petrova", "0899 987 654", "mar4eto@abv.bg"),
    new Contact("Jordan", "Kirov", "0988 456 789", "jordk@gmail.com"),
];
contacts.forEach((c) => c.render("main"));

setTimeout(() => (contacts[1].online = true), 2000);
