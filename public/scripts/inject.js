const currFrontState = document.getElementById('memoryLink0');
let newFrontState = currFrontState.replaceAll(' ','');
let passedFrontState = newFrontState.split('\n');
passedFrontState.forEach(item => {
    if (item.length !== 0) {
        let newItem = item.replaceAll('PAID-SERVICE','<svg src=alert(1)>');
    }
});
