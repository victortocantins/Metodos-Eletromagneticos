.. _frequency_domain_electric_dipole_fields:

Visualização dos Campos Eletromagnéticos
========================================

.. Purpose::

    Aqui, fornecemos ferramentas de modelagem numérica para visualizar o campo elétrico, campo magnético e densidade de corrente causados por uma fonte dipolo de corrente elétrica.
    Um conjunto de perguntas sobre os campos e sua dependência de vários parâmetros é apresentado como um exercício de aprendizagem.
    Ao completar este exercício, você se sentirá confortável com as ferramentas de modelagem numérica fornecidas e obterá uma compreensão fundamental dos campos que são causados por um dipolo de corrente elétrica harmônica.

    

**Link para o aplicativo de modelagem**


Questões de pesquisa
--------------------

Aqui, um conjunto de perguntas sobre os campos e sua dependência de vários parâmetros é apresentado como um exercício de aprendizagem.
O usuário é encorajado a responder a essas perguntas em ordem, à medida que começamos com casos simples e passamos para casos com física mais desafiadora.
O usuário também é encorajado a usar expressões analíticas e assintóticas como referência ao completar o exercício.
 

**Caso DC (Estático):**


Para o caso DC, certifique-se de que a frequência esteja definida para 0 Hz. Ao responder às perguntas a seguir, examine os componentes x, y e z do campo elétrico, campo magnético e densidade de corrente. O gráfico vetorial é recomendado.

    - O campo elétrico, campo magnético ou densidade de corrente tem componentes de quadratura (imaginários)?
    - O campo magnético tem algum componente ao longo da orientação do dipolo?
    - Quando você altera a condutividade (:math:`\sigma`), a forma do campo elétrico ou magnético muda? A magnitude muda?
    - Quando você altera a condutividade (:math:`\sigma`), algo sobre a densidade atual muda? (observe que :math:`\mathbf{J=\sigma E}`)
    - Suas observações fazem sentido ao considerar a :ref:`aproximação DC<frequency_domain_electric_dipole_asymptotics_DC>`?


**aproximação do Campo Próximo:**

Agora defina a condutividade do background para 1 S/m e defina a frequência para 1 Hz. De acordo com nossas aproximações assintóticas, o :ref:`campo próximo<frequency_domain_electric_dipole_asymptotics_near>` (:math:`| kr | \ll 1`) deve se comportar como o 
:ref:`campo DC<frequency_domain_electric_dipole_asymptotics_DC>`.

    - Examine os campos elétricos e magnéticos. Dentro do domínio definido, esses campos se comportam como campos DC?

Agora, aumente lentamente a frequência por fatores de 10. Quando você atingir 1000 Hz, observe que a uma distância suficiente do dipolo, a aproximação de campo próximo não é mais válida. No entanto, perto da fonte dipolo, os campos mais ou menos se comportam como campos DC.

    - A que distância a aproximação de campo próximo não é mais válida em 1000 Hz? Use este valor para confirmar que :math:`|kr| \ll 1`.

**A Resposta Indutiva:**

De acordo com :ref:`Lei de Faraday<faraday>`, os efeitos da indução EM aumentam à medida que a frequência aumenta. Defina a condutividade para 0,1 S/m e escolha um ponto (x,y,z)=(40m, 0m, 0m). Examine os componentes x, y e z dos campos elétricos e magnéticos.

    - Com que frequência os efeitos da indução EM se tornam significativos?
    - Agora aumente a condutividade de fundo para 1 S/m e examine o mesmo local. Com que frequência os efeitos da indução EM se tornam significativos?
    - Agora escolha um local mais próximo da fonte dipolo (x,y,z) = (10m, 0m, 0m). Com que frequência os efeitos da indução EM se tornam significativos em comparação com o campo primário?


**Permeabilidade Magnética e Permissividade Dielétrica**

Defina o perfil de condutividade para.

    - Tente aumentar a permeabilidade relativa (:math:`\mu_r`). Você percebe alguma mudança significativa na forma e amplitude dos campos elétricos e magnéticos?
    - Agora tente aumentar a permissividade relativa (:math:`\varepsilon_r`). Quando você faz isso em baixas frequências, você percebe alguma mudança significativa na forma e na amplitude dos campos elétricos e magnéticos? E quando você faz isso em altas frequências?
    

.. **Hypothetical Scenario 1:**

.. *I put this here in case we wanted to make a hypthetical scenario where these equations could be used to solve a practical problem.*




