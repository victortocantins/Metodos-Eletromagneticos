.. _harmonic_planewaves_homogeneous_phasevelocity:

Velocidade de Fase
==================

A velocidade de fase define a velocidade na qual as ondas oscilantes em uma determinada frequência se propagam. Como o :ref:`comprimento de onda<harmonic_planewaves_homogeneous_wavelength>`, a velocidade de fase depende do componente real do :ref:`número de onda<harmonic_planewaves_homogeneous_wavenumber>` (:math:`\alpha`) e é dada por:

.. math:: v_{ph} = \frac{\omega}{\alpha} = \left ( \frac{\mu \epsilon}{2} \left [ \left ( 1 + \frac{\sigma^2}{\epsilon^2 \omega^2} \right )^{1/2} + 1 \right ] \right )^{-1/2}

Velocidade de Fase para Vários Materiais
----------------------------------------

A tabela abaixo mostra a velocidade de fase para certas rochas em várias frequências. Isso serve como um guia geral, já que os tipos de rocha são classificados por uma gama de valores de propriedades físicas que podem levar a diferenças de ordem de magnitude na velocidade de fase.

+---------------------+-------------------+-------------+------------------+---------------------+----------------------+----------------------+----------------------+
|Tipo                 |:math:`\sigma`     |:math:`\mu_r`|:math:`\epsilon_r`|:math:`v_{ph}` (1Hz) |:math:`v_{ph}` (1kHz) |:math:`v_{ph}` (1MHz) |:math:`v_{ph}` (1GHz) |
+=====================+===================+=============+==================+=====================+======================+======================+======================+
|Ar                   | 0 S/m             | 1           | 1                | 299.8 m/us          | 299.8 m/us           | 299.8 m/us           | 299.8 m/us           |
+---------------------+-------------------+-------------+------------------+---------------------+----------------------+----------------------+----------------------+
|Água do Mar          | 3.3 S/m           | 1           | 80               | 0.0017 m/us         | 0.055 m/us           | 1.7 m/us             | 32 m/us              |
+---------------------+-------------------+-------------+------------------+---------------------+----------------------+----------------------+----------------------+
|Ígneas               |:math:`10^{-4}` S/m| 1           | 5                | 0.32 m/us           | 10 m/us              | 132 m/us             | 134 m/us             |
+---------------------+-------------------+-------------+------------------+---------------------+----------------------+----------------------+----------------------+
|Sedimentares (seco)  |:math:`10^{-3}` S/m| 1           | 4                | 0.1 m/us            | 3.2 m/us             | 90 m/us              | 150 m/us             |
+---------------------+-------------------+-------------+------------------+---------------------+----------------------+----------------------+----------------------+
|Sedimentares (molhado|:math:`10^{-2}` S/m| 1           | 25               | 0.032 m/us          | 1 m/us               | 30 m/us              | 60 m/us              |
+---------------------+-------------------+-------------+------------------+---------------------+----------------------+----------------------+----------------------+
|Sulfetos Silicatos   |:math:`10^{2}` S/m | 1           | 5                | 0.00032 m/us        | 0.01 m/us            | 0.32 m/us            | 10 m/us              |
+---------------------+-------------------+-------------+------------------+---------------------+----------------------+----------------------+----------------------+
|Magnetita Silicatos  |:math:`10^{2}` S/m | 2           | 5                | 0.00022 m/us        | 0.007 m/us           | 0.22 m/us            | 7 m/us               |
+---------------------+-------------------+-------------+------------------+---------------------+----------------------+----------------------+----------------------+


Aproximações
------------

.. _harmonic_planewaves_homogeneous_phasevelocity_quasi:

Aproximação Quase Estática
^^^^^^^^^^^^^^^^^^^^^^^^^^

No regime quase estático (:math:`\epsilon\omega \ll \sigma`), a velocidade de fase simplifica para:

.. math:: v_{ph} = \sqrt{ \frac{2\omega}{\mu \sigma} }

Assim, a velocidade de fase é mais rápida para ondas que oscilam em frequências mais altas. As ondas EM também se movem mais lentamente em meios que são condutores e altamente permeáveis.

Aproximação de Regime de Onda
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No regime de onda ( :math:`\epsilon \omega \gg \sigma` ), a velocidade de fase simplifica para:

.. math:: v_{ph} = \frac{1}{\sqrt{\mu \epsilon}}
    :label: wn3

Assim, em frequências suficientemente altas, as ondas em todas as frequências se propagam com a mesma velocidade. No espaço livre, as equações anteriores são simplificadas para 
:math:`1/ \! \sqrt{\mu_0 \epsilon_0} = 3 \times 10^8` m/s, que é a velocidade da luz.


Relacionando Comprimento de Onda e Velocidade de Fase
-----------------------------------------------------

Como mostramos, tanto a :ref:`comprimento de onda<harmonic_planewaves_homogeneous_wavelength>` e a velocidade de fase podem ser definidos em termos da componente real do 
:ref:`número de onda<harmonic_planewaves_homogeneous_wavenumber>` (:math:`\alpha`). Como resultado, podemos definir uma relação matemática quando relacionamos o comprimento de onda e a velocidade de fase em uma determinada frequência. Essa relação é dada por:

.. math::
	\lambda = \frac{2\pi v_{ph}}{\omega} = \frac{v_{ph}}{f}

onde :math:`f` ié a frequência de oscilação em Hz. Desta expressão, podemos ver que ondas EM que se propagam mais rapidamente pela Terra correspondem a comprimentos de onda mais longos.





