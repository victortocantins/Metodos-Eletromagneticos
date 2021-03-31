.. _fundamental_laws_coulomb:

Lei de Gauss a partir da Lei de Coulomb
=======================================


.. _gauss_electric_equivalence_to_coulombs_law:

Equivalência da Lei de Gauss para Campos Elétricos com a Lei de Coulomb
***********************************************************************
 
 .. figure:: images/CoulombsLaw.png
    :align: right
    :scale: 75% 
    :name: CoulombsLaw

    Força Elétrica

A lei de Coulomb é muitas vezes uma das primeiras leis quantitativas encontradas por
estudantes de eletromagnetismo. Descreve a força entre duas
cargas eletricas pontuais. Acontece que é equivalente à lei de Gauss. A lei de Coulomb 
afirma que a força entre duas cargas elétricas pontuais estáticas é
proporcional ao inverso do quadrado da distância entre elas, atuando na
direção de uma linha que as conecta. Se as cargas forem de sinais opostos, a
força é atrativa e se as cargas forem do mesmo sinal, a força é
repulsiva. Matematicamente, a lei de Coulomb é escrita como    

.. math::
  \mathbf{F} = \frac{qQ}{4\pi \varepsilon_0 |\mathbf{r} - \mathbf{r'}|^2}~\mathbf{\hat{\underline{r}}} \;,
  :label: Coulomb_q

onde :math:`\mathbf{F}` é a força entre duasa cargas :math:`q` and :math:`Q`, :math:`|\mathbf{r} - \mathbf{r'}|` é a distância entre as cargas e  :math:`\mathbf{\hat{\underline{r}}}` é o vetor unitário na direção da linha que separa as duas cargas.

Tendo definido a lei de Coulomb, pode-se naturalmente perguntar como
uma carga de referência padrão se comportaria na presença de qualquer distribuição
de carga elétrica que podemos pensar? Responder a esta pergunta nos leva ao
conceito de campo elétrico. Seguimos a apresentação de :cite:`griffiths1999`. Nós podemos
definir o campo elétrico de uma carga arbitrária :math:`Q` como a força
experimentado por uma carga unitária :math:`q` devido a :math:`Q`

.. math::
       \mathbf{e} = \frac{\mathbf{F}}{q}.
       :label: Force_per_q

Dividindo os dois lados da lei de Coulomb por :math:`q` e substituindo o
definição de :math:`\ mathbf {e}`, obtemos que o campo elétrico de uma
carga pontual :math:`Q` é

.. math::
      \mathbf{e}(\mathbf{r}) = \frac{Q}{4\pi\varepsilon_0 |\mathbf{r} - \mathbf{r'}|^2}~\mathbf{\hat{\underline{r}}}\;.
      :label: e_charge_q

É importante notar aqui que o campo elétrico obedece ao princípio de
superposição, o que significa que o campo elétrico de uma coleção arbitrária de
cargas pontuais são iguais à soma dos campos elétricos devido a cada
carga individual.

.. math::
   \mathbf{e}\left(\sum_{k=1,n} Q_i\right) = \sum_{k=1,n} \mathbf{e}(Q_i)
   :label:

Se considerarmos o campo elétrico devido a um corpo espacialmente estendido com
densidade de carga :math:`\rho`, a soma torna-se uma integral sobre o infinitesimal
elementos de volume do corpo

.. math::
  \mathbf{e} = \frac{1}{4\pi\varepsilon_0}\int_V \frac{\rho}{|\mathbf{r} - \mathbf{r'}|^2}\;~\mathbf{\hat{\underline{r}}}\;\mathrm{d}v,
  :label: e_charge_den

onde :math:`|\mathbf{r} - \mathbf{r'}|` agora é a distância de um ponto em
o corpo carregado até o ponto em que o campo elétrico deve ser avaliado.
A integral está sobre o corpo carregado.

Podemos mostrar :eq:`e_charge_den` é equivalente a lei de Gauss diretamente da definição de divergência,

.. math::
  \boldsymbol{\nabla} \cdot \mathbf{e} = \underset{\Delta V \rightarrow 0}{lim} ~\frac{1}{\Delta V} \oint_{S} \mathbf{e}~da,
  
onde a integral é sobre :math:`S`,  a superfície fechada limitando o volume
:math:`\Delta V`. Aplicando esta definição para o campo elétrico de uma carga pontual :math:`q` na origem temos

.. math::
   \boldsymbol{\nabla} \cdot \mathbf{e} = \underset{\Delta V \rightarrow 0}{lim} \left[ \frac{1}{\Delta V}\frac{q}{4\pi\varepsilon_0 |\mathbf{r} - \mathbf{r'}|^2} \oint_{S} ~da \right].

Tomando :math:`\Delta V` como o raio de uma esfera fechada de raio :math:`|\mathbf{r} -
\mathbf{r'}|` centrada na origem, podemos facilmente avaliara a integral,
dando
   
.. math::
  \boldsymbol{\nabla} \cdot \mathbf{e} &=  \underset{\Delta V \rightarrow 0}{lim} \left[ \frac{1}{\Delta V} \frac{4 \pi |\mathbf{r} - \mathbf{r'}|^2\;q }{4\pi\varepsilon_0 |\mathbf{r} - \mathbf{r'}|^2} \right ] 
  
  ~ &=  \underset{\Delta V \rightarrow 0}{lim} \left[ \frac{1}{\Delta V} \frac{q}{\varepsilon_0} \right ]. 

No limite :math:`\Delta V \rightarrow 0`, :math:`\frac{q}{\Delta V}` é
simplesmente a densidade de carga :math:`\rho`. Isto estabelece o resultado desejado

.. math::
   \boldsymbol{\nabla} \cdot \mathbf{e} = \frac{\rho}{\varepsilon_0}.

Para uma discussão mais detalhada, consulte a página 36 de :cite:`fleisch2008`. Para uma
derivação alternativa e discussão, consulte as páginas 65-70 de :cite:`griffiths1999`.
