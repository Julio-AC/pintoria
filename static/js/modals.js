function openModal(modalId) {
    // Cierra todos los modales abiertos
    $('.modal').modal('hide');

    // Abre el modal específico
    $('#' + modalId + 'Modal').modal('show');
}