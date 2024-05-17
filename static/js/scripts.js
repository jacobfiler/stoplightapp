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
            { responsivePriority: 3, targets: 1 },  // Reform Name
            { responsivePriority: 4, targets: 2 },  // Reform Area
            { responsivePriority: 5, targets: 3 },  // Sources
            { responsivePriority: 6, targets: 4 },  // Additional Notes
            { responsivePriority: 7, targets: 5 }   // Last Updated
        ]
    });
});