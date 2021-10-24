$(document).ready(function(){

    $(".button-box button").click(function(){
        $.get("../getRandomPokemon.py", function(data, status){
            alert("Data: " + data + "\nStatus: " + status);
        });
    });

});