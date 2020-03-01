$(document).ready(function (){

    $('body').on('submit', '#loginad', function (){

        var username = $('#userN').val();
        var password = $('#emailN').val();

        if(username == ""){
            $("#msg").html(' <div class="alert alert-danger material_alert material_alert_danger" > <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">x</span></button>  Enter Email Address</div>');


        }else if(password == ""){

            $("#msg").html(' <div class="alert alert-danger material_alert material_alert_danger" > <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">x</span></button>  Enter Password </div>');

        }else{

            $.ajax({
                type: "POST",
                url: document.location.origin + "/actions/addbank",
                data: dataString,
                processData: false,
                contentType: false,
                beforeSend: function () {

                    $("button#actionbtn").html('<i class="fa fa-spinner fa-spin"></i> In Progress...').attr("disabled", "disabled");

                }, success: function (data) {

                     if (data == 0) {
                        $("#msg").html(' <div class="alert alert-danger material_alert material_alert_danger" > <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">x</span></button>  Not allowed, login  and try again</div>');



                    } else if (data == 2) {
                        $("#msg").html(' <div class="alert alert-danger material_alert material_alert_danger" > <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">x</span></button>  Unable to proccess this action, try again</div>');

                    }  else if (data == 1) {

                        $("#msg").html(' <div class="alert alert-success" > <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">x</span></button>  Bank Account Updated Successfully</div>')
                            .delay(1000, function () {
                            setTimeout(function () {
                                $("#msg").html('');
                            }, 1000);

                    });
                    }

                }, error: function (e) {

                    alert(e);
                }

            });

        }

    })


})