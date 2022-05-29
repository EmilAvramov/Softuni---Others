function editElement(target, find, replace) {
    while (target.innerHTML.includes(find)) {
        target.innerHTML = target.innerHTML.replace(find, replace);
    }
}
