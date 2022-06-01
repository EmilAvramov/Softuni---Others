function solution(command) {
    if (command === "upvote") return this.upvotes++;
    if (command === "downvote") return this.downvotes++;

    let up = this.upvotes;
    let down = this.downvotes;
    let total = up + down;
    let balance = up - down;

    function ratings() {
        if (total < 10) return "new";
        if (up > total * 0.66) return "hot";
        if (balance >= 0 && total > 100) return "controversial";
        if (balance < 0) return "unpopular";
        return "new";
    }

    if (total > 50) {
        let inflated = Math.ceil(Math.max(up, down) * 0.25);
        return [up + inflated, down + inflated, balance, ratings()];
    }

    return [up, down, balance, ratings.call(this)];
}

let post = {
    id: "3",
    author: "emil",
    content: "wazaaaaa",
    upvotes: 50,
    downvotes: 100,
};

solution.call(post, "upvote");
solution.call(post, "downvote");
let score = solution.call(post, "score"); // [127, 127, 0, 'controversial']
solution.call(post, "downvote"); // (executed 50 times)
score = solution.call(post, "score");
