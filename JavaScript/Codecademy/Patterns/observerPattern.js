class Account {
    constructor() {
        this.followers = [];
        this.feed = [];
    }
    addToFollowers(follower) {
        this.followers.push(follower);
    }
    removeFromFollowers(follower) {
        this.followers.splice(this.followers.indexOf(follower, 1));
    }
    publish(post) {
        this.followers.forEach((follower) => follower.update(post));
    }
    update(post) {
        this.feed.push(post);
    }
}

let a = new Account();
let b = new Account();
let c = new Account();

a.addToFollowers(b);
a.addToFollowers(c);

a.publish("Hello, world");

console.log(a);
/* Output shows b and c objects listed in a's followers array:
[
  Account { followers: [], feed: [ 'Hello, world' ] },
  Account { followers: [], feed: [ 'Hello, world' ] }
] 
*/

console.log(b);
// Account { followers: [], feed: [ 'Hello, world' ] }
