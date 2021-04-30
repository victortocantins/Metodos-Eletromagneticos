.. _maxwell_fundamentals_sources:

Equações de Maxwell com Fontes Electromagnéticas
================================================

.. purpose::
	
	Aqui, mostramos como as equações de Maxwell são alteradas na presença de fontes eletromagnéticas. Os dois principais tipos de fontes eletromagnéticas são discutidos.

Em muitos casos, os campos e fluxos dentro de uma região resultam da presença de uma fonte eletromagnética. Como as equações de Maxwell caracterizam totalmente todas as interações eletromagnéticas, elas também devem acomodar a existência de fontes eletromagnéticas. Existem dois tipos principais de fontes eletromagnéticas: fontes elétricas (:math:`\mathbf{j_e^s}`) e fontes magnéticas (:math:`\mathbf{j_m^s}`).

Fontes Elétricas
----------------

Nas equações de Maxwell, as fontes elétricas são representadas usando uma densidade de corrente (:math:`\mathbf{j_e^s}`). Portanto, eles têm unidades 
:math:`[\mathrm{A/m}^2]`. As fontes elétricas podem corresponder a um :ref:`dipolo de corrente elétrica<definition_electric_dipole_index>` ou um loop de fio transportando corrente.

De acordo com a Equação de :ref:`Ampere-Maxwell<ampere_maxwell>`, correntes elétricas são responsáveis por gerar fluxos magnéticos. Ao contabilizar o termo da fonte elétrica, a equação Ampère-Maxwell torna-se:

.. math::
	 \nabla\times \mathbf{h} - \mathbf{j_f} - \frac{\partial \mathbf{d}}{\partial t} = \mathbf{j_e^s}

onde :math:`\mathbf{j_f}` agora é a densidade de corrente livre não contabilizada pelo termo fonte. A densidade de corrente total dentro da região pode ser tratada como a soma da densidade de corrente de origem e a densidade de corrente livre restante (ou seja :math:`\mathbf{j_{tot} = j_e^s + j_f}`). No domínio da frequência, a equação Ampère-Maxwell torna-se:

.. math::
	\nabla\times \mathbf{H} - \mathbf{J_f} - i\omega \mathbf{D} = \mathbf{J_e^s}

onde o termo da fonte elétrica é dado por :math:`\mathbf{J_e^s}` e a densidade de corrente livre remanescente é dada por :math:`\mathbf{J_f}`.

Fontes Magnéticas
-----------------

Nas equações de Maxwell, a fonte magnética é uma densidade de fluxo magnético (:math:`\mathbf{b_m^s}`); que tem unidades [T]. Um exemplo de fonte magnética é o :ref:`dipolo magnético<definition_magnetic_dipole_index>`.

De acordo com :ref:`Lei de Faraday <faraday>`, fluxos magnéticos variáveis no tempo induzem campos elétricos rotacionais. Observe, entretanto, que a análise dimensional da lei de Faraday mostra que o lado direito tem unidades [T/s]. Como resultado, o termo de fonte magnética é comumente definido como :math:`\mathbf{j_m^s}`, onde:


.. math::
	\mathbf{j_m^s} = - \frac{\partial \mathbf{b_m^s}}{\partial t}

Por esta convenção, o termo fonte magnética pode ser considerado uma densidade de corrente magnética. Na presença de um termo de fonte magnética, a lei de Faraday torna-se:

.. math::
	\nabla \times \mathbf{e} + \frac{\partial \mathbf{b}}{\partial t} = \mathbf{j_m^s}

onde :math:`\mathbf{b}` é a densidade de fluxo magnético não considerada dentro do termo fonte. A densidade total do fluxo magnético dentro da região pode ser tratada como a soma da densidade do fluxo da fonte e a densidade do fluxo restante (ou seja :math:`\mathbf{b_{tot}=b_m^s + b}`). No domínio da frequência, a densidade do fluxo magnético da fonte é dada por :math:`\mathbf{B_m^s}`. O termo de origem correspondente é, portanto, definido como:

.. math::
	\mathbf{J_m^s} = -i\omega\mathbf{B_m^s}

e a Lei de Faraday é dado por:

.. math::
	\nabla\times \mathbf{E} + i\omega\mathbf{B} = \mathbf{J_m^s}

	
Reafirmando as Equações de Maxwell
----------------------------------

A existência de fontes elétricas e magnéticas resulta em alterações na equação de Maxwell-Ampère e na lei de Faraday, respectivamente. Vamos agora reafirmar as equações de Maxwell em forma diferencial na presença de fontes eletromagnéticas.

Forma Diferencial no Domínio do Tempo
*************************************

Aqeui, apresentamos as formas diferenciais para :ref:`lei de Gauss para campos elétricos<gauss_electric>`, :ref:`lei de Gauss para campos magnéticos<gauss_magnetic>`, :ref:`lei de Faraday<faraday>` e a :ref:`equação de Ampere-Maxwell<ampere_maxwell>` no domínio do tempo.

.. math::
	\begin{align}
	\textbf{Gauss for E-field:}\;\;  &\nabla\cdot\mathbf{d}=\rho_f \\
	\textbf{Gauss for B-field:}\;\;  &\nabla\cdot\mathbf{b}=0 \\
	\textbf{Faraday:}          \;\;  &\nabla\times\mathbf{e} + \dfrac{\partial \mathbf{b}}{\partial t} = \mathbf{j_m^s} \\
	\textbf{Ampere-Maxwell:}   \;\;  &\nabla\times\mathbf{h} - \mathbf{j_f} - \dfrac{\partial \mathbf{d}}{\partial t} = \mathbf{j_e^s}
	\end{align}

onde as seguintes :ref:`relações constitutivas<physical_properties_index>` podem ser usadas para substituir campos e fluxos.

.. math::
	\begin{align}
	\mathbf{j} &= \sigma \mathbf{e}\\
	\mathbf{b} &= \mu \mathbf{h}\\
	\mathbf{d} &= \varepsilon \mathbf{e}
	\end{align}

Se considerarmos um **meio homogêneo** e combinamos a equação de Maxwell-Ampère e a lei de Faraday para obter a equação de onda, vemos que para uma 
**fonte elétrica**:

.. math::
	\nabla^2 \mathbf{e} - \mu\sigma \frac{\partial \mathbf{e}}{\partial t} - \mu \varepsilon \frac{\partial^2 \mathbf{e}}{\partial t^2} = \mu \frac{\partial \mathbf{j_e^s}}{\partial t}

Como podemos ver, o termo fonte na equação de onda acima depende da derivada no tempo de uma densidade de corrente elétrica. Para uma 
**fonte magnética**:

.. math::
	\nabla^2 \mathbf{h} - \mu\sigma \frac{\partial \mathbf{h}}{\partial t} - \mu \varepsilon \frac{\partial^2 \mathbf{h}}{\partial t^2} = - \sigma \mathbf{j_m^s} - \mu \frac{\partial \mathbf{j_m^s}}{\partial t}

onde o termo fonte contém derivada no tempo de primeira ordem além do termo sem derivada da fonte :math:`j_m^s` (ordem 0).

Forma Diferencial no Domínio da Frequência
******************************************

Aqui, apresentamos as formas diferenciais para :ref:`lei de Gauss para os acampos elétricos<gauss_electric>`, :ref:`lei de Gauss para os campos magnéticos<gauss_magnetic>`, :ref:`lei de Faraday<faraday>` e a :ref:`equação de Ampere-Maxwell<ampere_maxwell>` no domínio da frequência:

.. math::
	\begin{align}
	\textbf{Gauss for E-field:} \;\; &\nabla\cdot\mathbf{D}=\rho_f \\
	\textbf{Gauss for B-field:} \;\; &\nabla\cdot\mathbf{B}=0 \\
	\textbf{Faraday:}           \;\; &\nabla\times\mathbf{E} + i\omega\mathbf{B} = \mathbf{J_m^s} \\
	\textbf{Ampere-Maxwell:}    \;\; &\nabla\times\mathbf{H} - \mathbf{J_f} - i\omega \mathbf{D} = \mathbf{J_e^s}
	\end{align}

onde as seguintes :ref:`relações constitutivas<physical_properties_index>` podem ser usadas para substituir campos e fluxos:

.. math::
	\begin{align}
	\mathbf{J} &= \sigma \mathbf{E}\\
	\mathbf{B} &= \mu \mathbf{H}\\
	\mathbf{D} &= \varepsilon \mathbf{E}
	\end{align}

Se considerarmos um **meio homogêneo** e combinamos a equação de Maxwell-Ampère e a lei de Faraday para obter a equação de Helmholtz, vemos que para uma **fonte elétrica**:

.. math::
	\nabla^2 \mathbf{E} + k^2 \mathbf{E} = i\omega\mu \mathbf{J_e^s}

onde a magnitude do termo de fonte aumenta linearmente em relação à frequência angular. Para uma **fonte magnética**:

.. math::
	\nabla^2 \mathbf{H} + k^2 \mathbf{H} = - \big ( \sigma + i\omega\varepsilon \big ) \mathbf{J_m^s}

onde o lado direito depende das propriedades condutivas e dielétricas do meio. Lembre-se de que o
:ref:`o número de onda<harmonic_planewaves_homogeneous_wavenumber>` é dado por:

.. math::
	k = \sqrt{\omega^2 \mu \varepsilon - i\omega \mu\sigma}


