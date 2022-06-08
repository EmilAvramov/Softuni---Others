function solution() {
    class Balloon {
        constructor(color, weight) {
            this.color = color;
            this.hasWeight = weight;
        }
    }

    class PartyBalloon extends Balloon {
        constructor(color, weight, ribbon, length) {
            super(color, weight)
            this._ribbon = {color:ribbon, length: length}
        }

        get ribbon() {
            return this._ribbon
        }
    }

    class BirthdayBalloon extends PartyBalloon {
        constructor(text) {
            super(color, weight, ribbon, length)
            this._text = text;
        }

        get text() {
            return this._text;
        }
    }

    return {
        Balloon: Balloon,
        PartyBalloon: PartyBalloon,
        BirthdayBalloon: BirthdayBalloon
    }
}

let classes = solution();
let testBalloon = new classes.Balloon("yellow", 20.5);
let testPartyBalloon = new classes.PartyBalloon("yellow", 20.5, "red", 10.25);
let ribbon = testPartyBalloon.ribbon;
console.log(testBalloon);
console.log(testPartyBalloon);
console.log(ribbon);
