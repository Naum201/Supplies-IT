document.addEventListener('DOMContentLoaded', () => {
    const pdfButton = document.getElementById('export-pdf');
    if (pdfButton) {
        pdfButton.addEventListener('click', function () {
            import('https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.4.0/jspdf.umd.min.js').then((jsPDFModule) => {
                const { jsPDF } = jsPDFModule; // Extrair o construtor jsPDF do módulo

                const doc = new jsPDF();
                doc.text("Relatório de Movimentações", 10, 10);

                // Adicionar movimentações no PDF
                const movimentacoes = JSON.parse(pdfButton.dataset.movimentacoes);
                let startY = 20;

                movimentacoes.forEach((movimentacao, index) => {
                    doc.text(`${index + 1}. Movimento: ${movimentacao.movimento}`, 10, startY);
                    doc.text(`   Remetente: ${movimentacao.setor_remetente || 'N/A'}`, 10, startY + 10);
                    doc.text(`   Destinatário: ${movimentacao.setor_destinatario || 'N/A'}`, 10, startY + 20);
                    doc.text(`   Quantidade: ${movimentacao.quantidade}`, 10, startY + 30);
                    startY += 40;
                });

                doc.save("Relatorio.pdf");
            }).catch((error) => {
                console.error("Erro ao carregar jsPDF:", error);
            });
        });
    }
});
