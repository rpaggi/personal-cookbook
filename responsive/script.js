var nav_toggle = "<div class='nav-toggle' id='menuOpen'>Menu</div>"
function menu() {
		$('.nav-toggle').click(function() {
			if($("#listaMenu").hasClass("side-fechado")) {
				$('#listaMenu').animate({
				    left: "9px",
				}, 100, function() {
				    $("#listaMenu").removeClass("side-fechado");
				});
			}
			else {
				$('#listaMenu').animate({
				    left: "-500px",
				}, 100, function() {
				    $("#listaMenu").addClass("side-fechado");
				});
			}
		});
}
	
//Menu Sidebar
$(window).resize(function() {
	var tamanhoJanela = $(window).width();
	
	if (tamanhoJanela < 990) { 
		$('#listaMenu').css('left', '-500px').addClass('side-fechado');
		// $('#listaMenu').append( "<div id='menuClose' class='nav-toggle'><a href='#''>[x]</a></div>" );
		$('#sideBar').append( "<div class='nav-toggle' id='menuOpen'>Menu</div>" );
	} else {
		$('#listaMenu').css('left', '0px').addClass('side-fechado');
		$('.nav-toggle').remove();
	}
	
	menu();
});

$(document).ready(function() {
	var tamanhoJanela = $(window).width();
	
	if (tamanhoJanela < 990) { 
		$('#listaMenu').css('left', '-500px').addClass('side-fechado');
		// $('#listaMenu').append( "<div id='menuClose' class='nav-toggle'><a href='#''>[x]</a></div>" );
		$('#sideBar').append( "<div class='nav-toggle' id='menuOpen'>Menu</div>" );
	} else {
		$('#listaMenu').css('left', '0px').addClass('side-fechado');
		$('.nav-toggle').remove();
	}
	
	menu();
});

