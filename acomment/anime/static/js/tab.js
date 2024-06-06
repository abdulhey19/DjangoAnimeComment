const liste=document.getElementById("liste");
const hangisi=document.getElementById("hangisi");
let sayi=0
console.log(sayi);
const showInfo=(e)=>{
   
    for(let i=0; i<liste.children.length; i++) {
        if (liste.children[i].firstElementChild.classList.contains("active")) {
            liste.children[i].firstElementChild.classList.remove("active");
            
        }
    }
    e.target.classList.add("active");
    for(let i=0; i<liste.children.length; i++){
        if (liste.children[i].firstElementChild.classList.contains("active")) {
             hangisi.children[i].style.display="block";  
             sayi=i;
             console.log(sayi);
        }else{
           hangisi.children[i].style.display="none";          
        }

    }
    e.preventDefault();
}
    
document.addEventListener("DOMContentLoaded", function(e) {
    liste.children[sayi].classList.add("active");
    hangisi.children[sayi].classList.add("block");
    console.log(sayi);
    e.preventDefault();

});    

liste.addEventListener("click",showInfo);
