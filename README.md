# Literosfera - Acervo Lusófono de Domínio Público

## Objetivo do Projeto
O Literosfera é uma plataforma educacional dedicada à curadoria e distribuição de obras literárias de domínio público. O objetivo é democratizar o acesso à literatura clássica luso-brasileira para estudantes e professores, oferecendo downloads em formatos PDF e EPUB de forma gratuita e acessível.

## Tecnologias Utilizadas
- **Hugo**: Gerador de sites estáticos de alta performance.
- **Tailwind CSS**: Framework de estilização utilitária para um design responsivo e premium.
- **Decap CMS (anteriormente Netlify CMS)**: Sistema de gerenciamento de conteúdo baseado em Git.
- **Giscus**: Sistema de comentários baseado em GitHub Discussions.
- **Google Fonts**: Tipografias modernas (Outfit e Merriweather).
- **GitHub Actions**: Automação de deploy e processamento de livros.

## Como Executar Localmente
1. Certifique-se de ter o [Hugo](https://gohugo.io/) instalado.
2. Clone o repositório.
3. Execute o comando:
   ```bash
   hugo server
   ```
4. Acesse `http://localhost:1313`.

## Como Adicionar Livros
Os livros podem ser adicionados via painel administrativo (`/admin`) ou criando arquivos markdown na pasta `content/livros/`.
Agora é possível inserir links externos para PDF e EPUB, permitindo importar obras de outras fontes como a Biblioteca Nacional ou o [Project Gutenberg](https://www.gutenberg.org/).

## Implantação
O projeto está configurado para ser implantado via GitHub Pages / Netlify.
URL: [https://zonaeducacional.github.io/leiamais/](https://zonaeducacional.github.io/leiamais/)

## Histórico de Modificações (Changelog)
### v2.1 - 11/05/2026
- **Sistema de Comentários**: Implementação do Giscus integrado ao GitHub Discussions para interação dos leitores.
- **Melhoria na Importação**: Adicionado suporte para upload/link de capa diretamente no processo de importação do CMS.
- **Robustez**: Escapamento de caracteres especiais em títulos para evitar quebra de YAML no Hugo.

### v2.0 - 11/05/2026
- **Rebranding**: Mudança de nome para "Literosfera".
- **Nova Identidade Visual**: Implementação de paleta de cores personalizada (Teal/Sage/Cream) com foco em contrastes profissionais e estética premium.
- **Layout de Experiência do Usuário**:
  - Botões de download movidos para o topo da página do livro para acesso imediato.
  - Explicação detalhada sobre Domínio Público adicionada à Home.
  - Novo rodapé institucional.
- **Expansão de Fontes**: Adicionados campos no CMS para links externos de PDF/EPUB e identificação da fonte original.

---
**Desenvolvido pelo Prof. Sérgio Araújo para LPT e Língua Portuguesa . 2026.**
