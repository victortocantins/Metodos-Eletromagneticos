.. _frequency_domain_electric_dipole_index:

Dipolo de Corrente Elétrica Harmônico
=====================================


.. Purpose::

    No domínio da frequência, consideramos os campos elétricos e magnéticos harmônicos.
    Aqui, fornecemos uma descrição física do dipolo de corrente elétrica harmônico.
    Isso é usado para desenvolver uma expressão matemática que pode ser usada para substituir o termo de fonte elétrica nas equações de Maxwell.


**Deifinição Geral**


.. figure:: images/E_source_current_dipole.png
		:align: right
		:figwidth: 50%
		:name: CurrentWire

        	Representação física da fonte dipolo de corrente elétrica harmônica onde :math:`\mathbf{p}` = 1 Am.


O dipolo de corrente elétrica harmônica pode ser pensado como um comprimento infinitesimal de fio que carrega uma corrente harmônica.
A força da fonte é, portanto, definida por um momento de dipolo harmônico :math:`\mathbf{p}(\omega)`.
Para um dipolo de corrente harmônica definido por comprimento :math:`ds` e corrente harmônica :math:`\mathbf{I} (\omega)=\mathbf{I}e^{i\omega t}`, o momento de dipolo é dado por:


.. math::
	\mathbf{p}(\omega) = \mathbf{p} \, e^{i\omega t} = \mathbf{I} ds \, e^{i\omega t}
	:label: p_harmonic_def

onde :math:`\mathbf{p} = \mathbf{I}ds` é a amplitude do vetor do momento de dipolo.
Ao formular as equações de Maxwell no domínio da frequência, :math:`e^{i\omega t}` é geralmente suprimido.
Como resultado, o termo fonte para o dipolo de corrente elétrica harmônica é dado por:


.. math::
	\mathbf{J_e^s} = \mathbf{I}ds \, \delta (x) \delta (y) \delta (z)
	:label: Je_harmonic_def


onde :math:`\delta (x)` é a função delta de Dirac.
Ao incluir o termo fonte, as equações de Maxwell no domínio da frequência são dadas por:

.. math::
	\begin{split}
	&\nabla \times \mathbf{E_e} + i \omega \mu \mathbf{H_e} = 0  \\
	\nabla \times \mathbf{H_e} - & (\sigma  + i\omega \varepsilon ) \mathbf{E_e} = \mathbf{I}ds \, \delta(x) \delta(y) \delta(z)
	\end{split}
	:label: p_Maxwells_harmonic


onde subscritos :math:`_e` nos lembra que estamos considerando uma fonte elétrica.
A fonte de corrente é responsável por gerar uma densidade de corrente primária (e, portanto, um campo elétrico) na região circundante (:numref:`ElecDipole`). No entanto, a :ref:`equação Ampere-Maxwell<ampere_maxwell_differential_frequency>` afirma que os campos elétricos harmônicos, bem como as correntes livres, geram campos magnéticos. Além disso, a natureza harmônica dos campos magnéticos deve produzir campos elétricos secundários de acordo com :ref:`Lei de Faraday<faraday_differential_frequency>`.


**Organização**

Na seção a seguir, resolvemos as equações de Maxwell para uma fonte dipolo de corrente elétrica harmônica e fornecemos expressões analíticas para os campos elétrico e magnético em um meio homogêneo. Expressões assintóticas são então fornecidas para vários casos.
Ferramentas de modelagem numérica são disponibilizadas para investigar a dependência dos campos elétricos e magnéticos em vários parâmetros.


.. toctree::
    :maxdepth: 2

    analytic_solution
    asymptotics
    fields

