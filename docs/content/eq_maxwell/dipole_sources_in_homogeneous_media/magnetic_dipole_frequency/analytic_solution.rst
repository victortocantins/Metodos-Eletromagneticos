.. _frequency_domain_magnetic_dipole_analytic_solution:

Solução Analítica
=================

.. Purpose::

    Aqui, as equações de Maxwell são resolvidas para uma fonte dipolo magnética harmônica.
    Isso é realizado usando o método dos potenciais de Schelkunoff, conforme mostrado em Ward e Hohmann (:cite:`ward1988`).
    Expressões analíticas para o campo elétrico, o campo magnético e o potencial vetorial correspondente são fornecidas.
     



Para uma fonte magnética (:math:`\mathbf{J_m^s}`), as equações de Maxwell no domínio da frequência são dados por:


.. math::
	\nabla \times \mathbf{E_m} + i\omega \mu \mathbf{H_m} = - \mathbf{J_m^s}
	:label: Faraday_m
.. math::
	\nabla \times \mathbf{H_m} - (\sigma + i\omega \varepsilon) \mathbf{E_m} = 0
	:label: Ampere_m

onde os subscritos :math:`_m` nos lembram que estamos usando uma fonte magnética.
Para uma fonte magnética (:math:`\mathbf{J_m^s}`), os campos elétricos e magnéticos podem ser expressos em termos do potencial do vetor Schelkunoff 
(:math:`\mathbf{F}`), onde:

.. math::
	\mathbf{H}_m = -(\sigma + i \omega \varepsilon) \mathbf{F} + \frac{1}{(i \omega \mu)} \nabla (\nabla \cdot \mathbf{F})
	:label: H_F_potential


e

.. math::
	\mathbf{E}_m = - \nabla \times \mathbf{F}
	:label: E_F_potential


A Equação :eq:`E_F_potential` pode ser obtida simplemente tomando a divergência da Equação :eq:`Ampere_m`.
A Equação :eq:`H_F_potential` é obtida pela manipulção das Equações :eq:`Faraday_m`, :eq:`Ampere_m` e :eq:`E_F_potential`, e escolheno um calibre apropriado. 
Podemos ver das Equações :eq:`H_F_potential` e :eq:`E_F_potential` que :math:`\mathbf{F}` contém todas as informações correspondentes aos campos elétricos e magnéticos.
Portanto, as equações de Maxwell serão manipuladas para resolver para :math:`\mathbf{F}`; que pode então ser usado para obter :math:`\mathbf{E_m}` e 
:math:`\mathbf{H_m}`.

Ao manipular as Equações :eq:`Faraday_m`, :eq:`Ampere_m` e :eq:`E_F_potential` e escolhendo um calibre apropriado, descobrimos que :math:`\mathbf{F}` pode ser expresso usando a equação de Helmholtz:


.. math::
	\nabla^2 \mathbf{F} + k^2 \mathbf{F} = - \mathbf{J}_m^s, \  \  \  \  \text{where} \  \  k^2 = \omega^2\mu\varepsilon -i\omega\mu\sigma
	:label: Helmholtz_F

A equação de Helmholtz com condições de contorno pode ser resolvida para gerar :math:`\mathbf{F}`.
Para o meio infinito, a condição limite é tal que :math:`\mathbf{F} \rightarrow 0` quando :math:`r \rightarrow \infty`.
A partir da equação de Helmholtz, podemos ver que :math:`\mathbf{F}` terá apenas um componente ao longo da direção de :math:`\mathbf{J_m ^ s}`.
A função escalar de Green para a equação de Helmholtz é:

.. math::
	G(r) = \frac{e^{-ikr}}{4\pi r}.
	:label: GreensFncFullSpaceMag

e assim, o potencial vetor paara uma fonte magnética arbitrária é:

.. math::
	\mathbf{F}(\mathbf{r}) = \int_{V^\prime} \frac{e^{-ik|\mathbf{r}-\mathbf{r}'|}}{4\pi |\mathbf{r}-\mathbf{r}'|} \mathbf{J}_m^s (\mathbf{r}') dV^\prime
	:label: F_Potential

onde :math:`\mathbf{r}` é o vetor de observação, :math:`\mathbf{r^\prime}` refere-se a localizações dentro da região de origem e :math:`V^\prime` é o volume da região de origem. Para um dipolo magnético orientado na direção :math:`\mathbf{\hat x}`, o termo fonte é dado por:


.. math::
	\mathbf{J}_m^s = i \omega \mu I S \delta(x) \delta(y) \delta(z) \mathbf{\hat x}
	:label: Jm_x


e a solução para a Equação :eq:`F_Potential` é:

.. math::
	\mathbf{F} = \frac{i \omega \mu m}{4\pi r} e^{-ikr} \mathbf{\hat x}
	:label: F_Potential_for_Jm_x

Lembre-se de que :math:`\mathbf{F}` pode ser usado para obter o campo elétrico e magnético de acordo com as Equações :eq:`H_F_potential` e :eq:`E_F_potential`.
Assim, o campo elétrico para um dipolo magnético na direção :math:`\hat x` é:

.. math::
	\mathbf{E_m} = \frac{i \omega \mu m}{4 \pi r^2} \left( ikr + 1 \right) e^{-ikr} \left( -\frac{z}{r} \mathbf{\hat y} + \frac{y}{r} \mathbf{\hat z} \right).
	:label: Em_Cartesian


Enquanto o campo magnético é dado por:

.. math::
	\mathbf{H_m} = \frac{m}{4 \pi r^3} e^{-ikr} \left[ \left(\frac{x^2}{r^2} \mathbf{\hat x} + \frac{xy}{r^2} \mathbf{\hat y} + \frac{xz}{r^2} \mathbf{\hat z} \right) \left(-k^2 r^2 + 3ikr +3 \right) + \left(k^2 r^2 - ikr -1 \right) \mathbf{\hat x} \right].
	:label: Hm_Cartesian

Nas páginas seguintes, mostraremos como as Equações :eq:`Em_Cartesian` e :eq:`Hm_Cartesian` podem ser simplificdas para vários casos.




