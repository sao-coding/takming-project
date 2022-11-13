function change(active, value) {
    let list = document.querySelectorAll(".list");
    for (let i = 0; i < list.length; i++) {
        list[i].className = "list selected";
    }
    active.className = "list selected-active";
    if (value == 1) {
        document.querySelector(".search1").style.display = "block";
        document.querySelector(".search2").style.display = "none";
        document.querySelector(".search3").style.display = "none";
    } else if (value == 2) {
        document.querySelector(".search1").style.display = "none";
        document.querySelector(".search2").style.display = "block";
        document.querySelector(".search3").style.display = "none";
    } else if (value == 3) {
        document.querySelector(".search1").style.display = "none";
        document.querySelector(".search2").style.display = "none";
        document.querySelector(".search3").style.display = "block";
    }
}