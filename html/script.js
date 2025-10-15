document.addEventListener('DOMContentLoaded', () => {
    const inputs = document.querySelectorAll('.col-count-input');
    const totalInputDisplay = document.getElementById('grand-total-input');
    const calculateBtn = document.getElementById('calculate-btn');
    const transactionItems = document.querySelectorAll('.transaction-item');
    const resultAmountDisplay = document.getElementById('result-amount');
    const resultUnitDisplay = document.getElementById('result-unit');
    
    let currentRatio = parseFloat(document.querySelector('.transaction-item.active').dataset.ratio);

    const formatNumber = (num) => {
        return num.toLocaleString('vi-VN');
    };

    // tổng tiền khách đưa
    const updateInputTotals = () => {
        let grandTotal = 0;
        
        inputs.forEach(input => {
            const count = parseInt(input.value) || 0;
            const denomination = parseInt(input.dataset.value);
            const rowTotal = count * denomination;
            grandTotal += rowTotal;

            const rowTotalDisplay = input.nextElementSibling; 
            rowTotalDisplay.textContent = formatNumber(rowTotal) + ' VND';
        });

        totalInputDisplay.textContent = formatNumber(grandTotal) + ' VND';
        return grandTotal;
    };

    inputs.forEach(input => {
        input.addEventListener('input', updateInputTotals);
    });

    updateInputTotals();

    calculateBtn.addEventListener('click', () => {
        const grandTotal = updateInputTotals();
        
        // Công thức Quy đổi (Đơn giản: Chip = Tiền * Tỷ lệ)
        const chipResult = grandTotal / 1000 * currentRatio; // Giả sử 1 chip = 1000 VND

        // Cập nhật kết quả
        resultAmountDisplay.textContent = formatNumber(Math.round(chipResult));

        let transactionType = document.querySelector('.transaction-item.active span').textContent;
        let unitText = 'CHIP';

        if (transactionType.includes('TIỀN MẶT')) {
             unitText = 'VND'; // Nếu là giao dịch đổi chip -> tiền
        }
        
        resultUnitDisplay.textContent = unitText + ` (Tỉ lệ ${currentRatio}:1)`;
        
        if (grandTotal === 0) {
            resultAmountDisplay.textContent = '0';
        }
    });

    // Sự kiện chọn loại giao dịch
    transactionItems.forEach(item => {
        item.addEventListener('click', () => {
            // Xóa active khỏi nút cũ
            document.querySelector('.transaction-item.active').classList.remove('active');
            // Thêm active vào nút mới
            item.classList.add('active');
            
            // Cập nhật tỷ lệ và thực hiện tính toán lại
            currentRatio = parseFloat(item.dataset.ratio);
            calculateBtn.click();
        });
    });

    calculateBtn.click();
});