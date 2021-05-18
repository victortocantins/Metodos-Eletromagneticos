.. _time_domain_electric_dipole_asymptotics:

Aproximações Assintóticas
=========================

.. topic:: Purpose

    Aqui, expressões simplificadas para os campos elétricos e magnéticos são apresentadas para vários casos.
    Examinando expressões simplificadas, podemos ver mais facilmente como os campos dependem de certos parâmetros.
    Como a solução analítica completa para o potencial do vetor é bastante simples, aproximações assintóticas não são apresentadas aqui.


Campo Próximo/ Tempos tardios
-----------------------------

Para campos que estão muito próximos da fonte de dipolo elétrico, ou em tempos suficientemente tardios:

.. math::
	\theta r = \Bigg ( \frac{\mu \sigma}{4t} \Bigg )^{1/2} r \ll 1
	:label: theta_nearfield_latetime

Nesse caso, as funções exponencial e de erro podem ser aproximadas usando a expansão de Taylor. Desse modo:

.. math::
	e^{-\theta^2 r^2} = 1 - \theta^2 r^2 + \frac{1}{2}\theta^4 r^4 + \; ...
	:label: Taylor_expansion_exp
	
e

.. math::
	\textrm{erf}(\theta r) =  \frac{2}{\sqrt{\pi}} \theta r - \frac{2}{3 \sqrt{\pi}}\theta^3 r^3 + \frac{1}{5\sqrt{\pi}} \theta^5 r^5 + \;...
	:label: erfc_approximation

Ao substituir as expansões de Taylor acima nas :ref:`soluções analíticas completas<time_domain_electric_dipole_analytic_solution>` para 
:math:`{\bf e_e}` e :math:`{\bf h_e}`, podemos obter a aproximações para tempos tardios de campo próximo. No caso do campo elétrico:
	

.. math::
	{\bf e_e}(t) \approx \frac{ Ids}{15 \pi^{3/2} \sigma r^3} \Bigg [ 6 \,\theta^5 r^5 \Bigg ( \frac{x^2}{r^2}\mathbf{\hat x} + \frac{xy}{r^2}\mathbf{\hat y} + \frac{xz}{r^2}\mathbf{\hat z} \Bigg )   + \Big ( 10 \,\theta^3 r^3 + 3 \,\theta^5 r^5 \Big ) \mathbf{\hat x} \Bigg ]
	:label: e_nearfield_latetime

De acordo com as Equações :eq:`e_nearfield_latetime`, :math:`\mathbf {\hat y}` e :math:`\mathbf{\hat z}` componentes do campo elétrico próximo/tardio decaem proporcional a :math:`t^{-5/2}`.
No entanto, os termos :math:`\theta^3 r^3` para a componente :math:`\mathbf{\hat x}` não são cancelados.
Portanto, a componente :math:`\mathbf{\hat x}` do campo elétrico decai proporcionalmente a :math:`t^{-3/2}` em tempos suficientemente atrasados.
Para o campo magnético, a aproximação de campo próximo/tempo tardio é dada por:

.. math::
	{\bf h_e}(t) \approx \frac{\theta^3 Ids}{3\pi^{3/2}} \big (-z \, \mathbf{\hat y} + y \, \mathbf{\hat z} \big ) 
	:label: h_nearfield_latetime

De acordo com a Equação :eq:`h_nearfield_latetime`, o campo elétrico de campo próximo/tempo tardio decai proporcionalmente a :math:`t^{-3/2} `.
Tomando a derivada da Equação :eq:`h_nearfield_latetime`, aproximação de campo próximo/tempo tardio para a derivada de tempo do campo magnético é dada por:


.. math::
	\frac{\partial {\bf h_e}}{\partial t} \approx \frac{2 \theta^5 Ids}{\mu \sigma \pi^{3/2}} \big ( z \, \mathbf{\hat y} - y \, \hat  z \big )
	:label: dhdt_nearfield_latetime

De acordo com a Equação :eq:`dhdt_nearfield_latetime`, a derivada do tempo do campo magnético decai proporcionalmente a :math:`t^{-5/2}`.

Campo Distante
--------------


Para campos que estão longe da fonte de dipolo de corrente elétrica, ou em tempos suficientemente grandes:

.. math::
	\theta r = \Bigg ( \frac{\mu \sigma}{4t} \Bigg )^{1/2} r \gg 1
	:label: theta_farfield

Neste caso, a exponencial e a função erro complementar pode ser aproximada como segue:

.. math::
	e^{-\theta^2 r^2} \approx 0
	:label: exp_approximation
	
e

.. math::
	\textrm{erfc}(\theta r) \approx 0
	:label: erfc_approximation_2

Como resultado, não há aproximações assintóticas interessantes para o campo distante.











