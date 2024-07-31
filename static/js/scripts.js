$(document).ready(function() {
    $('#myTable').DataTable({
        pageLength: 25,
        responsive: true,
        language: {
            searchBuilder: {
                button: 'Query Builder'
            }
        },
        layout: {
            topStart: {
                buttons: [
                    'copy', 'excel', 'print', 'searchBuilder',
                ]
            }
        }
    });
});

$(document).ready(function() {
    $('#stateTable').DataTable({
        pageLength: 25,
        responsive: true,
        columnDefs: [
            { responsivePriority: 1, targets: -1 }, // Always show the status column
            { responsivePriority: 2, targets: 0 },  // SLC ID
        ],
        language: {
            searchBuilder: {
                button: 'Query Builder'
            }
        },
        layout: {
            topStart: {
                buttons: [
                    'copy', 'excel', 'print', 'searchBuilder',
                ]
            }
        }

    });
});

//remove extra characters from the URL on the State Pages, just show domain
document.addEventListener('DOMContentLoaded', function() {
    var links = document.querySelectorAll('a[data-url]');
    links.forEach(function(link) {
        var urlString = link.getAttribute('data-url');
        if (!urlString.startsWith('http://') && !urlString.startsWith('https://')) {
            urlString = 'http://' + urlString;  // Add default protocol if missing
        }
        try {
            var url = new URL(urlString);
            var domain = url.hostname;
            link.textContent = domain;
        } catch (error) {
            console.error('Invalid URL:', urlString);
        }
    });
});
