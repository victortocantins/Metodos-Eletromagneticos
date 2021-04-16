.. _magnetic_permeability_lab_measurements:

Medidas de Laboratório
======================

As medições de permeabilidade magnética são parte integrante da classificação das propriedades físicas da rocha. 
Aqui, apresentamos a abordagem geral para medir a permeabilidade magnética de uma rocha. 
A teoria de fundo é então fornecida para uma configuração simplificada do instrumento.

Aproximação Geral
-----------------


.. figure:: ./images/figSuscMeasure.png
    :align: center
    :figwidth: 50%
    :name: figLCcircuit

    Diagrama do circuito elétrico representando uma configuração simplificada do instrumento. 
    O elemento indutivo :math:`L` depende da permeabilidade magnética da amostra :math:`\mu_s`.

As medições de permeabilidade magnética podem ser entendidas considerando o diagrama de circuito LC em série forçado em :numref:`figLCcircuit`. A corrente :math:`I(t)` dentro do fio é gerada por uma tensão motriz :math:`V(t)`. Esta corrente é definida pela seguinte equação diferencial ordinária:

.. math::
    \frac{d^2 I (t)}{d t} + \frac{1}{LC} I(t) = F(t)
    :label: Forced_Oscillator

Para o nosso circuito, o elemento indutivo :math:`L` depende da permeabilidade magnética :math:`\mu_s` da amostra de rocha. Esse relacionamento é discutido mais detalhadamente na seção seguinte. :math:`C` representa um elemento capacitivo conhecido, e :math:`F(t)` é usado para representar a tensão de acionamento. Da Equação :eq:`Forced_Oscillator`, o circuito tem uma frequência de ressonância natural :math:`\omega_r` em:

.. figure:: ./images/figPermeabilityVsRes.png
    :align: right
    :figwidth: 35%
    :name: figMuEmpirical
    
    Representação de uma curva derivada experimentalmente, para um determinado
    instrumento, que caracteriza uma relação empírica entre
    :math:`\mu_s` e :math:`\omega_r`.

.. math::
    \omega_r = \frac{1}{\sqrt{LC}}
    :label: Omega_Resonance

Uma vez que :math:`C` é conhecido, a Equação :eq:`Omega_Resonance` implica que existe uma relação explícita entre :math:`\omega_r` e :math:`\mu_s`. Infelizmente, essa relação não é particularmente direta e depende da configuração do instrumento.
Na maioria dos casos, uma curva derivada experimentalmente é usada para caracterizar uma relação empírica entre :math:`\omega_r` e :math:`\mu_s`. Uma vez estabelecida, a permeabilidade magnética de uma amostra pode ser obtida 1) determinando a frequência de ressonância do circuito, então 2) encontrando o valor de permeabilidade magnética correspondente na curva (:cite:`ClarkEmerson1991`). Isso é ilustrado em :numref:`figMuEmpirical`.

Teoria Básica: Um Experimento Simplificado
------------------------------------------

Mais uma vez, vamos considerar nosso circuito LC em série. Para medições de permeabilidade sensível, uma parte do fio é freqüentemente enrolada em torno de uma ferrita. As ferritas são não condutoras e extremamente permeáveis (:math:`\mu_{f} \sim 1000 \mu_0`). Como resultado, eles se tornam extremamente magnetizados quando expostos a um campo magnético, mas experimentam indução EM desprezível abaixo de 5 kHz (:cite:`ClarkEmerson1991`). A ferrita não forma um caminho fechado. Dentro do gap, uma rocha de permeabilidade magnética :math:`\mu_s` é colocada. O sistema bobina-ferrita atua como um elemento indutivo para o circuito e é denotado por :math:`L`. Assim, a corrente dentro do fio pode ser descrita usando a Equação 
:eq:`Forced_Oscillator`.


A tensão de condução :math:`V(t)` gera uma corrente :math:`I(t)` dentro do fio. Esta corrente cria um campo magnético :math:`H` dentro da bobina. Se o material dentro da bobina fosse condutivo, experimentaria uma força eletromotriz. Como as ferritas são puramente magnéticas, elas experimentam uma força magnetomotriz :math:`\mathcal{F}` em vez disso. Enquanto as forças eletromotrizes se opõem ao campo magnético, as forças magnetomotoras o reforçam. Ao negligenciar os efeitos de borda perto das extremidades da bobina, a força magnetomotriz experimentada pela ferrita é:

.. math::
    \mathcal{F} = NI = H \Delta S
    :label: MMF

onde :math:`N` é o número de voltas da bobina, e :math:`\Delta S` é o comprimento da bobina. Como as ferritas são tão permeáveis, 
elas se comportam como um circuito magnético neste caso. A força magnetomotriz aplicada gera um fluxo magnético :math:`\Phi`, 
que permeia o material. Isso pode ser descrito usando a lei de Hopkinson 
<https://en.wikipedia.org/wiki/Magnetic_circuit#Ohm's_law_for_magnetic_circuits>`__, que é análoga à lei de Ohm:

.. math::
    \mathcal{F} = \Phi \Re
    :label: Hopkinsons_Law
    
onde :math:`\Phi` é o fluxo magnético ao longo do caminho da ferrita, e :math:`\Re` é definido como a relutância magnética. A relutância magnética representa a razão entre a força magnetomotriz e o fluxo magnético induzido. Se nossa ferrita forma um caminho fechado, tem uma área transversal uniforme :math:`A`, e comprimento total :math:`\ell`, sua relutância magnética é dada por:

.. math::
    \Re = \frac{\ell}{\mu_f A}
    :label: Reluctance

Em nosso experimento, entretanto, há um gap contendo uma amostra de rocha. A introdução de uma amostra altera a relutância magnética do circuito 
(:cite:`ClarkEmerson1991`). Como elementos eletricamente resistivos, elementos magneticamente relutantes podem ser adicionados em série. 
Se a área da seção transversal permanecer constante:

.. math::
    \Re = \sum_k \frac{\ell_k}{\mu_k A}
    :label: Reluctance_No_Sample

A Equação :eq:`Reluctance_No_Sample` pode, portanto, ser usada para descrever a relutância magnética de nosso sistema na ausência de uma amostra de rocha. Quando uma amostra de rocha é colocada dentro do gap, ela afeta a relutância magnética. Na maioria dos experimentos de laboratório, a relutância magnética é dada por (:cite:`ClarkEmerson1991`):

.. math::
    \Re = \Re_0 + \frac{\alpha}{\mu_s}
    :label: Reluctance_Sample

onde :math:`\Re_0` e :math:`\alpha` podem ser determinados experimentalmente e dependem da geometria do instrumento. Por definição da auto-indutância e usando as Equações :eq:`Hopkinsons_Law` e :eq:`Reluctance_Sample`:

.. math::
    L = \frac{N \Phi}{I} = \frac{N \mathcal{F}}{I \Re} = \frac{N^2}{\Re}
    :label: Inductance

Portanto, a auto-indutância do circuito é inversamente proporcional à relutância magnética. Usando as Equações :eq:`Omega_Resonance`, 
:eq:`Reluctance_Sample` e :eq:`Inductance`, a permeabilidade magnética de uma amostra de rocha pode ser determinada pela seguinte expressão:

.. math::
    \mu_s = \frac{\alpha}{C (N \omega_r )^2 - \Re_0}
    :label: EqFinal


