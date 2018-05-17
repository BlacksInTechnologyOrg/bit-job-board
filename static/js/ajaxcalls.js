	$('#FormMessageSend').on('click', function(event) {
		$.ajax({
			data : {
				username: $('#FormMessageUser').val(),
                subject: $('#FormMessageSubject').val(),
				message: $('#FormMessageMessage').val()
			},
			type : 'POST',
			url : '/message'
		})
		.done(function(data) {

			if (data.error) {
			    console.log("error");
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
			    $('#ModalMessage.close').click();

				$('#successAlert').text(data.name).show();
				$('#errorAlert').hide();
			}

		});

        event.preventDefault();


	});


    $("#inbox > tbody > tr").click(function() {
        var href = $(this).find("a").attr("href");
        if(href) {
            window.location = href;
        }
    });

