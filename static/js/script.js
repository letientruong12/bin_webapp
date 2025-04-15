$(document).ready(function() {
    // Khởi tạo Select2 cho các select
    $('.select2').select2({
        placeholder: "Chọn giá trị",
        allowClear: true
    });

    // Lấy dữ liệu cho dropdown từ server
    $.ajax({
        url: '/get_options',
        method: 'GET',
        success: function(data) {
            // Country
            let countrySelect = $('#country');
            data.countries.forEach(function(country) {
                countrySelect.append(new Option(country, country));
            });

            // Bank Name
            let bankSelect = $('#bank_name');
            data.bank_names.forEach(function(bank) {
                bankSelect.append(new Option(bank, bank));
            });

            // Card Name
            let cardSelect = $('#card_name');
            data.card_names.forEach(function(card) {
                cardSelect.append(new Option(card, card));
            });

            let cardTypeSelect = $('#card_type');
            data.card_types.forEach(function(type) {
                cardTypeSelect.append(new Option(type, type));
            });

            let providerTypeSelect = $('#provider_type');
            data.provider_types.forEach(function(provider) {
                providerTypeSelect.append(new Option(provider, provider));
            });
        }
    });
});