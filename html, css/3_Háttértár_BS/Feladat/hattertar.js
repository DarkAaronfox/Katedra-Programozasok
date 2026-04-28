    const alap = 1024;
    
    function HanyBajt(){
        var mirol;
        var ertek;
        var v = MirolValt(mirol);
        var eredmenyP = document.getElementById('bajt');
        eredmenyP.textContent =  ertek*Math.pow(alap, v)+' bájt';
    }

    function MirolValt(mirol){
    }
