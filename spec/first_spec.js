describe("A suite is just a function", function() {
  var a;

  it("and so is a spec - true=true", function() {
    a = true;

    expect(a).toBe(true);
  });
});

describe("A suite is just a function22", function() {
  var a;

  it("and so is a spec - false=false", function() {
    a = false;

    expect(a).toBe(false);
  });
});
