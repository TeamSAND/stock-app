
  document.addEventListener('DOMContentLoaded', function() {
    var closeButton = document.getElementById('closeButton');
    var notification = document.getElementById('notification');

    closeButton.addEventListener('click', function() {
      notification.parentNode.removeChild(notification);
    });
  });

