describe("test functionality of color function", () => {
    describe("check input parameter type validity", () => {
        let expected;
        before(() => {
            expected = undefined;
        });

        it("with strings on first param", () => {
            const actual = rgbToHexColor("red", 1, 2);

            assert.strictEqual(expected, actual);
        });
        it("with strings on second param", () => {
            const actual = rgbToHexColor(1, "green", 2);

            assert.strictEqual(expected, actual);
        });
        it("with strings on third param", () => {
            const actual = rgbToHexColor(1, 2, "blue");

            assert.strictEqual(expected, actual);
        });
    }),
        describe("check input parameter ranges", () => {
            let expected;
            before(() => {
                expected = undefined;
            });
            it("with out of bounds upper number for first param", () => {
                const actual = rgbToHexColor(300, 1, 2);
                assert.strictEqual(expected, actual);
            });
            it("with out of bounds upper number for second param", () => {
                const actual = rgbToHexColor(1, 300, 2);
                assert.strictEqual(expected, actual);
            });
            it("with out of bounds upper number for third param", () => {
                const actual = rgbToHexColor(2, 1, 300);
                assert.strictEqual(expected, actual);
            });
            it("with out of bounds lower number for first param", () => {
                const actual = rgbToHexColor(-300, 1, 2);
                assert.strictEqual(expected, actual);
            });
            it("with out of bounds lower number for second param", () => {
                const actual = rgbToHexColor(1, -300, 2);
                assert.strictEqual(expected, actual);
            });
            it("with out of bounds lower number for third param", () => {
                const actual = rgbToHexColor(2, 1, -300);
                assert.strictEqual(expected, actual);
            });
        }),
        describe("check if output is the correct hex", () => {
            it("check with 255, 255, 255", () => {
                const expected = "#FFFFFF";

                const actual = rgbToHexColor(255, 255, 255);

                assert.strictEqual(expected, actual);
            });
            it("check with 0, 0, 0", () => {
                const expected = "#000000";

                const actual = rgbToHexColor(0, 0, 0);

                assert.strictEqual(expected, actual);
            });
        });
        describe("check if output is of correct type", () => {
            it("check if string", () => {
                const expected = "string"

                const actual = rgbToHexColor(255, 255, 255);
                
                assert.strictEqual(expected, typeof actual)
            })
        })
});