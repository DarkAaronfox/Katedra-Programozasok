function klikk(){
    document.getElementById('szovegkeret').style.display='none';
    document.getElementById('kep').src=melyik+'.jpg';
    document.getElementById('kepkeret').style.display='block';   
}

function keprejt(melyik){
  document.getElementById('kepkeret').style.display='none';
  document.getElementById('szovegkeret').style.display='block';    
}