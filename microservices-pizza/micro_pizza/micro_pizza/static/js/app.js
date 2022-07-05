
$(document).ready(function() {
			    $('#power').dataTable( {
			    	responsive: true,


			        dom: 'Bfrtip',
			        buttons: [
			            'pageLength',
			            'copyHtml5',
			            'excelHtml5',
			            'csvHtml5',
			            'pdfHtml5',
			            'print',

			        ],
			        "lengthMenu": [ [10, 25, 50, -1], [10, 25, 50, "All"] ],
			        // orientation: 'landscape',

			        // Naanza footer sum

			        	"footerCallback": function ( row, data, start, end, display ) {
					            var api = this.api(), data;

					            // Remove the formatting to get integer data for summation
					            var intVal = function ( i ) {
					                return typeof i === 'string' ?
					                    i.replace(/[\$,]/g, '')*1 :
					                    typeof i === 'number' ?
					                        i : 0;
					            };

					            // Total over all pages
					            total = api
					                .column( 5 )
					                .data()
					                .reduce( function (a, b) {
					                    return intVal(a) + intVal(b);
					                }, 0 );

					            // Total over this page
					            pageTotal = api
					                .column( 5, { page: 'current'} )
					                .data()
					                .reduce( function (a, b) {
					                    return intVal(a) + intVal(b);
					                }, 0 );

					            // Update footer
					            $( api.column( 5 ).footer() ).html(
					                '$'+pageTotal +' ( $'+ total +' total)'
					            );
					        }

			        //end footer sum

			    } );

			} );