.. _harmonic_planewaves_homogeneous_wavenumber:

Número de Onda
==============

Para ondas eletromagnéticas caracterizadas pela equação de Helmholtz, todas as propriedades de onda correspondentes podem ser derivadas do número de onda :math:`k`. O número de onda em uma determinada frequência depende das propriedades físicas do meio de propagação e é dado por:

.. math:: k = \sqrt{\mu \epsilon \omega^2 - i \mu \sigma \omega}

O número de onda tem componentes real e imaginária e pode ser decomposto da seguinte forma:

.. math:: k = \alpha - i \beta

tal que :ref:`solução geral<harmonic_planewaves_homogeneous_derivation>` para a propagação de ondas planas EM na direção vertical torna-se:

.. math::
	\mathbf{E} = \mathbf{E}_0^- \, e^{\beta z}e^{i(\alpha z-\omega t)} + \mathbf{E}_0^+ \, e^{-\beta z}e^{-i(\alpha z+\omega t)}

De acordo com :cite:`stratton1941,ward1988`, :math:`\alpha` e :math:`\beta` are given by:

.. math:: \alpha = \omega \left ( \frac{\mu \epsilon}{2} \left [ \left ( 1 + \frac{\sigma^2}{\epsilon^2 \omega^2} \right )^{1/2} + 1 \right ] \right )^{1/2} \geq 0

.. math:: \beta = \omega \left ( \frac{\mu\epsilon}{2} \left [ \left ( 1 + \frac{\sigma^2}{\epsilon^2 \omega^2} \right)^{1/2} - 1 \right ] \right ) ^{1/2} \geq 0

Onde derivando uma :ref:`solução geral<harmonic_planewaves_homogeneous_derivation>`, estabelecemos que :math:`\alpha` (a componente real do número de onda) determina o  :ref:`comprimento de onda<harmonic_planewaves_homogeneous_wavelength>` e :ref:`velocidade<harmonic_planewaves_homogeneous_phasevelocity>` da onda plana. Enquanto :math:`\beta` (a componente imaginária  do número de onda) determina a :ref:`atenuação<harmonic_planewaves_homogeneous_skindepth>`. Os detalhes disso podem ser aprendidos visualmente por meio do aplicativo, bem como por meio do seguinte material sobre as propriedades de ondas plans.

Aproximações
------------

Aproximação Quase Estática
^^^^^^^^^^^^^^^^^^^^^^^^^^

No regime quase estático (:math:`\epsilon\omega \ll \sigma`), o número de onda simplifica para:

.. math::
    k \approx \sqrt{- i \mu \sigma \omega}

onde pode ser mostrado que:

.. math::
    \alpha = \beta = \left ( \frac{\omega \mu \sigma}{2} \right ) ^{1/2}

Neste caso, ondas EM oscilam e decaem quando se propagam.

Aproximação de Regime de Onda
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No regime de onda (:math:`\epsilon\omega \gg \sigma`), o número de onda simplifica para:

.. math::
    k \approx \alpha = \sqrt{\mu \epsilon \omega^2} = \omega \sqrt{\mu \epsilon}

e

.. math::
    \beta \approx \frac{\sigma}{2} \sqrt{\frac{\mu}{\epsilon}} \sim 0
    
Para uma equação de onda perfeita, :math:`\beta = 0` e as ondas não diminuem em amplitude à medida que se propagam. Em problemas geofísicos (:ref:`radar de penetração no solo <gpr_index>` 
por exemplo), os sinais ainda sofrem perda de amplitude à medida que se propagam pela Terra.
