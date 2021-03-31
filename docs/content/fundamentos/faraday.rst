.. _faraday:

Lei de Faraday
==============

.. raw:: html

  <iframe src="https://phet.colorado.edu/sims/html/faradays-law/latest/faradays-law_en.html" width="700" height="525" scrolling="no" allowfullscreen></iframe>

Podemos observar várias características da indução EM usando o miniaplicativo:

1) O voltímetro só registra um sinal quando o ímã está se movendo, independentemente de sua posição absoluta.
2) O sinal da tensão induzida muda dependendo da direção do movimento e orientação do ímã
3) A magnitude da tensão depende de quão rápido o ímã está se movendo
4) Se todo o resto for igual, a tensão induzida no circuito de quatro bobinas é maior do que no circuito de duas bobinas.

Esses comportamentos são descritos pela lei de Faraday.
A lei de Faraday leva o nome do cientista inglês Michael Faraday (1791-1867),
e descreve a maneira pela qual os campos magnéticos variáveis no tempo induzem o
campos elétricos rotacionais. Isso explica a indução eletromagnética
fenômeno, que é um mecanismo de excitação fundamental da fonte indutiva.

    .. figure:: ./images/IntFaradayDiagram.png
        :align: center
        :scale: 50%

.. _faraday_integral_time:

Forma Integral no Domínio do Tempo
----------------------------------

A lei de Faraday na forma integral pode ser expressa usando a seguinte equação:

.. math::
    \oint_C {\bf e} \cdot {\bf d}{\bf l}  = - \int_S \frac{\partial {\bf b}}{\partial t} \cdot \hat {\bf n} \, da,
    :label: faradays_law_int_time

onde:

- :math:`\mathbf{e}` é o campo elétrico definido em torno de um caminho fechado :math:`C`
- :math:`\mathbf{b}` é a densidade do fluxo magnético definida sobre uma superfície fechada :math:`A` contornada por :math:`C`
- :math:`\hat n` é um vetor unitário normal externo perpendicular a :math:`da`
- :math:`\ d\mathbf{l}` é um elemento vetorial de comprimento ao longo do contorno :math:`C`

A equação :eq:`faradays_law_int_time` afirma que a taxa de variação dependente do tempo no fluxo magnético, através de uma superfície limitada por um caminho fechado, é negativamente proporcional à integral de linha do campo elétrico que induz ao longo desse caminho.

.. _faraday_differential_time:

Forma Diferencial no Domínio do Tempo
-------------------------------------

Ao aplicar o teorema de Stokes ao lado esquerdo da Equação
:eq:`faradays_law_int_time`, obtemos a forma diferencial de lei de Faraday:

.. math::
    \nabla \times {\bf e} = - \, \frac{\partial {\bf b}}{\partial t}
    :label: faradays_law_diff_time

.. Therefore, the time dependent change in magnetic flux density at any location is negatively proportional to the curl of the electric field.
.. For magnetic fields which change rapidly with respect to time, we expect to observe a larger electric field.
.. TODO: Put some links: rotational field

A equação :eq:`faradays_law_diff_time` afirma que campos magnéticos variáveis com o tempo
induz campos elétricos rotacionais. Além disso, o rotacional dos campos elétricos induzidos 
se opõem às mudanças dependentes do tempo no campo magnético indutor.

.. _faraday_differential_frequency:

Lei de Faraday no Domínio da Frequência
---------------------------------------

A representação no domínio da frequência da lei de Faraday pode ser obtida por
aplicando uma transformada de Fourier às Equações :eq:`faradays_law_int_time` e
:eq:`faradays_law_diff_time`. A forma integral da Lei de Faraday no
domínio da frequência é:

.. math::
    \oint_C {\bf E} \cdot d{\bf l} = - \, i \omega \int_A {\bf B} \cdot \hat n \, da
    :label: faradays_law_int_freq

Similarmente o teorema de Stokes, a forma diferencial da lei de Faraday's é:

.. math::
    \nabla \times {\bf E} = - \, i \omega {\bf B}
    :label: faradays_law_diff_freq

onde :math:`\omega` é a frequência ângular, :math:`{\bf E}` é o campo elétrico dependente da Frequência 
e :math:`{\bf B}` é a densidade de fluxo magnético dependente da frequência the frequência

.. Seogi: This is not very intuitive so possibly omit
.. From a theoretical perspective, it is common practice to consider :math:`{\bf E}` and :math:`{\bf B}` as sinusoidal functions.

Da equação :eq:`faradays_law_diff_freq`, podemos inferir duas coisas:

1. Os campos elétricos rotacionais induzidos são proporcionais à frequência angular; isso implica que a indução eletromagnética é maior em frequências mais altas.
2. Os campos elétricos rotacionais induzidos e os campos magnéticos dependentes da frequência responsáveis por eles estão 90 graus defasados.

.. that sinusoidal magnetic fields characterized by higher frequencies will result in stronger electric fields.
.. Seogi: I possibly need better wording about this.
.. We can see from Eq. :eq:`faradays_law_diff_freq` that sinusoidal magnetic fields characterized by higher frequencies will result in stronger electric fields.
.. , :math:`{\bf E}` is the frequency-dependent electric field and :math:`{\bf B}` is the frequency-dependent magnetic flux density.

Descoberta da Lei de Faraday
----------------------------

A lei de Faraday é melhor compreendida usando três experimentos, que Faraday
conduzido e resumido em 1831. Para cada um desses experimentos, um
eletroímã foi usado para criar um campo magnético dependente do tempo, que nós
irá representar usando a densidade de fluxo magnético :math:`{\bf{b}}`. Um loop de
fio com área :math:`A`, contornado por um caminho fechado :math:`C`, foi então realizada
na proximidade do eletroímã. Isso resultou em um fluxo magnético
:math:`{\boldsymbol\Phi_b}` definido por: s

.. math::
    {\boldsymbol \Phi_b} = \int_A {\bf b} \cdot \hat {\bf{n}} \, da
    :label: magnetic_flux_time

Faraday então conduziu os três experimentos a seguir:

1. A alça de fio foi bloqueada enquanto o eletroímã permaneceu estacionário.
2. O eletroímã foi movido enquanto a alça de fio permanecia estacionária.
3. Tanto a alça do fio quanto o eletroímã permaneceram estacionários, entretanto, a intensidade do campo magnético variou em função do tempo.

Faraday notou que em todos os três experimentos, uma força eletromotriz
:math:`\mathcal{E}` foi induzido no fio, resultando em uma corrente elétrica mensurável. 
A força eletromotriz :math:`\mathcal{E}` pode ser definida
em termos de campo elétrico :math:`{\bf e}` integrando ao longo do caminho de
o fio da seguinte forma:

.. math::
    \mathcal{E} = - \oint_C {\bf e} \cdot d{\bf l} = V
    :label: electromotive_force_time
    
Em um circuito ideal, a força eletromotriz é equivalente à tensão
:math:`V` experimentado pelo fio. Para um circuito com resistência :math:`R`,
a Lei de Ohm :math:`V = IR` pode ser usada para mostrar que as forças eletromotrizes são
associado com correntes :math:`I`. A descoberta de Faraday veio ao propor
que uma mudança dependente do tempo no fluxo magnético através do loop do fio foi
responsável pela força eletromotriz resultante. Em 1833, Heinrich Lenz
determinou que a mudança dependente do tempo no fluxo magnético foi negativamente
proporcional à força eletromotriz que gerou. As contribuições feitas
por Faraday e Lenz são representados pela seguinte equação:

.. math::
    \mathcal{E} = - \, \frac{\partial {\boldsymbol \Phi_b}}{\partial t}
    :label: faraday_lenz_time

A contribuição de Lenz para a descoberta de Faraday não só fornece a igualdade na
Equação :eq:`faraday_lenz_time`, mas determina a direção da força sobre as cargas livres
em resposta a mudanças em um campo magnético aplicado. Para descrição mais completa veja a página
:ref:`lenz`. Substituindo a definição de fluxo magnético da Equação :eq:`magnetic_flux_time` e 
a definição de força eletromotriz da Equação :eq:`electromotive_force_time` na Equação 
:eq:`faraday_lenz_time`, podemos obter a lei de Faraday na forma integral
de acordo com a Equação :eq:`faradays_law_int_time`.


Unidades
--------

+--------------------------------+--------------------+----------------------------+---------------------------------------+
| Densidade de fluxo magnético   | :math:`\mathbf{b}` | :math:`\frac{\text{Wb}}    |  Weber por metro quadrado             |
|                                |                    | {\text{m}^{2}}`            |                                       |
+--------------------------------+--------------------+----------------------------+---------------------------------------+
| Densidade de corrente elétrica | :math:`\mathbf{j}` | :math:`\frac{\text{A}}     |                                       |
|                                |                    | {\text{m}^{2}}`            |  Ampere por metro quadrado            |
+--------------------------------+--------------------+----------------------------+---------------------------------------+
| Intensidade de campo elétrico  | :math:`\mathbf{e}` | :math:`\frac{\text{V}}     |                                       |
|                                |                    | {\text{m}}`                | Volt por metro                        |
+--------------------------------+--------------------+----------------------------+---------------------------------------+
| Potencial elétrico             | :math:`\text{V}`   | V                          | Volt                                  |
+--------------------------------+--------------------+----------------------------+---------------------------------------+
| Força eletromotriz             | :math:`\mathcal{E}`| V                          | Volt                                  |
+--------------------------------+--------------------+----------------------------+---------------------------------------+
| Corrente elétrica              | :math:`\text{I}`   | A                          | Ampere                                |
+--------------------------------+--------------------+----------------------------+---------------------------------------+

Considere as unidades das quantidade nos lados esquerdo e direito da Equação
:eq:`faradays_law_int_time`. Usando anáçise dimensional, obtemos:

.. math::
	V = \frac{Wb}{s}

.. TODO: parapharase this (I copy and paste wiki)

Portanto, a expressão acima afirma que uma mudança no fluxo magnético, igual a
1 Weber por segundo, irá induzir uma força eletromotriz de 1 Volt ao longo de um
caminho fechado. Usando a expressão acima mencionada, o Weber (:math:`Wb`) pode
ser expresso como:

.. math::
	Wb = V \cdot s = \frac{J}{A},

onde :math:`J` é o Joule, e :math:`A` é Ampere.
Joules são usados para representar uma unidade de energia, ou trabalho.
Assim, podemos interpretar o fluxo magnético como uma unidade de trabalho por unidade de corrente.

Aplicações da Lei de Faraday na Geofísica
-----------------------------------------


Ao realizar levantamentos eletromagnéticas, vários instrumentos são usados ​​para
gerar campos magnéticos dependentes do tempo. Esses campos são comumente chamados de
campos primários. De acordo com as Equações :eq:`faradays_law_diff_time`, isso vai
induzir campos elétricos rotacionais dentro da região circundante. Para uma rocha 
definida pela condutividade :math:`\sigma`, lei de Ohm (:math:`{\bf j} =\sigma{\bf e}`) 
implica que uma densidade :math:`{\bf j}` também é induzida pelo campo primário. 
Essas correntes induzidas são paralelas a :math:`{\bf e}`, e tem uma magnitude que depende da 
propriedade física da rocha. Portanto, podemos usar a lei de Faraday na forma diferencial
para compreender a maneira pela qual as correntes rotacionais são induzidas em
objetos condutores, por um campo primário gerado artificialmente.

De acordo com a seção da lei de Biot-Savart :ref:`biot_savart`, densidades de corrente
são responsáveis ​​pela geração de campos magnéticos. Isso implica que as correntes
induzida pelo campo primário resultará na criação de uma anomalia
campo magnético, comumente referido como o campo secundário. O secundário
campo pode ser medido em locais acima da superfície da Terra e fornece
informações importantes sobre estruturas geológicas de subsuperfície. Mas como é
o campo secundário medido?

Se colocado em uma região onde os campos secundários são observáveis, um loop receptor
do fio experimentará uma força eletromotriz de acordo com a Equação :eq:`faraday_lenz_time`. 
Da Equação :eq:`electromotive_force_time`, sabemos que a força eletromotriz é equivalente a 
tensão sendo induzida no fio. Portanto, podemos usar medições da tensão para representar informações
em relação ao campo secundário, ao invés de medir o campo diretamente.

A explicação fornecida nesta seção também pode ser entendida no
domínio da frequência. No entanto, as tensões induzidas dentro das bobinas receptoras
têm componentes reais (em fase) e imaginárias (fora de fase).

