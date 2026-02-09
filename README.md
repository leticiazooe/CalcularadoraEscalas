# 📐 Calculadora de Escalas
A Calculadora de Escalas é uma ferramenta desktop de precisão desenvolvida para estudantes e profissionais de desenho técnico. Ele automatiza o cálculo de escalas de ampliação, redução e real, eliminando erros matemáticos e agilizando o processo de detalhamento de peças e projetos.

## Interface do Programa:

<div align="center">
  <img width="430" height="560" alt="Mestre das Escalas Interface" src="https://github.com/user-attachments/assets/44889a13-7ad6-4560-8505-ab79f31eff6f">
</div>



## Autores

- [@leticiazooe](https://www.github.com/leticiazooe)

# 🛠️ Funcionalidades

- **Cálculo Automático**: Preencha dois campos e o sistema identifica e resolve o terceiro valor faltante automaticamente.
- **Detecção de Escala**: Identifica se a escala inserida ou calculada é de **Ampliação** (ex: 2:1) ou **Redução** (ex: 1:50).
- **Suporte a Formatos Técnicos**: Aceita entradas no formato padrão `1:50`, `5:1` ou apenas o valor decimal.
- **Interface Inteligente**: Tratamento de erros para entradas inválidas e suporte a uso de vírgulas ou pontos decimais.
- **Design Moderno**: Interface construída com CustomTkinter, oferecendo suporte nativo ao modo claro/escuro do sistema operacional.

# 📐 Fórmulas Matemáticas Aplicadas

O software utiliza as normas fundamentais do desenho técnico para os cálculos:

1. **Escala ($E$)**: $E = d / R$
2. **Dimensão Real ($R$)**: $R = d / f$
3. **Dimensão no Desenho ($d$)**: $d = R * f$

*(Onde $f$ é o fator decimal da escala)*

# 💻 Stack Utilizada

O projeto foi construído utilizando tecnologias modernas de Python para garantir uma ferramenta leve, rápida e com visual atraente.

* **Linguagem:** [Python 3.x](https://www.python.org/) - Base robusta para cálculos matemáticos e lógica de script.
* **Interface Gráfica (GUI):** [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) - Framework de interface UI/UX moderna com suporte nativo a temas e cantos arredondados.
* **Lógica:** **Álgebra Linear Aplicada** - Implementação de algoritmos de Proporcionalidade Geométrica para conversão precisa de medidas.
* **Design:** **Modern UI** - Interface limpa e minimalista com suporte a **Temas Dinâmicos** (Dark & Light Mode), adaptando-se às preferências do sistema operacional do usuário.

# 🚀 Instalação e Configuração
### 1. Requisitos Prévios
Certifique-se de ter o **Python 3.7+** instalado em sua máquina.

### 2. Clonar o Repositório
Abra o seu terminal ou prompt de comando e execute:
```bash
  git clone https://github.com/leticiazooe/CalculadoraEscalas.git
cd CalculadoraEscalas

