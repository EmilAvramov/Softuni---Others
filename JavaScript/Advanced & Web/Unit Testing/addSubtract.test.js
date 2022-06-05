describe("check calculator function functionality", () => {
    let calcObject;
    before(() => {
        calcObject = createCalculator();
    });
    describe("check type and properties", () => {
        it("type is object", () => {
            const expected = "object";

            assert.strictEqual(expected, typeof calcObject);
        });

        it("object has correct properties", () => {
            const expected = true;

            let actual;
            calcObject.add(6);
            calcObject.subtract(5);
            if (calcObject.get() === 1) {
                actual = true;
            } else {
                actual = false;
            }

            assert.strictEqual(expected, actual);

            //Teardown
            calcObject.subtract(1);
        });
    });

    describe("methods are working as intended", () => {
        it("add method is working as intended", () => {
            const expected = 5;

            calcObject.add(5);
            const actual = calcObject.get();

            assert.strictEqual(expected, actual);

            // Teardown
            calcObject.subtract(5);
        });

        it("add method returns a number", () => {
            const expected = "number";

            calcObject.add(5);
            const actual = typeof calcObject.get();

            assert.strictEqual(expected, actual);

            // Teardown
            calcObject.subtract(5);
        });

        it("subtract method is working as intended", () => {
            const expected = -5;

            calcObject.subtract(5);
            const actual = calcObject.get();

            assert.strictEqual(expected, actual);

            //Teardown
            calcObject.add(5);
        });

        it("subtract method returns a number", () => {
            const expected = "number";
            calcObject.subtract(5);
            const actual = typeof calcObject.get();

            assert.strictEqual(expected, actual);

            // Teardown
            calcObject.add(5);
        });
    });
    describe("object internal sum cannot be modified", () => {
        it("direct modificiation unsuccessful", () => {
            const expected = 0;

            calcObject.value += 5;
            const actual = calcObject.get();

            assert.strictEqual(expected, actual);
        });
    });
    describe("parameters can be parsed into numbers", () => {
        it("add method number can be parsed", () => {
            const expected = 5;

            calcObject.add("5");
            const actual = calcObject.get();

            assert.strictEqual(expected, actual);

            // Teardown
            calcObject.subtract(5);
        });
        it("subtract method number can be parsed", () => {
            const expected = -5;

            calcObject.subtract("5");
            const actual = calcObject.get();

            assert.strictEqual(expected, actual);

            // Teardown
            calcObject.add(5);
        });
    });
});
