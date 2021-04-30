.. _harmonic_planewaves_homogeneous_questions:

Questões
========


Skin Depth
----------

Uma onda plana :ref:`atenua-se<harmonic_planewaves_homogeneous_skindepth>` quando ela se propaga dentro da Terra. Use a frequência
de 10 Hz e a condutividade de :math:`\sigma` = 1 S/m para simulação inicial.

	- Plote a amplitude versus profundidade e estime a profundidade de penetração (skin depth).

	- Avalie o skin depth usando a :ref:`fórmula fornecida<harmonic_planewaves_homogeneous_skindepth_formula_quasi>`. Como esses valores se comparam?

	- Como o skin depth varia, se f = 100 Hz e :math:`\sigma` = 0,1 S/m forem usados?

	- Como o skin depth varia, se f = 1 Hz e :math:`\sigma` = 1 S/m forem usados?

Componentes Real and Imaginária
-------------------------------

A medida que a onda plana se propaga para a Terra, há uma componente real (em fase) e uma imaginária (em quadratura ou fora de fase). 
Por padrão, o aplicativo mostra esses sinais no tempo t = 0 (por exemplo :math:`e^{\pm i\omega t}` = 1). 
Assim, na superfície (z = 0) o campo :math:`E_x` é puramente real e o campo :math:`H_y` tem partes reais e imaginárias iguais. 
Por que isso é verdade? (dica: examine a solução final para :math:`H_y` :ref:`aqui<harmonic_planewaves_homogeneous_derivation_app_soln>`).

	- Considere uma profundidade z = 100 m. Avalie os componentes reais e imaginários de :math:`E_x` e :math:`H_y` 
  	  naquele ponto para f = 10 Hz e :math:`\sigma` = 1 S/m usando a :ref:`solução analítica<harmonic_planewaves_homogeneous_derivation_app_soln>`; 
	  assuma uma amplitude inicial de 1. Compare esses valores com os obtidos usando o aplicativo.
	- Use os valores reais e imaginários para :math:`E_x` do aplicativo para calcular a amplitude em z = 100 m. Use a :ref:`fórmula de atenuação<harmonic_planewaves_homogeneous_attenuation_formula>` para calcular a amplitude teórica nessa profundidade; assuma uma amplitude inicial :math:`A_0` = 1.
	- Calcule a fase entre as componentes reais e imaginários de :math:`E_x` em z = 100 m. Como o seu número se compara ao fornecido diretamente pelo aplicativo? Observe que a curva de fase exibe algum comportamento estranho. Isso parece fisicamente real e o que está acontecendo?

Comprimento de Onda
-------------------

Há uma série de gráficos a partir dos quais você pode estimar o comprimento de onda dos campos EM

- Qual parece o mais preciso? Por quê?
- Use o aplicativo para estimar visualmente o comprimento de onda de :math:`E_x` e :math:`H_y` para f = 10 Hz e :math:`\sigma` = 1 S / m. Ambos os valores são iguais ou diferentes, e isso faz sentido? Use :ref:`esta fórmula<harmonic_planewaves_homogeneous_wavelength_formula>` para calcular o comprimento de onda e comparar com os valores obtidos do aplicativo.
- O que acontece com o comprimento de onda se você definir f = 100 Hz?


Velocidade de Fase
------------------

O aplicativo fornece um snapshot das ondas na terra no tempo t = 0 (por exemplo :math:`e^ {\pm i \omega t}` = 1). Conforme o tempo avança, as ondas se propagam para baixo. Se você seguir um pico individual, vale ou cruzamento zero (experimente a escala logarítmica!) Com o tempo, você pode estimar a velocidade da fase. Faça isso ajustando o controle deslizante de tempo.

	- Escolha um ponto de referência duas vezes (digamos 0,02 e 0,04 segundos) e estime a velocidade da fase. Compare seu resultado com o resultado teórico dado por :ref:`esta equação<harmonic_planewaves_homogeneous_phasevelocity_quasi>`.


Impedância e Fase
-----------------

A :ref:`impedância da onda<harmonic_planewaves_homogeneous_impedancephase>` :math:`Z_{xy}=E_x/H_y` 
é um número complexo ele pode ser visualizado no aplicativo junto com os campos :math:`E_x` e :math:`H_y`. Usando a impedância da onda, podemos calcular :ref:`diferença na fase<harmonic_planewaves_homogeneous_impedancephase>` entre :math:`E_x` e :math:`H_y`. Os campos variam com a profundidade e com o tempo, mas, por definição, a impedância e a fase não.

	- Use o aplicativo para calcular a impedância da onda. Agora calcule a impedância da onda com :ref:`esta equação<harmonic_planewaves_homogeneous_impedancephase>`. Como os valores se comparam?
	- Use o aplicativo para determinar a fase. Agora calcule a fase com :ref:`esta equação<harmonic_planewaves_homogeneous_impedancephase>`. Como os valores se comparam?
	- Ajuste o controle deslizante de tempo. A impedância ou fase muda?


Resistividade Aparente
----------------------

Impedâncias podem ser convertidas para :ref:`resistividades aparentes<harmonic_planewaves_homogeneous_apparentresistivity>`.

- Use seus valores de impedância do exercício anterior e :ref:`esta equação<harmonic_planewaves_homogeneous_apparentresistivity>` 
  para calcular a resistividade aparente. Como esse valor se compara à resistividade inserida no app? (*Observe que não importa em que profundidade as medições foram obtidas*).


