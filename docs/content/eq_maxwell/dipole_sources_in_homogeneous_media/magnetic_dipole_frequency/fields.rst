.. _frequency_domain_magnetic_dipole_fields:

Visualização dos Campos Eletromagnéticos
========================================

.. Purpose::

     Aqui, fornecemos ferramentas de modelagem numérica para visualizar o campo elétrico, campo magnético e densidade de corrente causados por uma fonte de dipolo magnético. Um conjunto de perguntas sobre os campos e sua dependência de vários parâmetros é apresentado como um exercício de aprendizagem.
     Ao completar este exercício, você se sentirá confortável com as ferramentas de modelagem numérica fornecidas e obterá uma compreensão fundamental dos campos que são causados por um dipolo magnético harmônico.


**Link para o App**

Questões de Pesquisa
--------------------

Aqui, um conjunto de perguntas sobre os campos e sua dependência de vários parâmetros é apresentado como um exercício de aprendizagem.
O usuário é encorajado a responder a essas perguntas em ordem, à medida que começamos com casos simples e passamos para casos com física mais desafiadora.
O usuário também é encorajado a usar expressões analíticas e assintóticas como referência ao completar o exercício.



**Caso DC (Estático):**

Para o caso DC, certifique-se de que a frequência esteja definida para 0 Hz. Ao responder às perguntas a seguir, examine os componentes x, y e z do campo elétrico, campo magnético e densidade de corrente. O gráfico vetorial é recomendado.

    - Neste caso, existe um campo elétrico e/ou densidade de corrente diferente de zero?
    - O campo magnético tem algum componente radial?
    - O campo magnético tem algum componente de quadratura (imaginário)?
    - Algum aspecto do campo magnético muda quando você altera as propriedades físicas do meio?
    - Suas observações fazem sentido ao considerar a :ref:`aproximação DC<frequency_domain_magnetic_dipole_asymptotics_DC>`?

**Aproximação de campo próximo:**

Agora defina a condutividade do fundo para 1 S/m e defina a frequência para 1 Hz. De acordo com nossas aproximações assintóticas, o 
:ref:`campo próximo<frequency_domain_magnetic_dipole_asymptotics_near>` ( :math:`|kr| \ll 1`) o campo magnético deve se comportar como o caso DC e o campo elétrico deve ter apenas quadratura (imaginária ) componentes.

    - Examine os campos elétricos e magnéticos. Suas observações se comparam bem com o que você esperaria?
    - Aumente a frequência por um fator de 10. A intensidade do campo magnético muda? A intensidade do campo elétrico muda? Isso faz sentido ao considerar as aproximações de campo próximo?
    - Os campos elétricos induzidos são rotacionais em relação ao dipolo?

Agora, aumente lentamente a frequência por fatores de 10. Quando você atingir 1000 Hz, observe que a uma distância suficiente do dipolo, a aproximação de campo próximo não é mais válida. No entanto, perto da fonte dipolo, os campos mais ou menos se comportam como campos DC.

    - A que distância a aproximação de campo próximo não é mais válida em 1000 Hz? Use este valor para confirmar que :math:`|kr| \ll 1`.


**A resposta Indutiva:**

De acordo com :ref:`Lei de Faraday<faraday>`, os efeitos da indução EM aumentam à medida que a frequência aumenta. Defina a condutividade para 0,1 S/m e escolha um ponto (x, y, z) = (40m, 0m, 0m). Examine os componentes x, y e z dos campos elétricos e magnéticos.

    - Com que frequência os efeitos da indução EM se tornam significativos?
    - Agora aumente a condutividade de fundo para 1 S / me examine o mesmo local. Com que frequência os efeitos da indução EM se tornam significativos?
    - Agora escolha um local mais próximo da fonte dipolo (x, y, z) = (10m, 0m, 0m). Com que frequência os efeitos da indução EM se tornam significativos em comparação com o campo primário?

**Permeabilidade Magnética e Permissividade Dielétrica:**

Defina a condutividade logarítmica para 0,01 S/m.

    - Tente aumentar a permeabilidade relativa (:math:`\mu_r`). Você percebe alguma mudança significativa na forma e amplitude dos campos elétricos e magnéticos?
    - Agora tente aumentar a permissividade relativa (:math:`\varepsilon_r`). Quando você faz isso em baixas frequências, você percebe alguma mudança significativa na forma e na amplitude dos campos elétricos e magnéticos? E quando você faz isso em altas frequências?






