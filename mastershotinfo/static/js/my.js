
$(document).ready(function() {
	
	// AJAX GET
	$('.get-projects').click(function(){
		alert("get Ajax request");
        $.ajax({
            type: "GET",
            url: "/get_projects/",
			dataType: 'json',
			success: function(data) 
			{	
				console.log(data);
				$('.get-projects').html(data.html_form);

				for(i = 0; i < data.length; i++)
				{
                	$('ul').append('<li>'+data[i].type+'</li>');
				}				
			}
		
        });

    });


	// AJAX POST
	$('.add-projects').click(function(){
		console.log('am i called');
  
		  $.ajax({
			  type: "POST",
			  url: "/add_projects/",
			  dataType: "json",
			  data: { "item": $(".projects").val() },
			  success: function(data) {
				  alert(data.message);
				  console.log(data);
			  }
		  });
  
	  });
	// CSRF code 
	function getCookie(name) {
        var cookieValue = null;
        var i = 0;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (i; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    }); 
});





