describe("should return the sum of the array", () => {
  it("return the sum", () => {
    const expected = 10

    const actual = sum([1,2,3,4])

    assert.strictEqual(expected, actual)
  })
})


describe("items in the array should be numbers", () => {
  it("output should not be NaN", () => {
    const expected = "number"

    const actual = typeof sum([1,2,3,4])

    assert.strictEqual(expected, actual)

  })
})