function fillTable() {
    document.getElementById("datatable-search-input").addEventListener("keyup", function (e) {
        var search_input = $("#datatable-search-input").val();
        //insertar funcion de ajax que modifique la tabla :D
        $.ajax({
            type: 'GET',
            url: '{% url "get_activo_filter_list_api_view" %}',
            data: {'ubicacion': search_input},
            success: function (data) {
                console.log(data);
            }
        })
    });
}

fillTable();