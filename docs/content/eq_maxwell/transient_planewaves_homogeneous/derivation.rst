.. _transient_planewaves_homogeneous_derivation:

Derivação
==========

Solução Geral para uma Onda Plana
---------------------------------

.. figure:: images/planewavedown.png
   :align: center
   :figwidth: 50%
   :name: planewavedown_time_derive

   Geometria de uma onda plana propagando-se para baixo.

Para obter uma solução para ondas planas EM em um meio homogêneo, vamos começar com as seguintes equações de onda vetorial para :math:`\mathbf {e}` e :math:`\mathbf {h}`:


.. math::
    \boldsymbol{\nabla}^2 \mathbf{e} - \mu\epsilon \frac{\partial^2 \mathbf{e}}{\partial t^2} - \mu\sigma \frac{\partial \mathbf{e}}{\partial t} &= 0\\
    \boldsymbol{\nabla}^2 \mathbf{h} - \mu\epsilon \frac{\partial^2 \mathbf{h}}{\partial t^2} - \mu\sigma \frac{\partial \mathbf{h}}{\partial t} &= 0
    :label: Wave_full_analytic

Para simplificar, vamos supor que a onda do plano se propague ao longo da direção z. De acordo com Griffiths 
:cite:`griffiths1999` (pp. 378), os campos elétricos e magnéticos suportados por uma onda plana são transversais à direção de propagação; assim, os campos elétricos e magnéticos estão no plano xy. Neste caso, a equação governante para o campo elétrico simplifica para:    

.. math::
    \frac{\partial^2 \mathbf{e}}{\partial z^2} - \mu\epsilon \frac{\partial^2 \mathbf{e}}{\partial t^2} - \mu\sigma \frac{\partial \mathbf{e}}{\partial t} = 0

onde :math:`\mathbf{e} \equiv \mathbf{e}(z,t)`; portanto, não depende de x ou y. A fim de fornecer as condições iniciais para o PDE, deixe que o campo elétrico seja causado um impulso tal que nossas condições iniciais sejam dadas por:

.. math::
  \mathbf{e}(t=0)=\mathbf{E}_0\delta(t)
  :label: e_impulse

onde :math:`\delta(t)` é a função Delta de Dirac em :math:`t=0`. Em vez de resolver o PDE dependente do tempo diretamente, aplicaremos a transformada de Laplace inversa a soluções analíticas derivadas do 
:ref:`domínio da frequência<harmonic_planewaves_homogeneous_derivation>`:

.. math::
    \mathbf{E} =  \mathbf{E}_0^- e^{ikz} + \mathbf{E}_0^+ e^{-ikz}
    :label: e_frequency_analytic

em que :math:`E_0^-` e :math:`E_0^+` são as amplitudes vetoriais de ondas descendentes e ascendentes, respectivamente. Observe que o termo harmônico :math:`e^ {-i\omega t}` está sendo suprimido. A solução no domínio do tempo para uma excitação por impulso pode ser expressa como:

.. math::
	\mathbf{e}(t) = \mathcal{F}^{-1}[\mathbf{E}(\omega)]

onde :math:`\mathcal{F}[\cdot]` é a Transformada de Fourier. Modificada de :cite:`ward1988`, a solução correspondente no domínio do tempo para a equação de onda é:

.. math::
    \mathbf{e}(t) =& \mathbf{E}_0^- \Bigg ( e^{a(z/c)} \delta \bigg ( t+\frac{z}{c} \bigg ) -\frac{aze^{-at}}{c \big ( t^2-\frac{z^2}{c^2} \big)^{1/2}}
    I_1 \Bigg [ a \bigg ( t^2-\frac{z^2}{c^2} \bigg )^{1/2} \Bigg ] u \bigg ( t+\frac{z}{c} \bigg ) \Bigg ) \\
    &+ \mathbf{E}_0^+ \Bigg ( e^{-a(z/c)} \delta \bigg ( t-\frac{z}{c} \bigg ) +\frac{aze^{-at}}{c \big ( t^2-\frac{z^2}{c^2} \big)^{1/2}}
    I_1 \Bigg [ a \bigg ( t^2-\frac{z^2}{c^2} \bigg )^{1/2} \Bigg ] u \bigg ( t-\frac{z}{c} \bigg ) \Bigg )
    :label: e_wave_analytic_sol

onde

- :math:`u(t)` é função degrau de heaviside

- :math:`I_1(x)` é a função de Bessel modificada  de primeira espécie

- :math:`a=\dfrac{\sigma}{2\epsilon}`

- :math:`c=\dfrac{1}{\sqrt{\mu\epsilon}}`

Ambas as ondas subindo e descendo têm dois termos. O primeiro termo, contendo a função delta de Dirac, é o termo de onda. O segundo termo é o termo de difusão. Constantes :math:`a` e :math:`c` controlam as propriedades de onda e difusão da onda plana.

No caso em que a onda EM foi causada por um impulso correspondente às condições iniciais 
:math:`\mathbf{h}(t=0) = \mathbf{H_0}\delta(t)`, a solução geral para o campo magnético seria dado por:

.. math::
    \mathbf{h}(t) =& \mathbf{H}_0^- \Bigg ( e^{a(z/c)} \delta \bigg ( t+\frac{z}{c} \bigg ) -\frac{aze^{-at}}{c \big ( t^2-\frac{z^2}{c^2} \big)^{1/2}}
    I_1 \Bigg [ a \bigg ( t^2-\frac{z^2}{c^2} \bigg )^{1/2} \Bigg ] u \bigg ( t+\frac{z}{c} \bigg ) \Bigg )\\
    &+ \mathbf{H}_0^+ \Bigg ( e^{-a(z/c)} \delta \bigg ( t-\frac{z}{c} \bigg ) +\frac{aze^{-at}}{c \big ( t^2-\frac{z^2}{c^2} \big)^{1/2}}
    I_1 \Bigg [ a \bigg ( t^2-\frac{z^2}{c^2} \bigg )^{1/2} \Bigg ] u \bigg ( t-\frac{z}{c} \bigg ) \Bigg )
    :label: h_wave_analytic_sol

Note que as Equações :eq:`e_wave_analytic_sol` e Eq. :eq:`h_wave_analytic_sol` tem exatamente a mesma forma.

.. note::

    As Equações :eq:`e_wave_analytic_sol` e :eq:`h_wave_analytic_sol` ainda são soluções gerais, já que apenas as condições iniciais foram aplicadas. Para determinar :math:`\mathbf{E}_0^-` e :math:`\mathbf{E}_0^+` ou 
    :math:`\mathbf{H}_0^-` e :math:`\mathbf{H}_0^+`, você deve invocar um conjunto de condições de contorno. Por exemplo, :math:`\mathbf{e}(z\rightarrow -\infty, t) = 0` além de :math:`\mathbf{e}(t = 0) = \mathbf{E}_0 \delta(t)` resulta em um campo elétrico de propagação para baixo.

.. _transient_planewaves_homogeneous_derivation_app:


Derivação das Equações para o aplicativo
----------------------------------------

.. figure:: images/planewavedown.png
   :align: right
   :figwidth: 50%
   :name: planewavedown_time_derive_app
   
   Diagrama de configuração da propagação da onda EM plana indo para baixo (negativo :math:`z`).

O aplicativo simula a propagação para baixo de uma onda plana EM devido a uma corrente impulsiva. Como podemos ver em
:numref:`planewavedown_time_derive_app`, a onda do plano é polarizada de forma que a onda plana do campo elétrico fique ao longo da direção x e o campo magnético fique ao longo da direção y. Fisicamente, podemos pensar nesta onda como sendo causada por uma corrente de impulso horizontal :math:`\mathbf{I}(t)=I_0 \delta(t)\mathbf{u_x}`, onde 
:math:`\mathbf{u_x}` é o vetor unitário na direção x.

Para o aplicativo, consideramos apenas a aproximação quase estática da Equação :eq:`e_wave_analytic_sol`. Isso pode ser obtido tomando a transformada de Laplace inversa da :ref:`solução harmônica correspondente<harmonic_planewaves_homogeneous_derivation_app_soln>` tal que :math:`k=\sqrt{-i\omega\mu\sigma}`, ou seja:

.. math::
    \mathbf{E} (z,\omega) = E_x (z,\omega) \, \mathbf{u_x} = E_{x,0}^{-} e^{i\sqrt{-i\omega\mu\sigma}z} \mathbf{u_x}
    :label:

onde :math:`E_x` é uma função escalar e :math:`E_{x,0}^{-}` é a amplitude escalar do campo elétrico. Se substituirmos 
:math:`s=i\omega`, a transformação de Laplace inversa de :math:`E_x(z,w)` torna-se:

.. math::
    \mathcal{L}^{-1}[E_x (z,\omega)] = \mathcal{L}^{-1} \Bigg [ E_{x,0}^- \, e^{- \sqrt{\mu\sigma s} z} \Bigg ]
    :label:

Se usarmos a identidade (:cite:`abramowitz1965handbook`):

.. math::
    \mathcal{L}^{-1} \Bigg [ e^{-\alpha \sqrt{s}} \Bigg ] = \frac{\alpha}{2 \pi^{1/2} t^{3/2}} e^{-\alpha^2/4t} \;\;\; \textrm{for} \;\;\; \alpha \geq 0

a solução quase estática para o campo elétrico em :math:`t> 0` é dada por:

.. math::
	\mathbf{e}(t) = e_x(t) \mathbf{u_x} = E_{x,0}^- \frac{\big (\mu\sigma)^{1/2} z}{2\pi^{1/2} t^{3/2}} \, e^{-\mu\sigma z^2/4t} \, \mathbf{u_x}
	:label:

Da mesma forma, a solução para o campo magnético pode ser obtida tomando a transformada de Laplace inversa da 
:ref:`solução harmônica correspondente<harmonic_planewaves_homogeneous_derivation_app_soln>` tal que 
:math:`k = \sqrt{-i\omega\mu\sigma}`.

.. math::
    \mathcal{L}^{-1}[H_y (z,\omega)] = \mathcal{L}^{-1} \Bigg [ - \frac{ik}{i\omega \mu} E_{x,0}^- \, e^{ikz} \Bigg ] = \mathcal{L}^{-1} \Bigg [ - \sqrt{ \dfrac{\sigma}{\mu s}} E_{x,0}^- \, e^{- \sqrt{\mu\sigma s} z} \Bigg ]

onde :math:`k = \sqrt{-i\omega\mu\sigma}`, substituimos :math:`s = i\omega` e fazemos :math:`\sqrt{-1} = -i`.  Se seguimos  a seguimos a seguinte identidade :cite:`abramowitz1965handbook`:

.. math::
    \mathcal{L}^{-1} \Bigg [ \frac{1}{\sqrt{s}} e^{-\alpha \sqrt{s}} \Bigg ] = \frac{1}{\sqrt{\pi t}} e^{-\alpha^2/4t} \;\;\; \textrm{for} \;\;\; \alpha \geq 0

a solução quase estática para o campo magnético é dada por:

.. math::
    \mathbf{h}(t) = h_y(t) \mathbf{u_y} =  -E_{x,0}^- \sqrt{\dfrac{\sigma}{\pi\mu t}}\, e^{-\mu\sigma z^2/4t} \, \mathbf{u_y}

onde :math:`\mathbf{u_y}` é o vetor unitário na direção y.


