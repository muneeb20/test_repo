$(document).ready(function () {
    $("#btn_sort_list").click(function (e) {
        e.preventDefault();
        var string_list_value = $("#txt_str_lst").val();
        if (string_list_value && string_list_value.split(',').length > 0) {
            post_string_list_via_ajax(e, string_list_value.split(','));
        }
        else {
            alert("Invalid String List Format");
        }
    });
});

post_string_list_via_ajax = function(e, string_list_data) {
    var data= {};
    data["string_list"] = JSON.stringify(string_list_data);
    $.ajax({
        type: "POST",
        data: data,
        url: "/api/v1/sort_string_list/",
        success: function (resp) {
            if (resp.success) {
                $("#response_message").html("Sorted List         " + resp.string_list);
            }
            else{
                $("#response_message").html(resp.msg);
            }
            $("#response_message").show();
        }
    })
}