.. _lenz:

Lei de Lenz
===========

Por meio de uma série de experimentos em 1831, Michael Faraday chegou a
constatação de que os campos magnéticos variáveis criam campos elétricos. Dois anos
posteriormente, Heinrich Lenz formulou a Lei de Lenz, que caracteriza a direção
das correntes induzidas em um condutor por esses campos magnéticos variáveis com o tempo.

Uma maneira conveniente de quantificar a força do campo magnético em um
região particular é o fluxo magnético (:math:`\Phi_{\mathbf{B}}`),

.. math::
    {\boldsymbol \Phi_b} = \int_A {\bf b} \cdot \hat {\bf{n}} \, da
    :label: magnetic_flux_time_lenz

que fornece uma medida da densidade do fluxo sobre uma dada área

Lei de Faraday da indução

.. math::
    \mathcal{E} = - \, \frac{\partial {\boldsymbol \Phi_b}}{\partial t}
    :label: faraday_lenz_time2

mostra que qualquer variação no fluxo magnético produz uma força eletromotriz
(fem, :math:`\mathcal{E}`). Este fem cria correntes elétricas dentro daqueles
corpos que estão sujeitos ao fluxo variável com o tempo. A amplitude do
corrente induzida é dependente da força da fem e da condutividade
do material, enquanto a direção da corrente induzida é caracterizada
pela Lei de Lenz.

A Lei de Lenz afirma que a corrente induzida irá fluir em tal direção que
seus campos magnéticos secundários ou induzidos agem para se opor à mudança observada no 
fluxo magnético. Simplificando, "a natureza abomina uma mudança no fluxo", de modo que a corrente
induzida flui de forma a cancelar a mudança :cite:`griffiths1999`. Isto é
a razão para o sinal negativo na Lei de Faraday, equação :eq:`faraday_lenz_time2`.  :numref:`Lenzs_Law_Diagram` e o 
link da demonstração abaixo fornece ilustrações visuais da Lei de Lenz.

 .. figure:: images/LenzsLawDiagram.png
    :align: center
    :scale: 25%
    :name: Lenzs_Law_Diagram

    No painel (a), vemos uma situação em que o fluxo magnético através do
    loop está aumentando em função do tempo. A direção da corrente induzida
    e o campo magnético secundário que se opõe ao aumento do fluxo são
    mostrado no painel (b). Da mesma forma, o painel (c) mostra quando o fluxo magnético
    através do loop está diminuindo em função do tempo e do painel (d)
    demonstra a direção da corrente induzida e o campo magnético secundário. 
    (Figura criada por  M. Mitchell usando a seguinte Wikimedia
    Commons images: `VFPt_dipole <https://commons.wikimedia.org/wiki/File:VFPt_dipole.svg>`_
    e `VFPt ringcurrentNoLoop <https://commons.wikimedia.org/wiki/File:VFPt_ringcurrentNoLoop.svg>`_
    ambas são licenciadas `Creative Commons Attribution-Share Alike 3.0
    não portado <https://creativecommons.org/licenses/by-sa/3.0/deed.en>`_.)

Demonstração ilustrativa:

.. raw:: html

    <div style="position: relative; padding-bottom: 2%; height: 0; overflow: hidden; max-width: 100%; height: auto;"><iframe width="560" height="315" src="https://www.youtube.com/embed/N7tIi71-AjA" frameborder="0" allowfullscreen></iframe></div>

Agradecimentos Technical Services Group (TSG) at MIT's Departmento de Física!
