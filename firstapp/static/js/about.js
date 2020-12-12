let button = document.querySelector(".btn-primary");
var isVisible = false;
let my_hobbies = ['Chess', 'Football', 'Math', 'Programming']

function clickOnButton(event) {
    let parentNode = event.target.parentNode;
    if (!isVisible) {
        for (let i = 0; i < my_hobbies.length;i++) {
            let child = document.createElement("div");
            let attribute = my_hobbies[i];
            child.setAttribute("class", attribute);
            child.innerHTML = attribute;
            parentNode.appendChild(child);
        }
    } else {
        for (let i = 0; i < my_hobbies.length;i++) {
            parentNode.removeChild(document.querySelector("." + my_hobbies[i]))
        }
    }
    isVisible = !isVisible
}

button.onclick = clickOnButton;