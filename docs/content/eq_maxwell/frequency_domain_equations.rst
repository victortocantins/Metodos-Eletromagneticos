.. _frequency_domain_equations:

Equações de Maxwell: Domínio da Frequência
==========================================

.. purpose::
    Aqui, :ref:`Lei de Faraday<faraday>` e a equação :ref:`Ampere-Maxwell<ampere_maxwell>` são usadas para construir equações vetoriais de Helmholtz para :math:`\mathbf{E}` e 
    :math:`\mathbf{H}`, respectivamente. Isso é realizado assumindo que estamos em um meio homogêneo. Várias componentes das equações diferenciais resultantes em frequência são discutidas. 
    O entendimento físico das equações derivadas aqui pode ser estendido para aplicações mais complexas em todo o curso.
    
    
Para obter as equações de onda no domínio da frequência, usamos a transformada de Fourier com uma dependência de tempo do tipo
:math:`e^{i\omega t}`. A derivada de :math:`e^{i\omega t}` em relaçaão ao tempo é :math:`i\omega e^{i\omega t}`. Assim, podemos facilmente
converter as :ref:`equações de onda no domínio do tempo <time_domain_equations>` para o
domínio da frequência substituindo :math:`\partial / \partial t` por :math:`i\omega` e :math:`\partial^ 2 / \partial t^2` com :math:`- \omega^2`. 
As equações no domínio da frequência são, portanto, dadas por:

.. math::  \boldsymbol{\nabla}^2 \mathbf{E} + (\mu \epsilon \omega^2 - i \mu \sigma \omega) \mathbf{E}  = 0
    :label: hme8

e

.. math:: \boldsymbol{\nabla}^2 \mathbf{H} + (\mu \epsilon \omega^2 - i \mu \sigma \omega) \mathbf{H}  = 0
    :label: hmh8

Equações :eq:`hme8` e :eq:`hmh8` são geralemnte expressadas na seguinte forma:

.. math::
	\boldsymbol{\nabla}^2 \mathbf{E} + k^2 \mathbf{E}  = 0
	:label: hme9

e

.. math::
	\boldsymbol{\nabla}^2 \mathbf{H} + k^2 \mathbf{H}  = 0
	:label: hmh9

em que :math:`k = \sqrt{\mu \epsilon \omega^2 - i \mu \sigma \omega}` é conhecido com número de onda.

Equação de Helmholtz
--------------------

As Equações :eq:`hme9` e :eq:`hmh9` têm formas idênticas e são ambas caracterizadas pela **equação vetorial de Helmholtz**. Em teoria eletromagnética, a equação vetorial de Helmholtz é a equivalente no domínio da frequência da :ref:`equação de onda com perdas <time_domain_equations>`. As propriedades de :math:`\mathbf{E}` e :math:`\mathbf{H}` dependem do número de onda 
:math:`k`. Soluções para a equação de Helmholtz são frequentemente proporcionais a :math:`e^{\pm i k r}`, onde :math:`r` define alguma distância percorrida pelo sinal. Para essas soluções, 
a componente real de :math:`k` define a perda de amplitude à medida que o sinal viaja. A componente imaginária de :math:`k` define o comportamento oscilatório do sinal. Isso é discutido com muito mais detalhes quando falamos sobre :ref:`ondas planas harmônicas em um meio homogêneo <harmonic_planewaves_homogeneous_index>`.


Regime Quase Estático
---------------------

No regime quase estático, a condutividade domina as propriedades do sinal EM, ou seja:

.. math::
	\sigma \gg \omega \epsilon

e o número de onda é aproximadamente igual a:

.. math::
	k \approx \sqrt{-i\omega\mu\sigma}

O número de onda ainda tem componentes real e imaginária. Como resultado, o sinal EM experimenta atenuação e oscilação. O número de onda é controlado pelo produto de :math:`\mu\sigma`. Lembre-se de :ref:`propriedades físicas<physical_properties_index>` entretanto, que :math:`\mu\approx\mu_0` para a maioria dos materiais e que :math:`\sigma` varia em muitas ordens de magnitude. Como resultado, as propriedades de :math:`\mathbf{E}` e :math:`\mathbf{H}` são controladas principalmente pela condutividade. A relação entre :math:`\sigma` e sinais EM é muito importante para métodos eletromagnéticos no domínio de frequência (:ref:`FDEM <airborne_fdem_index> `).


Regime de Onda
--------------

No regime de onda, a permissividade dielétrica domina as propriedades do sinal EM, ou seja:

.. math::
	\sigma \ll \omega \epsilon

e o número de onda é aproximadamente igual a 

.. math::
	k \approx \sqrt{\omega^2 \mu\epsilon}

Neste caso, o número de onda contém apenas componente real e, portanto, a amplitude de :math:`e^{\pm i k r}` é constante. Isso faria sentido, visto que a energia é conservada em uma equação de onda sem perdas. O número de onda é controlado pelo produto de :math:`\mu\epsilon`. Lembre-se de :ref:`propriedades físicas<physical_properties_index>` entretanto, que 
:math:`\mu\approx\mu_0` para a maioria dos materiais e que :math:`\epsilon` varia em várias ordens de magnitude. Como resultado, as propriedades de :math:`\mathbf{E}` e 
:math:`\mathbf{H}` são controladas principalmente pela permissividade dielétrica. A relação entre :math:`\epsilon` e sinais EM é muito importante para o radar de penetração no solo no domínio da frequência.



