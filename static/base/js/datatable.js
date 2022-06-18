$(document).ready(function() {
  $('#dataTable').DataTable({
        "language": {
            "lengthMenu": "Zeige _MENU_ Einträge pro Seite",
            "zeroRecords": "keine Transaktionen gefunden",
            "info": "Seite _PAGE_ von _PAGES_",
            "infoEmpty": "No records available",
            "infoFiltered": "(filtered from _MAX_ total records)",
            "search": "Suche",
            "paginate": {
                "first":      "erste Seite",
                "last":       "letzte Seite",
                "next":       "nächste Seite",
                "previous":   "vorherige Seite"
                },
        },
        "order": [],
    } );
});
