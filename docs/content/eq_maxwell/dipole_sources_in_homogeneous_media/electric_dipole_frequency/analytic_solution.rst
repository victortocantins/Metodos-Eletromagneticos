.. _frequency_domain_electric_dipole_analytic_solution:

Solução Analítica
=================

.. Purpose::

    Aqui, as equações de Maxwell são resolvidas para uma fonte dipolo de corrente elétrica harmônica.
    Isso é realizado usando o método dos potenciais de Schelkunoff, conforme mostrado em Ward e Hohmann (:cite:`ward1988`).
    Expressões analíticas para o campo elétrico, o campo magnético e o potencial vetorial correspondente são fornecidas.
    :ref:`Ferramentas de modelagem numérica<frequency_domain_electric_dipole_fields>` para visualizar os campos são fornecidas após a seção 
    :ref:`asymptotics <frequency_domain_electric_dipole_asymptotics>`.


Para uma fonte de corrente elétrica (:math:`\mathbf{J_e^s}`), As equações de Maxwell no domínio da frequência são dadas por:

.. math::
	\nabla \times \mathbf{E_e} + i\omega \mu \mathbf{H_e} = 0 
	:label: Faraday_e
.. math::
	\nabla \times \mathbf{H_e} - (\sigma + i\omega \varepsilon) \mathbf{E_e} = \mathbf{J}_e^s 
	:label: Ampere_e

onde subscritos :math:`_e` nos lembra que estamos considerando uma fonte elétrica.
Para uma fonte de corrente elétrica (:math:`\mathbf{J_e^s}`), os campos elétricos e magnéticos podem ser expressos em termos do potencial do vetor Schelkunoff (:math:`\mathbf{A}`), onde:
	
.. math::
	\mathbf{H_e} \equiv \nabla \times \mathbf{A} 
	:label: H_A_potential

e

.. math::
	\mathbf{E}_e = -i\omega\mu\mathbf{A} + \frac{1}{(\sigma + i\omega\varepsilon)} \nabla (\nabla \cdot \mathbf{A})
	:label: E_A_potential


A Equação :eq:`H_A_potential` pode ser obtida simplesmente tomando a divergência da Equação :eq:`Faraday_e`.
A Equação :eq:`E_A_potential` é obtida pela manipulação das Equações :eq:`Faraday_e`, :eq:`Ampere_e` e :eq:`H_A_potential`, e
e escolher um medidor apropriado
Podemos ver das Equações :eq:`H_A_potential` e :eq:`E_A_potential` que :math:`\mathbf{A}` contém todas as informações correspondentes aos campos elétricos e magnéticos.
Portanto, as equações de Maxwell serão manipuladas para resolver para :math:`\mathbf{A}`; que pode então ser usado para obter :math:`\mathbf{E_e}` e
:math:`\mathbf{H_e}`.

Ao manipular as Equações :eq:`Faraday_e`, :eq:`Ampere_e` e :eq:`H_A_potential` e escolhendo um medidor apropriado, descobrimos que 
:math:`\mathbf{A}` pode ser expresso usando a equação de Helmholtz:


.. math::
	\nabla^2 \mathbf{A} + k^2 \mathbf{A} = - \mathbf{J}_e^s, \  \  \  \  \text{where} \  \  k^2 = \omega^2\mu\epsilon -i\omega\mu\sigma
	:label: Helmholtz_A 

A equação de Helmholtz com condições de contorno pode ser resolvida para gerar :math:`\mathbf{A}`.
Para o meio infinito, a condição de limite é tal que :math:`\mathbf{A} \rightarrow 0` quando :math:`r \rightarrow \infty`.
A partir da equação de Helmholtz, podemos ver que :math:`\mathbf{A}` terá apenas um componente ao longo da direção de :math:`\mathbf{J_e^s}`.
A função escalar de Green para a equação de Helmholtz é:

.. math::
	G(r) = \frac{e^{-ikr}}{4\pi r}.
	:label: GreensFncFullSpace

e, portanto, o potencial vetorial para uma fonte de corrente elétrica arbitrária é:

.. math::
	\mathbf{A}(\mathbf{r}) = \int_{V^\prime} \frac{e^{-ik|\mathbf{r}-\mathbf{r}'|}}{4\pi |\mathbf{r}-\mathbf{r}'|} \mathbf{J_e^s}(\mathbf{r}') dV^\prime
	:label: A_Potential

onde :math:`\mathbf{r}` é o local de observação, :math:`\mathbf{r^\prime}` refere-se a locais dentro da região de origem e :math:`V^\ prime` é o volume de a região de origem.
Para um dipolo de corrente elétrica orientado na direção :math:`\mathbf{\hat{x}}`, o termo fonte é dado por:

.. math::
	\mathbf{J_e^s} = \mathbf{\hat{x}} I ds \delta(x) \delta(y) \delta(z)
	:label: Je_x

e a solução para a Equação :eq:`A_Potential` é:

.. math::
	\mathbf{A} = \frac{I ds}{4\pi r} e^{-ikr} \mathbf{\hat{x}}
	:label: A_Potential_for_Je_x

Lembre-se de que :math:`\mathbf{A}` pode ser usado para obter o campo elétrico e magnético de acordo com as Equações :eq:`H_A_potential` e 
:eq:`E_A_potential`.
Assim, o campo elétrico para um dipolo de corrente elétrica na direção :math:`\mathbf{\hat x}` é:

.. math::
	\mathbf{E_e} = \frac{I ds}{4 \pi (\sigma + i \omega \varepsilon)} \left[ \left( k^2 + \frac{\partial^2}{\partial x^2} \right) \mathbf{\hat{x}} + \frac{\partial^2}{\partial x \partial y} \mathbf{\hat{y}} + \frac{\partial^2}{\partial x \partial z} \mathbf{\hat{z}} \right] \frac{e^{-ikr}}{r}

que é igual a:

.. math::
	\begin{split}
	\mathbf{E_e} = \frac{I ds}{4 \pi (\sigma + i \omega \varepsilon) r^3} e^{-ikr} \Bigg [ \Bigg ( \frac{x^2}{r^2} \mathbf{\hat{x}} + & \frac{xy}{r^2} \mathbf{\hat{y}} + \frac{xz}{r^2} \mathbf{\hat{z}} \Bigg ) ... \\
	&\big ( -k^2 r^2 + 3ikr +3 \big ) + \big ( k^2 r^2 - ikr -1 \big ) \mathbf{\hat{x}} \Bigg ] .
	\end{split}
	:label: E_Cartesian

O campo magnético é:

.. math::
	\mathbf{H_e} = \frac{I ds}{4 \pi} \left[ \frac{\partial}{\partial z} \mathbf{\hat{y}} - \frac{\partial}{\partial y} \mathbf{\hat{z}} \right] \frac{e^{-ikr}}{r}

que é igual a:

.. math::
	\mathbf{H_e} = \frac{I ds}{4 \pi r^2} \left( ikr + 1 \right) e^{-ikr} \left( -\frac{z}{r} \mathbf{\hat{y}} + \frac{y}{r} \mathbf{\hat{z}} \right) .
	:label: H_Cartesian


A seguir, mostramos como as Equações :eq:`E_Cartesian` e :eq:`H_Cartesian` pode ser simplificados para vários casos.

