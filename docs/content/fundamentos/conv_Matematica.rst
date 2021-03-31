.. _conv_Matematica:

Notação e Convenção
===================

Escolhemos a notação estabelecida em :cite:`ward1988`. O capítulo desta obra tem
sido a base de muitos trabalhos de pesquisa, é usado por geofísicos em todo o mundo é claro e inequívoco.

Vetores
-------

- vetores e operadores vetoriais são em negrito:
    * exemplo: :math:`\mathbf{v}`, :math:`\boldsymbol{\nabla\cdot}`, :math:`\boldsymbol{\nabla\times}`
- tensores são em negrito and sublinhados:
    * exemplo: :math:`\mathbf{\underline{v}}`, :math:`\boldsymbol{\underline{\sigma}}`
- variáveis no domínio do tempo são minúsculas:
    * exemplo: :math:`\mathbf{e}`, :math:`\mathbf{j}`, :math:`\mathbf{h}`, :math:`\mathbf{b}`
- variáveis no domínio da frequencia são maiúsculas:
    * exemplo: :math:`\mathbf{E}`, :math:`\mathbf{J}`, :math:`\mathbf{H}`, :math:`\mathbf{B}`

Integrais
---------

- Integração de uma função escalar sobre um volume:
    .. math::
        \int_V f ~dv

   ou sobre um volume fechado:
    .. math::
        \oint_V f ~dv

- Integração de uma função vetorial sobre uma superfície:
    .. math::
        \int_S \mathbf{f} \cdot \mathbf{da} = \int_S \mathbf{f} \cdot \mathbf{\hat{n}} ~da

   ou sobre uma superfície fechada:
    .. math::
        \oint_S \mathbf{f} \cdot \mathbf{da} = \oint_S \mathbf{f} \cdot \mathbf{\hat{n}} ~da

- Integração de uma função vetorial sobre uma curva:
    .. math::
        \int_C \mathbf{f} \cdot \mathbf{dl} = \int_C \mathbf{f} \cdot \mathbf{\hat{n}} ~dl

   ou sobre uma curva fechada:
    .. math::
        \oint_C \mathbf{f} \cdot \mathbf{dl} = \oint_C \mathbf{f} \cdot \mathbf{\hat{n}} ~dl


.. _fourier_transform_convention:

Convenção da Transformada de Fourier
------------------------------------

Também adotamos a escolha de sinal na Transformada de Fourier considerando a dependência temporal :math:`e^{i\omega t}`.

.. math::
    F(\omega) = \int_{-\infty}^{\infty} f(t)e^{-i\omega t} dt
    :label: fourier_transform_convention

.. math::
    f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) e^{i\omega t} d\omega
    :label: inv_fourier_transform_convention



.. **References**

..  .. bibliography:: ../references.bib
..     :style: alpha
..     :encoding: latex+latin
..     :filter: docname in docnames
