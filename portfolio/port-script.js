const words = ["I'm Nisit KU", "I'm Computer Engineer", "I'm Developer", "I'm Data Engineer"];
const link = ["me1.jpg", "me2.jpg", "me3.jpg"];
let index1 = 0;
let index2 = 0;

function changeword() {
    document.getElementById("present-four").textContent = words[index1];
    index1 = (index1 + 1) % words.length;
}

function changepic() {
    document.getElementById("pic-me").src = link[index2];
    index2 = (index2 + 1) % link.length;
}

changeword();
changepic()
setInterval(changeword, 2000);
setInterval(changepic, 2000);