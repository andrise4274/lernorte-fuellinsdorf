// code for interacting with the html tables

window.addEventListener('DOMContentLoaded', function () {

    // code to search the table
    document.getElementById('searchInput').addEventListener('input', function () {
        var upper = this.value.toUpperCase();
        var names = document.querySelector("#dataTable tbody").rows;
        
        for (var i = 0; i < names.length; i++) {
            var firstCol = names[i].cells[0].textContent.toUpperCase();
            if (firstCol.indexOf(upper) > -1) {
                names[i].style.display = "";
            } else {
                names[i].style.display = "none";
            }
        }
    });

    

    // code to sort the table by clicking on the coumn heads
    document.querySelectorAll('th.sortable').forEach(function(header, index) {
        header.addEventListener('click', function() {
            sortTable(index);
        });
    });
    
    function sortTable(colIndex) {
        var table = document.getElementById("dataTable");
        var rows = Array.from(table.rows).slice(1);
        var ascending = true;
    
        if (table.getAttribute('data-sorted-column') == colIndex) {
            ascending = table.getAttribute('data-sort-order') !== 'asc';
        }
    
        rows.sort(function(rowA, rowB) {
            var cellA = rowA.cells[colIndex].firstChild;
            var cellB = rowB.cells[colIndex].firstChild;
    
            var valA = cellA.tagName === 'INPUT' ? cellA.checked : cellA.textContent.trim().toUpperCase();
            var valB = cellB.tagName === 'INPUT' ? cellB.checked : cellB.textContent.trim().toUpperCase();
    
            if (valA > valB) return ascending ? -1 : 1;
            if (valA < valB) return ascending ? 1 : -1;
            return 0;
        });
    
        rows.forEach(function(row) {
            table.tBodies[0].appendChild(row);
        });
    
        table.setAttribute('data-sorted-column', colIndex);
        table.setAttribute('data-sort-order', ascending ? 'asc' : 'desc');
    }
    


})
