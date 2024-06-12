$(document).ready(function() {
    $('#myTable').DataTable({
        pageLength: 25,
        responsive: true
    });
});

$(document).ready(function() {
    $('#stateTable').DataTable({
        pageLength: 25,
        responsive: true,
        columnDefs: [
            { responsivePriority: 1, targets: -1 }, // Always show the status column
            { responsivePriority: 2, targets: 0 },  // SLC ID
        ]
    });
});
