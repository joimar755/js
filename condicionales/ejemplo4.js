function AdivinaNumero() {
    const numeroALeatorio = Math.floor(Math.random()*10) + 1;
    let numeroUsuario = 3
    if (parseInt(numeroUsuario) === numeroALeatorio) {
        console.log('��Has acertado! El número era '+ numeroALeatorio);
    }else{
        console.log('Has fallado. El número era '+ numeroALeatorio);
    }
    
}
AdivinaNumero()