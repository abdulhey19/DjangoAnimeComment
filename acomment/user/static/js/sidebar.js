const liste=document.querySelector("#liste");



const locref=document.location.href;

for (let i=0; i<liste.children.length; i++){
    if( locref===liste.children[i].firstElementChild.href){
        liste.children[i].firstElementChild.classList.add("active");
    }
}