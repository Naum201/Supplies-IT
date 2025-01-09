    document.addEventListener('DOMContentLoaded', function() {
        // Verifica se há alerta de reposição
        const reposicaoAlert = document.getElementById('reposicaoAlert');
        
        if (reposicaoAlert) {
            // Adiciona um botão de fechar manual
            const closeButton = document.createElement('button');
            closeButton.classList.add('btn', 'btn-sm', 'btn-link', 'ml-2');
            closeButton.innerHTML = 'Fechar';
            reposicaoAlert.appendChild(closeButton);

            // Função para fechar o alerta
            closeButton.addEventListener('click', function() {
                reposicaoAlert.style.display = 'none';
            });

            // Fechar o alerta automaticamente após 10 segundos (10000 ms)
            setTimeout(function() {
                reposicaoAlert.style.display = 'none';
            }, 10000); // 10 segundos
        }
    });
