$(document).ready(function () {
    $("#saveTodo").click(function () {
        $.ajax({
            url: 'savetodo',
            method: 'POST',
            data: {
                "name": $('#nameInput').val(),
                "description": $('#descriptionInput').val()
            },
            success: function (response) {
                location.reload();
            }
        });
    });
    $(document).on('click', '.deleteTodo', function () {
        $.ajax({
            url: 'deletetodo',
            method: 'DELETE',
            data: {
                "todoToDelete": $(this).attr('id')
            },
            success: function (response) {
                location.reload();
            }
        });
    });
    $("#openAddTodoModal").click(function () {
        $('#nameInput').val('');
        $('#descriptionInput').val('');
        $('#addTodoModal').modal('show');
    });
    $(".closeModal").click(function () {
        $('#addTodoModal').modal('hide');
    });
});