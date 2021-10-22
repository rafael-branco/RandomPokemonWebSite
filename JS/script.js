$(document).ready(function(){

    $(".button-box button").click(function(event) {
        
        $.ajax({
            type: 'POST',
            url: '/D:\\Programação\\RandomPokemonWebSite\\getRandomPokemon.py'

        }).done(function(data){
            console.log("Done!");
            console.log(data.teste);
        });
        
        event.preventDefault();

//https://cursos.alura.com.br/forum/topico-from-origin-null-has-been-blocked-by-cors-policy-cross-origin-requests-are-only-supported-for-protocol-schemes-http-data-chrome-chrome-extension-https-101166
    });

});