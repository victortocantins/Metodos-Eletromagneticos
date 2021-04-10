.. _harmonic_planewaves_homogeneous_derivation:

Derivação
=========

Solução Gerla para uma Onda Plana
---------------------------------

.. figure:: images/planewavedown.png
   :align: right
   :figwidth: 50%
   :name: planewavedown_freq_derivation
   
   Geometria de uma onda plana propagando-se para baixo.

Para obter uma solução para ondas planas EM em um meio homogêneo, vamos começar com as seguintes equações vetoriais de Helmholtz para :math:`\mathbf{E}` e :math:`\mathbf{H}`:

.. math::
    \boldsymbol{\nabla}^2 \mathbf{E} + k^2 \mathbf{E}  &= 0\\
    \boldsymbol{\nabla}^2 \mathbf{H} + k^2 \mathbf{H}  &= 0
    :label: Helmholtz_full_analytic

onde o :ref:`número de onda<harmonic_planewaves_homogeneous_wavenumber>` complexo é dado por:

.. math::
    k = \sqrt{\mu \epsilon \omega^2 - i \mu \sigma \omega}
    :label: Helmholtz_complex_wavenumber

Para simplificar, vamos supor que a onda plana se propague ao longo da direção :math:`z`. De acordo com Griffiths :cite:`griffiths1999` (pp. 378), os campos elétricos e magnéticos suportados por uma onda plana são transversais à direção de propagação; assim, os campos elétricos e magnéticos estão no plano :math:`xy`. Neste caso, a equação governante para o campo elétrico simplifica para:

.. math::
    \frac{\partial^2 \mathbf{E}}{\partial z^2} + k^2 \mathbf{E} = 0
    :label: Helmholtz_1D_analytic

onde :math:`\mathbf{E} \equiv \mathbf{E}(z,\omega)`; assim ela não depende nem de :math:`x` ou :math:`y`. A equação anterior tem uma solução geral na forma:

.. math::
    \mathbf{E} = \mathbf{E}_0^- \, e^{i(kz-\omega t)} + \mathbf{E}_0^+ \, e^{-i(kz + \omega t)}
    :label: Helmholtz_1D_solution

onde :math:`\mathbf{E}_0^-` e :math:`\mathbf{E}_0^+` são as amplitudes do vetores  of para baixo e para cima, respectivamente. A exponencial :math:`e^{-i\omega t}` em ambos os termos  controla a fase temporal. O número de onda complexo tem as ambas componentes real e imagnária. Dessa forma ela pode ser expressada como:

.. math::
    k = \alpha - i\beta
    :label: wavenumber_split

em que :math:`\alpha \geq 0` e :math:`\beta \geq 0` dependem da frequência e das propriedades físicas do meio. Substituindo a Equação :eq:`wavenumber_split` na Equação 
:eq:`Helmholtz_1D_solution`, a solução para nossa equação da onda para :math:`\mathbf{E}` e torna-se:

.. math::
    \mathbf{E} = \mathbf{E}_0^- \, e^{\beta z} e^{i(\alpha z -\omega t)} + \mathbf{E}_0^+ \, e^{-\beta z} e^{-i (\alpha z + \omega t)}
    :label: Helmholtz_1D_components

Para as ondas descendentes e ascendentes, existem dois comportamentos importantes na solução. O primeiro termo, que contém :math:`e^{\pm i \alpha z}`, controla o comportamento oscilatório (ou seja :ref:`comprimento de onda <harmonic_planewaves_homogeneous_wavelength>`) e :ref:`velocity <harmonic_planewaves_homogeneous_phasevelocity>` de cada onda. O segundo termo, que contém :math:`e^{\pm \beta z}`, controla o comportamento de decaimento (ou seja :ref:`atenuação <harmonic_planewaves_homogeneous_skindepth>`) de cada onda. Observe que como 
:math:`z\rightarrow -\infty` para a onda descendente, sua amplitude vai a zero. O mesmo comportamento ocorre para a onda ascendente como :math:`z \rightarrow \infty`.

Usando a mesma abordagem na equação de Helmholtz para :math:`\mathbf{H}`, o campo magnético tem uma solução geral da forma:

.. math::
    \mathbf{H} &= \mathbf{H}_0^- \, e^{i(kz-\omega t)} + \mathbf{H}_0^+ \, e^{-i(kz+\omega t)}\\
    &= \mathbf{H}_0^- \, e^{\beta z} e^{i(\alpha z-\omega t)} + \mathbf{H}_0^+ \, e^{-\beta z} e^{-i (\alpha z+\omega t)}
    :label: Helmholtz_1D_h

.. note::

    A Equação :eq:`Helmholtz_1D_components` ainda é uma solução geral. Para determinar :math:`\mathbf{E}_0^-` e :math:`\mathbf{E}_0^+` explicitamente, você deve invocar um conjunto de condições de contorno. Por exemplo, :math:`\mathbf{E}(z \rightarrow -\infty, \omega) = 0` e :math:`\mathbf{E}(z = 0, \omega) = \mathbf{E}_0`. Isso lhe daria uma solução 
    :math:`\mathbf{E} (z,\omega) = \mathbf{E}_0 \, e^{\beta z} e^{i(\alpha z - \omega t)}` (ou seja, apenas a onda descendente). A partir desta solução, :math:`\mathbf{H}(z,\omega)` 
    pode ser determinada usando a lei de Faraday. Você também pode invocar condições de contorno para resolver para :math:`\mathbf{H}` e usar a lei de Ampère-Maxwell para obter 
    :math:`\mathbf{E}`.

.. _harmonic_planewaves_homogeneous_derivation_app:

Derivação de Suporte para o Aplicativo
--------------------------------------

.. figure:: images/planewavedown.png
   :align: right
   :figwidth: 50%
   :name: planewavedown_freq_derivation_2

   Propagação da onda plana descedente modelada pelo app.
   
O aplicativo simula a propagação descendente de uma onda plana EM. Como podemos ver em :numref:`planewavedown_freq_derivation_2`, a onda do plana é polarizada de forma que o campo elétrico fique ao longo da direção :math:`x` e o campo magnético fique ao longo da direção :math:`y`. Fisicamente, podemos pensar nesta onda como sendo causada por uma folha horizontal de corrente harmônica :math:`\mathbf{I} (\omega) = I_x \, \textrm{cos}(\omega t) \mathbf{u_x}`, onde :math:`\mathbf{u_x}` é o vetor unitário na direção :math:`x`.

Para resolver o campo elétrico, começamos com a solução geral da Equação :eq:`Helmholtz_1D_components`:

.. math::
    \mathbf{E} (z,\omega) = \mathbf{E}_0^-  e^{ikz} + \mathbf{E}_0^+ e^{-ikz}

onde :math:`\mathbf{E}_0^-` e :math:`\mathbf{E}_0^+` são as amplitudes das ondas descendentes e ascendentes, respectivamente. Dado que estamos apenas modelando a onda descendente e o campo elétrico correspondente possui apenas componentes na direção :math:`x`, nossa solução assume a forma:

.. _harmonic_planewaves_homogeneous_derivation_app_soln:

.. math::
    \mathbf{E} (z,\omega) = E_x (z,\omega) \, \mathbf{u_x} = E_{x,0}^{-} e^{ikz} \mathbf{u_x}

onde :math:`E_x` é uma função escalar e :math:`E_{x,0}^{-}` é a amplitude escalar do campo elétrico. Usando a Lei de Faraday, podemos confirmar que o campo magnético correspondente tem apenas componentes na direção :math:`y`, onde:

.. math::
    \frac{\partial E_x}{\partial z} + i \omega \mu H_y = 0

Solucionando para a componente :math:`y` do campo magnético, obtemos:

.. math::
    H_y (z,\omega ) = H_{y,0}^- e^{ikz} = -\frac{k}{\omega \mu} E_{x,0}^- \, e^{ikz}

Assim:

.. math::
    \mathbf{H}(z,\omega) = H_y (z,\omega) \, \mathbf{u_y} = - \frac{k}{\omega \mu} E_{x,0}^- \, e^{ikz} \, \mathbf{u_y}

onde :math:`\mathbf{u_y}` é o vetor unitário na direção :math:`y`.


