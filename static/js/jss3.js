const txts=document.querySelector(".animate-text").children,
      txtsLen=txts.length;
  let index=0;
 const textInTimer=4000,
       textOutTimer=3800;

function animateText() {
   for(let i=0; i<txtsLen; i++){
     txts[i].classList.remove("text-in","text-out");  
   }
   txts[index].classList.add("text-in");

   setTimeout(function(){
       txts[index].classList.add("text-out");              
   },textOutTimer)

   setTimeout(function(){

     if(index == txtsLen-1){
         index=0;
       }
      else{
          index++;
        }
       animateText();
   },textInTimer); 
}

window.onload=animateText;



  let slideIndex = 0;
    showSlides();
    
    function showSlides() {
      let i;
      let slides = document.getElementsByClassName("mySlides");
      let dots = document.getElementsByClassName("dot");
      for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  
      }
      slideIndex++;
      if (slideIndex > slides.length) {slideIndex = 1}    
      for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
      }
      slides[slideIndex-1].style.display = "block";  
      dots[slideIndex-1].className += " active";
      setTimeout(showSlides, 2000); // Change image every 2 seconds
    }