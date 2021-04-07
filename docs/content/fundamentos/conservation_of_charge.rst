.. _conservation_of_charge:

Lei da Conservação da Carga
===========================

A conservação de carga afirma que as cargas elétricas não podem ser criadas ou
destruídas. Não é uma equação independente, uma vez que pode ser derivada de
outras equações de Maxwell, mas é um ponto de partida útil para resolver alguns
problemas. Ela pode ser escrita nas formas integral e diferencial.


Forma Integral
--------------

A formulação integral de conservação da carga é

.. math::
    \int_A \mathbf{j} \cdot da =  - \dfrac{d}{dt} \int_V \rho dv = - \dfrac{dQ}{dt} 
    :label: charge_conservation_integral

onde:

- :math:`\mathbf{j}` é a densidade de corrente
- :math:`\rho` é a densidade de carga volumetrica
- :math:`Q` é a carga total dentro do volume
- :math:`A` é a área da superfície do volume 
- :math:`V` é o volume


Forma Diferencial:
------------------

Com o uso da equação do teorema da divergência ou (:ref:`Gauss_teorema`), a 
:eq:`charge_conservation_integral` pode ser escrita na forma diferencial:

.. math::
    \nabla \cdot \mathbf{j} = -\dfrac{\partial \rho}{\partial t}
    :label: charge_conservation_differential

Fórmula da Conservação da Carga da Lei de Ampère-Maxwell
--------------------------------------------------------

A conservação da equação da carga não é uma equação independente que precisa
para ser incluída juntamnete as equações de Maxwell. Pode ser derivada da Lei de Ampère-Maxwell e 
Lei de Gauss para cargas elétricas.

.. math::
    \nabla \times \mathbf{h} = \mathbf{j} +  \dfrac {\partial \mathbf{d}}{\partial t}
   

Tomando a divergência e usando :math:`\nabla \cdot \mathbf{d} = \rho_f` e  a identidade vetorial :math:`\nabla.\nabla\times\mathbf{f}=0` temos

.. math::
    0 = \nabla\cdot\nabla \times \mathbf{h} = \nabla\cdot\mathbf{j} +  \dfrac {\partial}{\partial t} \nabla\cdot\mathbf{d} \quad \text{implica} \quad
	\nabla \cdot \mathbf{j} = - \dfrac{\partial \rho_f}{\partial t}

Note que as equações de Maxwell :math:`\mathbf{j}` refere-se a densidade de cargas livres


Uso da conservação das cargas
-----------------------------

Equações iniciais para resistividade DC
***************************************

Se houver um termo fonte, digamos uma corrente :math:`I` que é injetada em uma
locação :math:`\mathbf{r_s}` então a lei para a conservação de carga torna-se

.. math::
	\nabla \cdot \mathbf{j} + \dfrac{\partial \rho_f}{\partial t} = I \delta (\mathbf{r} - \mathbf{r_s})

Observe que o sinal positivo se refere à corrente positiva sendo injetada no
meio. Sob condições de estado estacionário, o termo da derivada de tempo é zero e o
equação se reduz a

.. math::
	\nabla \cdot \mathbf{j}  = I \delta (\mathbf{r} - \mathbf{r_s})

que é uma equação inicial para problemas de resistividade DC.

Dissipação de carga livre em um meio condutor
*********************************************

Este é um cálculo clássico, mas criterioso (:cite:`stratton1941`). Considere um pequeno
volume tendo uma densidade de carga inicial de :math:`\rho_0`. A carga é liberada
em um meio homogêneo que tem uma condutividade :math:`\sigma` e permissividade 
:math:`\epsilon_0`. Usando :math:`\mathbf{j}=\sigma\mathbf{e}` podemos escrevemos

.. math::
	\nabla \cdot \mathbf{j} = \dfrac{\sigma}{\epsilon_0} \nabla \cdot \mathbf{d} = \dfrac{\sigma}{\epsilon_0}\rho_f

A conservação das cargas torna-se

.. math::	
	\dfrac{\partial \rho_f}{\partial t} + \dfrac{\sigma}{\epsilon_0}\rho_f = 0

que tem uma solução

.. math::
	\rho_f(t)= \rho_0 e^{ \frac {-\sigma}{\epsilon_0} t}
	
Mesmo com condutividade muito baixa, por exemplo :math:`\sigma=10^{-5}` com 
:math:`\epsilon_0 = 8,85 \times 10^{-12}` a densidade de carga no local de
liberação diminui por um fator de :math:`e` em :math:`10^{-6}` segundos. Assim para
tipos de materiais de Terra, uma carga inserida na terra se dissipa
extremamente rápido.


