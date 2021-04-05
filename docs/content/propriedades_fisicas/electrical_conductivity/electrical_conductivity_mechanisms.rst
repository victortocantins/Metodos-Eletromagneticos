.. _electrical_conductivity_mechanisms:

Mecanismos de Condutividade e Cargabilidade
===========================================

Condução Elétrica e Iônica
---------------------------

A condução descreve o movimento da carga elétrica de um local para outro. Existem dois importantes portadores de carga elétrica, elétrons e íons. Vamos definir a condutividade da seguinte forma:

.. math::
	\sigma = n e \mu_e,

onde :math:`n` é o número de portadores de carga, :math:`e` é a carga transportada
por cada portadora de carga, e :math:`\mu_e` é a mobilidade das portadoras. Por esta definição,
a condutividade de uma rocha pode ser determinada por sua capacidade de mover cargas por meio de elétrons e íons. Isso resulta em dois tipos distintos de condução: condução elétrica e condução iônica. Ambas as conduções estão relacionadas ao movimento aleatório de partículas afetadas por um
campo elétrico aplicado. No entanto, como a carga se move em cada processo de condução é
bem diferente.

Condutividade Elétrica
^^^^^^^^^^^^^^^^^^^^^^

O portador de carga da condutividade elétrica é o elétron, que define a condução dentro da maioria dos metais, como ferro e cobre. O compartilhamento de elétrons de valência entre átomos metálicos permite que as cargas se movam livremente ao longo diretamente de um campo elétrico aplicado.

Condutividade Iônica
^^^^^^^^^^^^^^^^^^^^

A condução dentro da maioria das rochas é principalmente eletrolítica, ocorrendo no
espaços de poros conectados, ao longo dos limites de grãos e em fraturas. A condução dentro das rochas é normalmente insignificante através dos grãos minerais ou estrutura de silicato :cite:`ward1990`. Nesse
caso, o portador de carga consiste principalmente de íons dissolvidos; é por isso que usamos o termo condutividade iônica.

A condutividade iônica resulta do movimento ordenado de íons em um
eletrólito sob a aplicação de um campo elétrico externo. Sem nenhum
campo elétrico externo, os íons se movem aleatoriamente como resultado da temperatura
agitação e colisões com outros íons e átomos. Porque ambos os cátions (+)
e os ânions (-) estão presentes em um eletrólito, a condutividade pode ser
Expressa como

.. math::
	\sigma = e(n^+\mu_m^+ + n^-\mu_m^-),

onde :math:`n` é o número de portadores de carga, :math:`e` é a carga
transportada, e :math:`\mu_m` é a mobilidade dos portadoras. Aqui sobrescritos
+ e - representam cátion e ânion, respectivamente.

Polarização de Eletrodo e de Membrana
-------------------------------------

A cargabilidade dos materiais terrestres é essencialmente um efeito eletroquímico e pode ser
causada por muitos fatores, nem todos completamente compreendidos. Se o solo
é carregável, ele responde como se a resistividade fosse uma quantidade complexa - ele
se comporta como um capacitor com vazamento. Portanto, a cargabilidade pode ser
medido de várias maneiras usando técnicas no domínio do tempo ou no domínio da frequência.
Os aspectos que afetam a exigibilidade de uma amostra incluem:

- O tamanho do grão das partículas na amostra;
- O tipo e a mobilidade dos íons nos fluidos dos poros;
- Os detalhes das interações microscópicas entre superfícies sólidas e fluidos;
- A quantidade de área de superfície dentro de um volume específico.
- A relação entre a área de superfície e o volume é um fator importante. As argilas tendem a ter cargabilidade
  enquanto arenitos não são, e as imagens aqui ilustram um motivo porque isso é verdade. Além disso, as interações de superfície entre minerais de argila e os fluidos aumentam a capacidade desses materiais de reter cargas.

  
Existem duas causas principais de cargabilidades, "polarização da membrana" e "polarização do eletrodo". 
Em ambos os casos, a redistribuição de cargas após a aplicação de um campo elétrico DC externo leva algum tempo para ocorrer. Da mesma forma, leva a mesma quantidade de tempo para reverter para uma distribuição de carga equilibrada, uma vez que o campo elétrico é removido.

..     - Induced polarization is greater when there are larger regions of
..       adsorbed anomalous charge (adjacent to an interface); i.e. when there is
..       a large surface area-to-volume ratio.

..     - Non-ionic fluids (such as contaminants) can markedly change the
..       behavior of surface-electrolyte interactions.

..     - Changes in ion concentration (such as increased salinity) will also
..       affect both types of polarization.

..     - Both effects (membrane and electrode polarization) are related to grain
..       size as much as material type. Therefore, discrimination of mineral type
..       on the basis of chargeability alone is not recommended.


.. sidebar:: Polarização de Eletrodo

        .. figure:: ./images/elec_pol_1.gif
            :align: center
            :figwidth: 100 %
            :name: fig_elec_pol_1

            Eletrodo de polarização.

        .. figure:: ./images/elec_pol_2.gif
            :align: center
            :figwidth: 100 %
            :name: fig_elec_pol_2

            Dupla camadas elétricas.

        .. figure:: ./images/elec_pol_3.gif
            :align: center
            :figwidth: 100 %
            :name: fig_elec_pol_3
            
            Anomalia hipotética da distribuição de íons perto de uma interface sólido-líquido.
            
        .. figure:: ./images/elec_pol_4.gif
            :align: center
            :figwidth: 100 %
            :name: fig_elec_pol_4
            
            Circuito analógico da impedância interfacial
        


.. _electrical_conductivity_mechanisms_electrode:


Polarização de Eletrodo
^^^^^^^^^^^^^^^^^^^^^^^

A polarização do eletrodo ocorre quando os espaços dos poros são bloqueados por partículas metálicas (:numref:`fig_elec_pol_1`). Novamente, as cargas se acumulam quando um campo elétrico é aplicado. O resultado são duas camadas elétricas duplas que contribuem para as tensões medidas (:numref:`fig_elec_pol_2`).

Em interfaces entre condutores iônicos e metálicos (por exemplo, um grão de minério dentro do espaço de poro), há uma impedância associada à obtenção de corrente para fluir pelas interfaces. Essas interfaces se parecem com aquelas ilustradas em :numref:`fig_elec_pol_1` e têm um circuito analógico simplificado mostrado em :numref:`fig_elec_pol_4`. A corrente pode fluir através dessas interfaces pelo meio 1) transferência de carga (ou difusão de íons) ou 2) por meio de um efeito capacitivo (sem transferência de carga).

A difusão de íons não é fácil de modelar com elementos de circuito. Em vez disso, esse processo é frequentemente descrito usando a impedância de Warburg e a resistência de reação. A magnitude da impedância de Warburg varia aproximadamente como 
:math:`\omega^{- 1/2}`. Portanto, a impedância devido à difusão de íons realmente aumenta à medida que a frequência diminui.

Observe que, embora seja útil entender os modelos simplificados de relevantes comportamentos elétricos das interações eletrolíticas superficiais, todas as rochas são "sujas" no sentido de que não são simplesmente "eletrodos" puros. Existem outros materiais e partículas que afetam o comportamento iônico dentro e fora da camada difusa, e alguns dos constituintes da amostra afetarão o comportamento da camada fixa perto e nas interfaces líquido-sólido. Isso resultou na criação de muitos modelos empíricos para descrever as interações eletrolíticas de superfície.

.. _electrical_conductivity_mechanisms_membrane:

Polarização de Membrana
^^^^^^^^^^^^^^^^^^^^^^^

.. sidebar:: Polarização de Membrana

	.. figure:: ./images/memb1.gif
		:align: center
		:figwidth: 100 %
		:name: fig_memb_pol_1

		Íons em repouso.

	.. figure:: ./images/memb2.gif
		:align: center
		:figwidth: 100 %
		:name: fig_memb_pol_2

		Íons sujeitos ao campo.

	.. figure:: ./images/memb3.gif
		:align: center
		:figwidth: 100 %
		:name: fig_memb_pol_3

		Circuito dipolo elétrico.


A polarização da membrana ocorre quando o espaço dos poros se estreita para dentro de várias espessuras da camada limite (que são as espessuras dos íons adsorvidos em um superfície). Observe que as superfícies dos grãos minerais possuem naturalmente uma carga negativa fraca que atrai cátions 
(:numref:`fig_memb_pol_1`).

Quando um campo elétrico é aplicado, as cargas não podem fluir facilmente através da "garganta dos poros", então se acumulam 
(:numref:`fig_memb_pol_2`). O resultado é um dipolo elétrico líquido que contribui para quaisquer outras tensões medidas na rocha. 
Como a polarização do eletrodo, este processo não é instantâneo.

Uma segunda forma de polarização da membrana ocorre onde as partículas de argila bloqueiam parcialmente os caminhos da solução iônica, veja a figura a seguir. Após a aplicação de um campo elétrico, positivo. Os portadores de carga passam facilmente, enquanto os portadores negativos se acumulam. Isso é conhecido como uma "membrana seletiva de íons".


.. figure:: ./images/memb_pol_2nd_type.gif
	:align: center
	:figwidth: 70 %
	:name: fig-memb-pol-4
	

Um excedente de cátions e ânions ocorre em uma extremidade da membrana, enquanto
uma deficiência ocorre na outra extremidade. A redução da mobilidade é mais
óbvio em frequências mais lentas do que o tempo de difusão de íons entre
zonas de membrana; ou seja, mais lento do que cerca de 0,1 Hz. A condutividade aumenta em
frequências mais altas.
