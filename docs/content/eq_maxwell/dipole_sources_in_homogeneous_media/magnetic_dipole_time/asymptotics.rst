.. _time_domain_magnetic_dipole_asymptotics:

Aproximações Assintóticas
=========================

.. purpose::

    Aqui, expressões simplificadas para os campos elétricos e magnéticos são apresentadas para vários casos.
    Examinando expressões simplificadas, podemos ver mais facilmente como os campos dependem de certos parâmetros.
    Como a solução analítica completa para o potencial do vetor é bastante simples, aproximações assintóticas não são apresentadas aqui.
    

Campo Próximo/Tempos Tardios
----------------------------

Para campos que estão muito próximos da fonte de dipolo magnético, ou em momentos suficientemente tardios:

.. math::
	\theta r = \Bigg ( \frac{\mu \sigma}{4t} \Bigg )^{1/2} r \ll 1
	:label: theta_nearfield_latetime_mag


Como resultado, as funções exponencial e de erro podem ser aproximadas usando a expansão de Taylor, onde:

.. math::
	e^{-\theta^2 r^2} \approx 1 - \theta^2 r^2 + \frac{1}{2}\theta^4 r^4 + \; ...
	:label: Taylor_expansion_exp_mag

e

.. math::
	\textrm{erf}(\theta r) = \frac{2}{\sqrt{\pi}} \theta r - \frac{2}{3 \sqrt{\pi}}\theta^3 r^3 + \frac{1}{5\sqrt{\pi}}\theta^5 r^5 + \; ...
	:label: erfc_approximation_mag


Substituindo a série de Taylor acima nas :ref:`expressões analíticas<frequency_domain_magnetic_dipole_analytic_solution>` para :math:`{\bf e_m}` e 
:math:`{\bf h_m}`, podemos obter campo próximo/ aproximações tempos tardio.
No caso do campo elétrico, a aproximação de campo próximo/tempo-tardio é dada por:

.. math::
	{\bf e_m}(t) \approx \frac{2 m \theta^5}{\pi^{3/2} \sigma} \big ( -z \, \mathbf{\hat y} + y \, \mathbf{\hat z} \big )
	:label: e_nearfield_latetime_mag

De acordo com a Equação :eq:`e_nearfield_latetime`, o campo elétrico próximo/tempo-tardio decai proporcionalmente a :math:`t^{-5/2}`.
Para o campo magnético, a aproximação de campo próximo/tempo tardio é dada por:


.. math::
	{\bf h_m}(t) \approx \frac{2 m}{15 \pi^{3/2} r^3} \Bigg [ 3\, \theta^5 r^5 \Bigg ( \frac{x^2}{r^2}\mathbf{\hat x} + \frac{xy}{r^2}\mathbf{\hat y} + \frac{xz}{r^2}\mathbf{\hat z} \Bigg )  + \bigg ( 5\, \theta^3 r^3 - 6\, \theta^5 r^5 \bigg ) \mathbf{\hat x} \Bigg ]
	:label: h_nearfield_latetime_mag

De acordo com a Equação :eq:`h_nearfield_latetime`, as componentes :math:`\mathbf{\hat y}` e :math:`\mathbf{\hat z}` do campo magnético decai proporcionalmente  para :math:`t^{-5/2}`.
Para a componente :math:`\mathbf{\hat x}` entretanto, o termo :math:`\theta^3 r^3` permanece.
Como resulatado, a componete :math:`\mathbf{\hat x}` do campo decai proporcional a :math:`t^{-3/2}` apoós substituir tempo suficente.
A aproximação de campo próximo/tempo-tardio para a derivada de tempo do campo magnético é dada por:

.. math::
	\frac{\partial {\bf h_m}}{\partial t} \approx - \frac{4m \theta^5}{\pi^{3/2} \mu \sigma} \Bigg [ \theta^2 r^2 \Bigg ( \frac{x^2}{r^2}\mathbf{\hat x} + \frac{xy}{r^2}\mathbf{\hat y} + \frac{xz}{r^2}\mathbf{\hat z} \Bigg ) + \bigg ( 1 - 2\, \theta^2 r^2 \bigg ) \mathbf{\hat x}  \Bigg ]
	:label: dhdt_nearfield_latetime_mag

De acordo com as Equações :eq:`dhdt_nearfield_latetime`, :math:`\mathbf{\hat y}` e :math:`\mathbf{\hat z}` as componentes do campo decaem proporcional a 
:math:`t^{-7/2}`.
Na :math:`\mathbf{\hat x}` entretanto, os termos :math:`\theta^5 r^ 5` permanecem.
Como resultado, a componente :math:`\mathbf{\hat x}` do campo decai proporcionalmente a :math:`t^{-5/2}` após tempo suficiente.


Campo Distante
--------------


Para campos que estão longe da fonte do dipolo magnético, ou em tempos suficientemente iniciais:

.. math::
	\theta r = \Bigg ( \frac{\mu \sigma}{4t} \Bigg )^{1/2} r \gg 1
	:label: theta_farfield_mag

Neste caso, a exponencial e a função erro complementa, podem ser aproximadas como seguem:

.. math::
	e^{-\theta^2 r^2} \approx 0
	:label: exp_approximation_mag

e

.. math::
	\textrm{erfc}(\theta r) \approx 0
	:label: erfc_approximation_2_mag


Como resultado, não há aproximações assintóticas interessantes para o campo distante.





