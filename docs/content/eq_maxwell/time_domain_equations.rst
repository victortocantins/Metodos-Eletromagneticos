.. _time_domain_equations:

Equações de Maxwell: Domínio do Tempo
=====================================

.. purpose::

    Aqui, :ref:`Lei de Faraday <faraday>` e a equação :ref:`Ampere-Maxwell <ampere_maxwell>` são usadas para construir equações de onda com perdas para :math:`\mathbf{e}` e 
    :math:`\mathbf{h}`, respectivamente. Isso é realizado assumindo que estamos em um meio homogêneo. Derivações detalhadas podem ser encontradas no :ref:`Apêndice <maxwell1_apethoscope_wave_eq_derivation_time>`. Várias componentes das equações diferenciais de 2ª ordem resultantes no tempo são discutidos. 
    O entendimento físico das equações derivadas aqui pode ser estendido para aplicações mais complexas em todo o curso.

Vamos começar com a forma difrencials da :ref:`Lei de Faraday<faraday>` e a :ref:`equação de Ampere-Maxwell<ampere_maxwell>`, respectivamente:

.. math::
    \boldsymbol{\nabla} \times \mathbf{e}
    = -\frac{\partial \mathbf{b}}{\partial t}
    :label: faraday_time

.. math::
    \boldsymbol{\nabla} \times \mathbf{h}
    = \mathbf{j} + \frac{\partial \mathbf{d}}{\partial t}
    :label: ampere_maxwell_time

as well as the three :ref:`constitutive relations<physical_properties_index>`:

.. math::
    \mathbf{j} = \sigma \mathbf{e}
    :label: ohms_law_time

.. math:: \mathbf{d} = \epsilon \mathbf{e}
    :label: depse

.. math:: \mathbf{b} = \mu \mathbf{h}
    :label: bmuh

Nosso objetivo é combinar essas equações para obter uma equação que depende exclusivamente de :math:`\mathbf{e}` ou :math:`\mathbf{h}`. Para :math:`\mathbf {e}`, começamos tomando o rotacional de :eq:`faraday_time`. Em seguida, usamos as Equações :eq:`ohms_law_time` e :eq:`depse` para reduzir o número de variáveis. Assumindo que todas as propriedades físicas são constantes no espaço e no tempo, podemos considerá-las fora dos operadores de onda e derivadas do tempo. Por fim, obtemos a Equação :eq:`hme7`:

.. math::  \boldsymbol{\nabla}^2 \mathbf{e} - \mu \sigma \frac{\partial \mathbf{e}}{\partial t} - \mu \epsilon \frac{\partial^2 \mathbf{e}}{\partial t^2}  = 0
    :label: hme7

Um procedimento semelhante pode ser usado para obter uma equação que envolve apenas :math:`\mathbf{h}`. Começamos da Equação :eq:`ampere_maxwell_time`, e usando as Equações 
:eq:`faraday_time` e :eq:`bmuh` obtemos:

.. math:: \boldsymbol{\nabla}^2 \mathbf{h} - \mu \sigma \frac{\partial \mathbf{h}}{\partial t} - \mu \epsilon \frac{\partial^2 \mathbf{h}}{\partial t^2}  = 0
    :label: hmh7

A s derivações detalhadas das Equações :eq:`hme7` e :eq:`hmh7` pode ser encontrada :ref:`aqui <maxwell1_appendix_wave_eq_derivation_time>`

A Equação da Onda com Perda
---------------------------

As Equações :eq:`hme7` e :eq:`hmh7` têm forma idêntica e são caracterizados usando a **equação de onda com perdas**. Assim, os sinais eletromagnéticos se propagam como ondas que também estão sujeitas à difusão. O primeiro termo em cada equação é chamado de Laplaciano (:math:`\nabla^2`). O segundo termo, que contém uma derivada de tempo de primeira ordem, controla o comportamento difusivo do sinal eletromagnético. O terceiro termo, que contém uma derivada de tempo de segunda ordem, representa um termo de conservação de energia. A velocidade de propagação, difusão e outros comportamentos das ondas eletromagnéticas são discutidos ao apresentar materiais sobre :ref:`ondas planas transitórias no meio homogênea <transient_planewaves_homogeneous_index>`.


Regime Quase Estático
---------------------

No regime quase estático, o termo difusivo é muito maior do que o termo de conservação, ou seja:

.. math::
    \sigma \frac{\partial \mathbf{e}}{\partial t} \gg \epsilon \frac{\partial^2 \mathbf{e}}{\partial t^2} \;\;\;\;\; \textrm{e} \;\;\;\;\; \sigma \frac{\partial \mathbf{h}}{\partial t} \gg \epsilon \frac{\partial^2 \mathbf{h}}{\partial t^2}

Nete caso, ambos :math:`\mathbf{e}` e :math:`\mathbf{h}`  se comportam de acordo com a **equação do calor**, com:

.. math::
    \nabla^2 \mathbf{e} - \mu\sigma \frac{\partial \mathbf{e}}{\partial t} = 0

e

.. math::
    \nabla^2 \mathbf{h} - \mu\sigma \frac{\partial \mathbf{h}}{\partial t} = 0

A taxa de difusão é controlada pelo produto de :math:`\mu\sigma`. Lembre-se de :ref:`propriedades físicas <physical_properties_index>` entretanto, que :math:`\mu\approx\mu_0` para a maioria dos materiais e que :math:`\sigma` varia em muitas ordens de magnitude. Como resultado, as propriedades difusivas dos sinais eletromagnéticos são principalmente dependentes da condutividade. O comportamento difusivo dos sinais EM é um aspecto muito importante dos métodos eletromagnéticos no domínio do tempo (:ref:`TDEM <airborne_tdem_index>`).    


Regime de Ondas
---------------

No regime de ondas, o termo difusivo é muito menor do que o termo de conservação, ou seja:

.. math::
    \sigma \frac{\partial \mathbf{e}}{\partial t} \ll \epsilon \frac{\partial^2 \mathbf{e}}{\partial t^2} \;\;\;\;\; \textrm{e} \;\;\;\;\; \sigma \frac{\partial \mathbf{h}}{\partial t} \ll \epsilon \frac{\partial^2 \mathbf{h}}{\partial t^2}

Neste, caso :math:`\mathbf{e}` e :math:`\mathbf{h}` comportam-se de acordo a clássica **equação da onda**, com:

.. math::
    \nabla^2 \mathbf{e} - \mu\epsilon \frac{\partial^2 \mathbf{e}}{\partial t^2} = 0

e

.. math::
    \nabla^2 \mathbf{h} - \mu\epsilon \frac{\partial^2 \mathbf{h}}{\partial t^2} = 0

Aqui, a energia é conservada e ambos :math:`\mathbf{e}` e :math:`\mathbf{h}` propagam-se como ondas. As propriedades das ondas (comprimento de onda, velocidade de propagação, etc ...) dependem do produto de :math:`\mu\epsilon`. Lembre-se de :ref:`propriedades físicas <physical_properties_index>` entretanto, que :math:`\mu\approx\mu_0` para a maioria dos materiais e que 
:math:`\epsilon` varia em várias ordens de magnitude. Como resultado, as propriedades da onda são principalmente dependentes da permissividade dielétrica. As propriedades das ondas são um aspecto importante dos levantamentos de radar de penetração no solo ( :ref:`GPR <gpr_index>`).














