$(document).ready(function() {
  $('.a-href-bombero-details').on(
      'click', function () {
        var bomberoDetailsURL = $(this)[0].dataset.url
        $( ".modal-bombero-details .modal-body" ).load( bomberoDetailsURL );
        $( ".modal-bombero-details" ).modal();
      });
});
