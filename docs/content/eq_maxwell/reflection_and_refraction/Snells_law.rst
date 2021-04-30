.. _Snells_law:

Reflexão e Lei de Snell
=======================

.. purpose::

    Aqui, derivamos os ângulos de propagação das ondas refletidas e refratadas em uma interface horizontal. A lei de Snell é então usada para caracterizar o ângulo de refração em termos do número de onda complexo para ambos os meios.

Setup
-----

Aqui, consideraremos a reflexão e a refração de uma onda plana uniforme, linearmente polarizada e homogênea em uma interface horizontal 
(:numref:`snells_law_setup`). A onda incidente está confinada ao plano xz. A interface é denotada por :math:`S`, tem um vetor normal 
:math:`\mathbf{\hat n}` e separa dois meios homogêneas com propriedades físicas :math:`\sigma_1`, :math:`\mu_1`, :math:`\epsilon_1` e :math:`\sigma_2`, 
:math:`\mu_2`, :math:`\epsilon_2`.

Para a configuração em :numref:`snells_law_setup`, a onda incidente (:math:`k_i`) chega no ângulo :math:`\theta_i`. Uma vez que esta onda atinge a interface, ela se divide em duas partes, uma onda refletida (:math:`k_r`) e uma onda transmitida (:math:`k_t`). A onda transmitida experimenta uma mudança na direção de propagação, portanto é uma onda refratada. As ondas refletidas e refratadas viajam em direções caracterizadas por ângulos :math:`\theta_r` e 
:math:`\theta_t`, respectivamente.    

.. figure:: images/snellslaw_setup.png
   :align: center
   :figwidth: 70%
   :name: snells_law_setup

   Geometria para lei de Snell. Modificada de :cite:`ward1988` Figure 3.1.


.. _Snells_law_derive:

Lei de Snell, Reflexão e Refração
-----------------------------------

Os ângulos de reflexão e refração (:math:`\theta_r` e :math:`\theta_t`) podem ser derivados considerando o campo elétrico ou o campo magnético transportado pela onda EM incidente. Aqui, derivaremos esses ângulos considerando um campo elétrico. As respectivas ondas incidentes, refletidas e refratadas são dadas por:

.. math::
	\mathbf{E_i} = \mathbf{E_{i,0}} \, e^{-i \mathbf{k_i \cdot r}}, \;\;\; \mathbf{E_r} = \mathbf{E_{r,0}} \, e^{-i \mathbf{k_r \cdot r}}, \;\;\; \textrm{e} \;\;\; \mathbf{E_t} = \mathbf{E_{t,0}} \, e^{-i \mathbf{k_t \cdot r}}
	:label:

onde :math:`\mathbf{k}` é o vetor da onda (vetor de Poynting) para cada onda e:

.. math::
	\mathbf{E \times H} = \mathbf{k}
	:label:

Dentro das leis formativas, discutimos as :ref:`condições de interface<maxwell1_fundamentals_interface_conditions_index>` necessárias para campos elétricos e magnéticos. Elas afirmam que os componentes do campo elétrico paralelo à superfície :math:`S` devem ser iguais em toda a interface. Como resultado:

.. math::
	\mathbf{\hat n} \times \big ( \mathbf{E_i} + \mathbf{E_r} \big ) = \mathbf{\hat n} \times \mathbf{E_t}
	:label:

Usando as três expressões anteriores, encontramos:

.. math::
	\theta_i = \theta_r
	:label: eq_reflected

e

.. math::
	k_i \, \textrm{sin}\theta_i = k_t \, \textrm{sin}\theta_t
	:label: eq_Snells_law

De acordo com a Equação :eq:`eq_reflected`, o ângulo refletido e o ângulo incidente em relação a :math:`\mathbf{\hat n}` são os mesmos. A Equação 
:eq:`eq_Snells_law` é conhecido como **Lei de Snell **. A lei de Snell define o ângulo de refração correspondente à onda transmitida. Assim, dependendo das propriedades físicas de cada meio, a onda transmitida pode ser refratada tanto na vertical quanto na horizontal.

.. _Snells_law_Snells_law:

Aproximações para a Lei de Snell
--------------------------------

A definição mais comum da lei de Snell é dada por:

.. math::
	k_1 \, \textrm{sin}\theta_1 = k_2 \, \textrm{sin}\theta_2
	:label: eq_Snells_law_2

em que :math:`k_1` é o número de onda para a onda incidente com ângulo :math:`\theta_1` e :math:`k_1` é o número de onda da onda refratada com ângulo
:math:`\theta_2`. Aqui, discutimos algumas prpriedades da lei de Snell..

**Regime Quase Estático**

No regime quase estático (:math:`\sigma \gg \omega \varepsilon`), o número de onda torna-se:

.. math::
	k \approx \sqrt{-i \omega \mu \sigma}
	:label:

Neste caso a lei de Snell se reduz para:

.. math::
	\sqrt{\mu_1 \sigma_1} \, \textrm{sin}\theta_1 = \sqrt{\mu_2 \sigma_2} \, \textrm{sin} \theta_2


**Regime de Onda**

No regime de onda (:math:`\sigma \ll \omega \varepsilon`), o número de onda se torna:

.. math::
	k \approx w \sqrt{\mu \varepsilon}
	:label:

onde a velocidade da onda é dada por:

.. math::
	V = \frac{1}{\sqrt{\mu \varepsilon}}
	:label:

Usando as duas expressões anteriores, a lei de Snell no regime de ondas torna-se:

.. math::
	\frac{V_1}{V_2} = \frac{sin \theta_1}{sin \theta_2}
	:label: eq_Snells_law_3

Nesse caso, o ângulo de incidência e refração estão diretamente relacionados à velocidade de propagação das ondas EM em cada meio. Esta relação é especialmente importante quando se considera :ref:`radar de penetração no solo<gpr_index>`.






