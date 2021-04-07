.. _maxwell1_appendix_wave_eq_derivation_time:

Derivação da Equação da Onda no Tempo
=====================================

Aqui, derivamos as equações de onda no tempo para os campos elétrico e magnético. Para fazer isso, começamos com :ref:`Lei de Faraday<faraday>` e 
:ref:`Lei de Ampere-Maxwell<ampere_maxwell>`:

.. math::
    \boldsymbol{\nabla} \times \mathbf{e}
    = -\frac{\partial \mathbf{b}}{\partial t}
    :label: faraday_time_derivation

.. math::
    \boldsymbol{\nabla} \times \mathbf{h}
    = \mathbf{j} + \frac{\partial \mathbf{d}}{\partial t}
    :label: ampere_maxwell_time_derive

bem como as três relações constitutivas:

.. math::
    \mathbf{j} = \sigma \mathbf{e}
    :label: jsigmae

.. math:: \mathbf{d} = \epsilon \mathbf{e}
    :label: depse_derivation

.. math:: \mathbf{b} = \mu \mathbf{h}
    :label: bmuh_derivation

Derivação para o Campo Elétrico
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para derivar a equação de onda para :math:`\mathbf{e}`, primeiro tomamos
o rotacional da Lei de Faraday, mostrada na equação :eq:`faraday_time_derivation`:

.. math:: \boldsymbol{\nabla} \times (\boldsymbol{\nabla} \times \mathbf{e}) = - \boldsymbol{\nabla} \times \frac{\partial \mathbf{b}}{\partial t}
    :label: hme1

As relações constitutivas apropriadas podem ser substituídas na Equação
:eq:`hme1` para obter as seguintes expressões em termos de apenas os campos
:math:`\mathbf{e}` e :math:`\mathbf{h}` em vez de campos e fluxos:

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{e} = - \boldsymbol{\nabla} \times \left (  \frac{\partial}{\partial t} (\mu \mathbf{h}) \right )
    :label: hme2

Assumindo que as propriedades físicas são homogêneas em todo o domínio, :math:`\mu`,
:math:`\epsilon`, e :math:`\sigma` podem ser movidos para a frente dos termos da derivada. Isso simplifica as expressões acima:
    
.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{e} = - \mu \boldsymbol{\nabla} \times \frac{\partial \mathbf{h}}{\partial t}
    :label: hme3

Se ainda assumirmos que podemos tomar a primeira e a segunda derivadas de
:math:`\mathbf{e}`, podemos tomar as derivadas primeiras espaciais ou as
derivadas do tempo. Equação :eq:`hme3` também pode ser escrita como:

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{e} = - \mu \frac{\partial}{\partial t} \left ( \boldsymbol{\nabla} \times \mathbf{h} \right )
    :label: hme4

Esta expressão agora é apenas em termos de :math:`\boldsymbol{\nabla}\times\mathbf{e}`e :math:`\boldsymbol{\nabla}\times\mathbf{h}`. 
Assim, podemos use Equação :eq:`ampere_maxwell_time_derive` para gerar uma equação com apenas
:math:`\mathbf{e}`. Substituímos na Equação :eq:`ampere_maxwell_time_derive` em
Equação :eq:`hme4` e simplificar usando as relações constitutivas nas Equações
:eq:`ohms_law_time` e :eq:`depse_derivation`:

.. math::  \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{e} = - \mu \frac{\partial}{\partial t} \left ( \mathbf{j} + \frac{\partial \mathbf{d}}{\partial t} \right )

.. math::  \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{e} = - \mu \frac{\partial}{\partial t} \left ( \sigma \mathbf{e} + \frac{\partial (\epsilon \mathbf{e})}{\partial t} \right )

.. math::  \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{e} = - \mu \sigma \frac{\partial \mathbf{e}}{\partial t} - \mu \epsilon \frac{\partial^2 \mathbf{e}}{\partial t^2}
    :label: hme5

Além disso, podemos simplificar o primeiro termo desta expressão usando o
identidade vetorial :math:`\boldsymbol{\nabla}\times\boldsymbol{\nabla}\times\mathbf{x} = \boldsymbol{\nabla}\boldsymbol{\nabla}\cdot\mathbf{x} - \boldsymbol{\nabla}^2 \mathbf{x}`. 
Lembrando que ambos
:math:`\boldsymbol{\nabla}\cdot\mathbf{e}` e :math:`\boldsymbol{\nabla}\cdot\mathbf{h}` são zero em um espaço homogêneo, a identidade vetorial simplesmente
torna-se :math:`\boldsymbol{\nabla}\times\boldsymbol{\nabla}\times\mathbf{x} = - \boldsymbol{\nabla}^2\mathbf{x}`. Se agora substituirmos isso
em :eq:`hme5`, obtemos a seguinte expressão:

.. math::  \boldsymbol{\nabla}^2 \mathbf{e}  - \mu \epsilon \frac{\partial^2 \mathbf{e}}{\partial t^2} - \mu \sigma \frac{\partial \mathbf{e}}{\partial t} = 0
    :label: hme6
    
Esta é a equação de onda para o campo elétrico no domínio do tempo.

Derivação para o Campo Magnético
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para derivar a equação de onda para :math:`\mathbf{h}`, repetimos acima a
derivação, mas iniciando agora, tomando o rotacional da Lei de Ampère, mostrada em
equação :eq:`ampere_maxwell_time_derive`:

.. math:: \boldsymbol{\nabla} \times (\boldsymbol{\nabla} \times \mathbf{h}) = \boldsymbol{\nabla} \times \mathbf{j} + \boldsymbol{\nabla} \times \frac{\partial \mathbf{d}}{\partial t}
    :label: hmh1

As relações constitutivas podem ser substituídas na Equação :eq:`hmh1` para obter
as seguintes expressões em termos de apenas :math:`\mathbf{e}` e
:math:`\mathbf{h}`:

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{h} = \boldsymbol{\nabla} \times (\sigma \mathbf{e}) + \boldsymbol{\nabla} \times \left (  \frac{\partial}{\partial t} (\epsilon \mathbf{e}) \right )
    :label: hmh2

Simplificamos a expressão como fizemos antes para o campo elétrico.

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{h} = \sigma \boldsymbol{\nabla} \times \mathbf{e} + \epsilon \boldsymbol{\nabla} \times \frac{\partial \mathbf{e}}{\partial t}
    :label: hmh3

Podemos assumir que podemos pegar a primeira e a segunda derivadas de
:math:`\mathbf{e}` e :math:`\mathbf{h}` e podemos tomar as
derivadas espaciais ou derivadas de tempo primeiro. A equação :eq:`hmh3` então também pode ser
escrita como:

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{h} = \sigma \boldsymbol{\nabla} \times \mathbf{e} + \epsilon \frac{\partial}{\partial t} \left ( \boldsymbol{\nabla} \times \mathbf{e} \right )
    :label: hmh4

Estas expresões são agora em termos de :math:`\boldsymbol{\nabla} \times
\mathbf{e}` e :math:`\boldsymbol{\nabla} \times \mathbf{h}`. Assim, podemos usar a 
Equação :eq:`faraday_time_derivation` para gerar uma equação com somente 
:math:`\mathbf{h}`. Então tomamos novamente a identidade vetorial
:math:`\boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{x} =
\boldsymbol{\nabla} \boldsymbol{\nabla} \cdot \mathbf{x} -
\boldsymbol{\nabla}^2 \mathbf{x}` e o fato de que :math:`\boldsymbol{\nabla}
\cdot \mathbf{h}` é zero num espaço homogêneo para simplificar a identidade vetorial
para :math:`\boldsymbol{\nabla} \times \boldsymbol{\nabla} \times
\mathbf{x} = - \boldsymbol{\nabla}^2 \mathbf{x}`. Isto é então substituído
na equação de onda, como mostra as seguintes derivações.


.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{h} = - \sigma \frac{\partial \mathbf{b}}{\partial t} - \epsilon \frac{\partial}{\partial t} \left (\frac{\partial \mathbf{b}}{\partial t} \right )

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{h} = - \sigma \frac{\partial (\mu \mathbf{h}) }{\partial t} - \epsilon \frac{\partial}{\partial t} \left (\frac{\partial (\mu \mathbf{h})}{\partial t} \right )

.. math:: \boldsymbol{\nabla} \times \boldsymbol{\nabla} \times \mathbf{h} = - \sigma \mu \frac{\partial \mathbf{h}}{\partial t} - \epsilon \mu \frac{\partial^2 \mathbf{h}}{\partial t^2}

.. math:: - \boldsymbol{\nabla}^2 \mathbf{h} = - \sigma \mu \frac{\partial \mathbf{h}}{\partial t} - \epsilon \mu \frac{\partial^2 \mathbf{h}}{\partial t^2}

.. math:: \boldsymbol{\nabla}^2 \mathbf{h} - \epsilon \mu \frac{\partial^2 \mathbf{h}}{\partial t^2} - \sigma \mu \frac{\partial \mathbf{h}}{\partial t} = 0
    :label: hmh6

A equação :eq:`hmh6` é então a equação de onda para o campo magnético no domínio do tempo. 

