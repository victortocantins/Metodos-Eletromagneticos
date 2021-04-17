.. _transient_planewaves_homogeneous_peaktime:

Tempo de Pico
=============

O tempo de pico é o momento em que a amplitude máxima do sinal é observada em um determinado local. O tempo de pico observado em :numref:`fig_planewaves_peaktime` (a) pode ser obtido definindo a derivada de tempo da solução analítica para :math:`E_x` igual zero. Onde:

.. math::
	e_x(t>0)  = E_{x,0}^- \frac{\big (\mu\sigma)^{1/2} z}{2\pi^{1/2} t^{3/2}} \, e^{-\mu\sigma z^2/4t}

é a solução analítica quase estática, o tempo de pico é dado por:

.. math::
    t_{max} = \frac{\mu\sigma z^2}{6}
    :label: tmax

Para um impulso como excitação, o tempo de pico é proporcional ao quadrado da distância percorrida.

.. figure:: images/Ward1988Fig1_2.png
   :align: center
   :scale: 40%
   :name: fig_planewaves_peaktime

   Campo elétrico em função do tempo 100 m de um impulso 1D no campo em um espaço inteiro de 0,01 S/m (a). Campo elétrico em t = 0,03 ms em função da distância (modificado de :cite:`ward1988`) (b).
