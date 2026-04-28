function Menetido_szamitas(){
    let kezd = document.getElementById("indul").value;
    let veg = document.getElementById("erkezik").value
    let menetido = Math.abs(kezd - veg);
    if (menetido != 0)
    {
        alert("Menetidő: " + menetido + " perc")
    }
    else{
        alert("Hiba: Azonos megállókat választottál ki");
    }
}