document.addEventListener('DOMContentLoaded', () => {
    const excelButton = document.getElementById('export-excel');
    if (excelButton) {
        excelButton.addEventListener('click', function () {
            import('https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js').then(({ XLSX }) => {
                const movimentacoes = JSON.parse(excelButton.dataset.movimentacoes);

                // Criar dados no formato necessário para Excel
                const data = movimentacoes.map(mov => ({
                    Movimento: mov.movimento,
                    Remetente: mov.setor_remetente || 'N/A',
                    Destinatário: mov.setor_destinatario || 'N/A',
                    Quantidade: mov.quantidade,
                    Data: mov.data_movimento,
                }));

                // Converter para uma planilha
                const ws = XLSX.utils.json_to_sheet(data);
                const wb = XLSX.utils.book_new();
                XLSX.utils.book_append_sheet(wb, ws, "Movimentações");

                // Exportar para arquivo Excel
                XLSX.writeFile(wb, "Relatorio.xlsx");
            });
        });
    }
});
