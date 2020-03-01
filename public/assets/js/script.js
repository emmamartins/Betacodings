
$(document).ready(function(){

    $('body').on('submit', '#contactform', function(e){

        e.preventDefault();
        var email = $("#email").val();
        var name = $("#name").val();
        var message = $("#message").val();
        var attachment = $("#attachment").val();
        

        var dataString = new FormData($("#contactform")[0]);
        
        if (name == ""){

            $("#msg").html('<div class="alert alert-danger material_alert material_alert_danger" > <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">x</span></button>  Enter Full Name  </div>');

        }else if (email == ""){

            $("#msg").html('<div class="alert alert-danger material_alert material_alert_danger" > <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">x</span></button>  Enter Email Address </div>');

        }else if (!emailValidation(email)) {

            $("#msg").html('<div class="alert alert-danger material_alert material_alert_danger" > <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">x</span></button>  Invalid Email Address </div>');
            
        }else if (message == ""){

            $("#msg").html('<div class="alert alert-danger material_alert material_alert_danger" > <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">x</span></button>  Enter Message Content </div>');

        }else{
            $("#msg").html('');
            $.ajax({
                type: "POST",
                url: document.location.origin + "/action/subscribe",
                data: dataString,
                processData: false,
                contentType: false,
                beforeSend: function () {

                    $("button#subscribehome").html('<i class="fa fa-spinner fa-spin"></i> In Progress...').attr("disabled", "disabled");
                    $("button#subscribehome").css("pointer-events", "none");
                }, success: function (data) {
                        alert(data);
                }, 
                error: function(e){

                    alert(e);
                }
            });

        }
        
    })

    $('body').on('submit', '#subscribeform', function(e){

        e.preventDefault();
        var email = $("#email").val();
        var dataString = new FormData($("#subscribeform")[0]);
        
        if (email == ""){

            $("#msg").html('<div class="alert alert-danger material_alert material_alert_danger" > <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">x</span></button>  Enter Email Address </div>');

        }else if (!emailValidation(email)) {

            $("#msg").html('<div class="alert alert-danger material_alert material_alert_danger" > <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">x</span></button>  Invalid Email Address </div>');
            
        }else{
            $("#msg").html('');
            $.ajax({
                type: "POST",
                url: document.location.origin + "/action/subscribe",
                data: dataString,
                processData: false,
                contentType: false,
                beforeSend: function () {

                    $("button#subscribehome").html('<i class="fa fa-spinner fa-spin"></i> In Progress...').attr("disabled", "disabled");
                    $("button#subscribehome").css("pointer-events", "none");
                }, success: function (data) {
                        alert(data);
                }, 
                error: function(e){

                    alert(e);
                }
            });

        }
        
    })
})

function phoneValidation(phoneN){

    var phone_reg = /^([+]?\d{1,4}[.-\s]?)?(\d{3}[.-]?){2}\d{4}$/; // reg ex Phone check

    return phone_reg.test(phoneN);
}
function emailValidation(email){

    var email_reg = /^[\w%_\-.\d]+@[\w.\-]+.[A-Za-z]{2,6}$/; // reg ex email check

    return email_reg.test(email);
}

function gettext(val, url) {
    var geturl = url;
    var getstring = val.value;
    var getnonchar = getstring.replace(/\W+/g, " ");
    // alert(getstring);

    $("#urlink").text(geturl + getnonchar.toLowerCase().replace(/ /g, '-').replace(/[^\w-]+/g, '') + '.html');


}