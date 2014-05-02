$(document).ready(function(){
	//alert("test")
	$(".how").hide()
	$(".boards").hide()

	$(".howLink").click(function() {
        $(".how").toggle("slide", {direction: "up"}, 550);
    });

    $(".boardsLink").click(function() {
        $(".boards").toggle("slide", {direction: "up"}, 550);
    });
})