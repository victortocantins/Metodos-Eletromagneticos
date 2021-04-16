.. _quick_guide_maxwell:

Visão Geral das Equações de Maxwell
===================================

.. purpose::
	
	Tendo fornecido o conjunto de :ref:`leis fundamentais<fundamentos_index>` para eletromagnetismo, apresentamos as quatro representações mais comuns das equações de Maxwell. 
	Esta página serve como um guia rápido. Para problemas específicos, pode ser benéfico começar a partir de formas menos comuns das equações de Maxwell. 
	Observe, entretanto, que todos os formulários podem ser derivados das expressões apresentadas aqui.

As equações de Maxwell são compostas de quatro :ref:`leis fundamentais<fundamentos_index>`; ie :ref:`Lei de Gauss para campos elétricos<gauss_electric>`, 
:ref:`Lei de Gauss para campos magnéticos<gauss_magnetic>`, :ref:`Lei de Faraday<faraday>` e a :ref:`Lei de Ampère-Maxwell<ampere_maxwell>`. 
As equações podem ser escritas de várias maneiras e caracterizam as relações físicas entre os campos :math:`(\mathbf{e},\mathbf{h})` e os fluxos :math:`(\mathbf{b},\mathbf{d})`. 
Formulações específicas podem ser obtidas através do uso de :ref:`relações constitutivas <physical_properties_index>`. As equações de Maxwell podem ser escritas na frequência 
ou no tempo e na forma diferencial ou integral:

(a) :ref:`differential_equations_time`
(b) :ref:`differential_equations_frequency`
(c) :ref:`integral_equations_time`
(d) :ref:`integral_equations_frequency`

Esta página foi projetada para ser um acesso rápido às equações relevantes com
:ref:`notação<conv_matematica>` e unidades. As equações são apropriadas para campos EM na matéria. Se os campos estão em espaço livre, então as mesmas relações constitutivas são usadas, 
mas com :math:`\sigma= 0`, :math:`\mu_0` e :math:`\varepsilon_0`. As equações constitutivas também são escritas assumindo que as propriedades físicas são isotrópicas e não dispersivas. 
Mais detalhes sobre isso podem ser encontrados em :cite:`ward1988` (pp. 133) ou na página de :ref:`propriedades físicas<physical_properties_index>`.

Variáveis e Unidades
--------------------

As variáveis e unidades de quantidades relevantes nas equações de Maxwell são dadas aqui.

.. include:: maxwell_variables.rst


.. _differential_equations_time:

Forma Diferencial no Domínio do Tempo
-------------------------------------

Aqui, apresentamos formas diferenciais para :ref:`Lei de Gauss para campos elétricos<gauss_electric>`, :ref:`Lei de Gauss para campos magnéticos<gauss_magnetic>`, 
:ref:`Lei de Faraday<faraday>` e a :ref:`Equação Ampere-Maxwell<ampere_maxwell>` no domínio do tempo.

.. math::
	\begin{align}
	\textbf{Gauss para campo E:}\;\;  &\nabla\cdot\mathbf{d}=\rho_f \\
	\textbf{Gauss para campo B:}\;\;  &\nabla\cdot\mathbf{b}=0 \\
	\textbf{Faraday:}          \;\;  &\nabla\times\mathbf{e}=-\dfrac{\partial \mathbf{b}}{\partial t} \\
	\textbf{Ampere-Maxwell:}   \;\;  &\nabla\times\mathbf{h}=\mathbf{j} + \dfrac{\partial \mathbf{d}}{\partial t}
	\end{align}

onde :math:`\rho_f` é a densidade de carga livre e :math:`\mathbf{j}` é a densidade de corrente livre. As seguintes :ref:`relações constitutivas<physical_properties_index>` 
pode ser usadas para substituirem campos e fluxos:

.. math::
	\begin{align}
	\mathbf{j} &= \sigma \mathbf{e}\\
	\mathbf{b} &= \mu \mathbf{h}\\
	\mathbf{d} &= \varepsilon \mathbf{e}
	\end{align}

.. _differential_equations_frequency:

Forma Diferencial no Domínio da Frequência
------------------------------------------

Aqui, apresentamos as formas diferenciais :ref:`lei de Gauss para campos elétricos<gauss_electric>`, :ref:`Lei de Gauss para campos magnéticos<gauss_magnetic>`, 
:ref:`Lei de Faraday<faraday>` and the :ref:`Equação de Ampere-Maxwell<ampere_maxwell>` no domínio da frequência:

.. math::
	\begin{align}
	\textbf{Gauss para campo E:} \;\; &\nabla\cdot\mathbf{D}=\rho_f \\
	\textbf{Gauss para campo B:} \;\; &\nabla\cdot\mathbf{B}=0 \\
	\textbf{Faraday:}           \;\; &\nabla\times\mathbf{E}=-i\omega\mathbf{B} \\
	\textbf{Ampere-Maxwell:}    \;\; &\nabla\times\mathbf{H}=\mathbf{J} + i\omega \mathbf{D}
	\end{align}

onde :math:`\rho_f` é a densidade de carga livre e :math:`\mathbf{J}` é a densidade de corrente. As seguintes :ref:`relações constitutivas<physical_properties_index>` 
podem ser usadas para substituirem campos e fluxos:

.. math::
	\begin{align}
	\mathbf{J} &= \sigma \mathbf{E}\\
	\mathbf{B} &= \mu \mathbf{H}\\
	\mathbf{D} &= \varepsilon \mathbf{E}
	\end{align}

.. _integral_equations_time:

Forma Integral no Domínio do Tempo
----------------------------------

Aqui, apresentamos formas integrais para :ref:`Lei de Gauss para campos elétricos<gauss_electric>`, :ref:`Lei de Gauss para campos magnéticos<gauss_magnetic>`, 
:ref:`Lei de Faraday<faraday>` e a :ref:`Equação Ampere-Maxwell<ampere_maxwell>` no domínio do tempo.

.. math::
	\begin{align}
	\textbf{Gauss para campo E:} \; & \int_V\nabla\cdot\mathbf{d}\; dV \! =\!\oint_S\mathbf{d}\cdot d\mathbf{a} \! = \! Q_f \\
	\textbf{Gauss para campo B:} \; & \oint_S \mathbf{b} \cdot d \mathbf{a}=0 \\
	\textbf{Faraday:}           \; & \oint_C \mathbf{e}\cdot d\mathbf{l}=-\int_S\dfrac{\partial \mathbf{b}}{\partial t}\cdot d\mathbf{a} \\
	\textbf{Ampere-Maxwell:}    \; & \oint_C \!\mathbf{h} \cdot  d\mathbf{l} = \! \int_S \!\Big ( \mathbf{j} \!+\! \dfrac{\partial \mathbf{d}}{\partial t} \Big ) \!\cdot d\mathbf{a}
	\end{align}

onde :math:`Q_f` é a carga elétrica total e :math:`\mathbf{j}` é a densidade de corrente livre. :math:`d\mathbf{a}` é uma unidade infintesimal de área de superfície com direção vetorial normal à superfície :math:`S`. :math:`d\mathbf{l}` é um comprimento infinitesimal com a direção vetorial ao longo de um caminho fechado :math:`C`. O seguinte 
:ref:`relacionamentos constitutivos<physical_properties_index>` podem ser usados para substituir campos e fluxos:

.. math::
	\begin{align}
	\mathbf{j} &= \sigma \mathbf{e}\\
	\mathbf{b} &= \mu \mathbf{h}\\
	\mathbf{d} &= \varepsilon \mathbf{e}
	\end{align}


.. _integral_equations_frequency:

Forma Integral no Domínio da Frequência
---------------------------------------

Aqui, apresentamos formas integrais para :ref:`Lei de Gauss para campos elétricos<gauss_electric>`, :ref:`Lei de Gauss para campos magnéticos<gauss_magnetic>`, 
:ref:`Lei de Faraday<faraday>` e a :ref:`Equação Ampere-Maxwell<ampere_maxwell>` no domínio da frequência.


.. math::
	\begin{align}
	\textbf{Gauss for E-field:} \; &\int_V\nabla\cdot\mathbf{D}\; dV=\oint_S\mathbf{D}\cdot d \mathbf{a} \! =\! Q_f \\
	\textbf{Gauss for B-field:} \; &\oint_S \mathbf{B} \cdot d\mathbf{a}=0 \\
	\textbf{Faraday:}           \; &\oint_C \mathbf{E}\cdot d\mathbf{l}=-i\omega\int_S\mathbf{B}\cdot d\mathbf{a} \\
	\textbf{Ampere-Maxwell:}    \; & \oint_C \!\mathbf{H} \cdot  d\mathbf{l} = \! \int_S \!\big ( \mathbf{J} \!+\! i\omega \mathbf{D} \big ) \!\cdot d\mathbf{a}
	\end{align}

onde :math:`Q_f` é a carga elétrica total e :math:`\mathbf{j}` é a densidade de corrente livre. :math:`d\mathbf{a}` é uma unidade infintesimal de área de superfície com direção vetorial 
normal à superfície :math:`S`. :math:`d\mathbf{l}` é um comprimento infinitesimal com a direção vetorial ao longo de um caminho fechado :math:`C`. As seguintes 
:ref:`relações constitutivas<physical_properties_index>` podem ser usados para substituir campos e fluxos:

.. math::
	\begin{align}
	\mathbf{J} &= \sigma \mathbf{E}\\
	\mathbf{B} &= \mu \mathbf{H}\\
	\mathbf{D} &= \varepsilon \mathbf{E}
	\end{align}












