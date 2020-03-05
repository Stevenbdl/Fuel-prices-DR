document.getElementById("table-container").style.display = "none";

document.addEventListener("scroll", showTable);

function showTable(){
    let top = window.scrollY;
    let table = document.getElementById("table-container");

    if(top >= 600){
        table.classList.add("showTable");
        document.getElementById("table-container").style.display = "block";
    }
}