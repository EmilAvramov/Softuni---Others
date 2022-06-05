describe("test function parameters", () => {
    let expected;

    before(() => {
        expected = false;
    });

    it("with a non-array input", () => {
        const actual = isSymmetric("test");

        assert.strictEqual(expected, actual);
    });

    it("with an array input", () => {
        const actual = isSymmetric([1, 1, 1, 1, 1]);
        assert.notStrictEqual(expected, actual);
    });

    it("with a symmetric array input of numbers", () => {
        const actual = isSymmetric([1, 2, 1]);

        assert.notStrictEqual(expected, actual);
    });

    it("with a non-symmetric array of numbers", () => {
        const actual = isSymmetric([1, 2, 3]);

        assert.strictEqual(expected, actual);
    });

    it("with a symmetric array of mixed items", () => {
        const actual = isSymmetric([1, 2, "wood", 2, 1]);

        assert.notStrictEqual(expected, actual)
    });
    it("with a non-symmetric array of mixed items", () => {
      const actual = isSymmetric([1,2,3, "wood", "stone", false])

      assert.strictEqual(expected, actual)
    })
});
