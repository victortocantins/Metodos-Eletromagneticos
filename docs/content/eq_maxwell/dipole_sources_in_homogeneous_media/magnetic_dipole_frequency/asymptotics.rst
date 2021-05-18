.. _frequency_domain_magnetic_dipole_asymptotics:

Aproximações Assintóticas
=========================

.. purpose::

    Aqui, expressões simplificadas para os campos elétricos e magnéticos são apresentadas para vários casos.
    Examinando expressões simplificadas, podemos ver mais facilmente como os campos dependem de certos parâmetros.


.. _frequency_domain_magnetic_dipole_asymptotics_DC:

Aproximação Campo-DC
--------------------

Os campos elétricos e magnéticos DC de uma fonte de dipolo magnético podem ser obtidos a partir de soluções analíticas completas, tomando o limite como 
:math:`\omega\rightarrow 0`.
Neste caso, o número da onda :math:`k \rightarrow 0`.
Para uma fonte de dipolo magnético :math:`M \hat x`, o campo magnético DC dentro de um meio homogêneo é dado por:

.. math::
	\lim_{\omega \rightarrow 0} \mathbf{H_m} = \frac{m}{4 \pi r^3} \left[ \left(\frac{3x^2}{r^2} - 1 \right) \mathbf{\hat x} + \frac{3xy}{r^2} \mathbf{\hat y} + \frac{3xz}{r^2} \mathbf{\hat z} \right]
	:label: eq_Mdip_Hdc

De acordp com a Equação :eq:`eq_Mdip_Hdc`, o campo magnético DC depende exclusivamente do local de observação e do momento de dipolo. É independente de quaisquer propriedades físicas do meio.
A fonte e o campo magnético também estão completamente em fase.
Da mesma forma, o campo elétrico DC correspondente dentro do meio é dado por:

.. math::
	\lim_{\omega \rightarrow 0} \mathbf{E_m} = 0
	:label: eq_Mdip_Edc

De acordo com a Equação :eq:`eq_Mdip_Edc`, o campo elétrico DC é nulo.

.. _frequency_domain_magnetic_dipole_asymptotics_near:

Aproximação de Campo Próximo
----------------------------

Para campos suficientemente próximos da fonte de dipolo elétrico, podemos assumir que :math:`| kr | \ll 1`.
Neste caso, o termo exponencial em :math:`\mathbf{E}_m` e :math:`\mathbf{H}_m` pode ser aproximado usando a expansão de Taylor:

.. math::
	e^{-ikr} \approx 1 - ikr + O \left ( k^2 r^2 \right )
	:label: eq_exp_TaylorO2_mag

A aproximação de campo próximo para :math:`\mathbf{H}_m` pode ser obtida substituindo o termo exponencial na solução analítica completa pela aproximação da série de Taylor da Equação :eq:`eq_exp_TaylorO2_mag`.
Desse modo:

.. math::
	\begin{split}
	\mathbf{H_m} \approx \frac{m}{4 \pi r^3} \Big ( 1 - ikr + O ( k^2 r^2 ) \Big ) \Bigg [ \Bigg ( & \frac{x^2}{r^2} \mathbf{\hat x} + \frac{xy}{r^2} \mathbf{\hat y} + \frac{xz}{r^2} \mathbf{\hat z} \Bigg ) ... \\
	& \Big ( -k^2 r^2 + 3ikr +3 \Big ) + \Big ( k^2 r^2 - ikr -1 \Big ) \mathbf{\hat x} \Bigg ]
	\end{split}
	:label: eq_Mdip_Hnear1

A Equação :eq:`eq_Mdip_Hnear1` pode ser simplificada ngligenciando os termos polinomila que são :math:`O(k^2 r^2)` ou maiores.

.. math::
	\mathbf{H_m} \approx \frac{m}{4 \pi r^3} \left[ \left(\frac{3x^2}{r^2} - 1 \right) \mathbf{\hat x} + \frac{3xy}{r^2} \mathbf{\hat y} + \frac{3xz}{r^2} \mathbf{\hat z} \right] + O(k^2 r^2 )
	:label: eq_Mdip_Hnear2

De acordo com a Equação :eq:`eq_Mdip_Hnear2`, o campo magnético próximo depende apenas do local de observação e do momento de dipolo magnético.
Além disso, a fonte e o campo magnético estão completamente em fase.

A aproximação de campo próximo para :math:`\mathbf{E}_m` pode ser obtida substituindo o termo exponencial na solução analítica completa pela aproximação da série de Taylor da Equação :eq:`eq_exp_TaylorO2_mag`.
Desse modo:

.. math::
	\mathbf{E_m} \approx \frac{i \omega \mu m}{4 \pi r^2} \left( ikr + 1 \right ) \left ( 1 - ikr + O \left ( k^2 r^2 \right ) \right ) \left( -\frac{z}{r} \mathbf{\hat y} + \frac{y}{r} \mathbf{\hat z} \right)
	:label: eq_Mdip_Enear1

A Equação :eq:`eq_Mdip_Enear1` pode ser ainda mais simplificado negligenciando os termos polinomiais que são :math:`O(k^2 r^2)` ou superior.
Portanto, o campo elétrico próximo ao momento de dipolo magnético :math:`\hat x I S` é aproximadamente igual a:

.. math::
	\mathbf{E_m} \approx \frac{i \omega \mu m}{4 \pi r^2} \left( -\frac{z}{r} \mathbf{\hat y} + \frac{y}{r} \mathbf{\hat z} \right) + O(k^2 r^2 )
	:label: eq_Mdip_Enear2

De acordo com a Equação :eq:`eq_Mdip_Enear2`, :math:`\mathbf{E}_m` depende das propriedades físicas do meio de fundo.
Além disso, a Equação :eq:`eq_Mdip_Enear2` indica que :math:`\mathbf{E}_m` e :math:`\mathbf{H}_m` estão fora de fase.


Aproximação de Campo Distante
-----------------------------

Para campos suficientemente distantes da fonte de dipolo elétrico, podemos assumir que :math:`1 \ll | kr |`.
Nesse caso, a expansão de Taylor não pode ser usada para simplificar os termos exponenciais em soluções analíticas completas para os campos.
As expressões ainda podem ser simplificadas, no entanto, considerando os termos de maior ordem em cada equação.

Vamos primeiro considerar a aproximação de campo distante de :math:`\mathbf{H}_m` dentro de um meio uniforme.
Para localizações fora do eixo (:math:`y, z \not \ll x`), apenas os termos :math:`O(k^2r^2)` são necessários para aproximar com precisão o campo elétrico de uma fonte de dipolo elétrico.
No entanto, no caso em que (:math:`y, z \ll x`), os termos de segunda ordem na direção :math:`\mathbf{\hat x}` cancelam, e ambos :math:`\mathbf{\hat y}` e 
:math:`\mathbf{\hat z}` são insignificantes devido à geometria. Supondo que estejamos no regime quase estático :math:`k^2 = - i \omega \mu \sigma`, a aproximação de campo distante de :math:`\mathbf{H}_m` é representada pelos dois casos a seguir:

.. math::
	\mathbf{H_m} \approx
	\begin{cases}
	\dfrac{i \omega \mu \sigma m}{4 \pi r} e^{-ikr} \Bigg [ \left ( \dfrac{x^2}{r^2} - 1 \right ) \mathbf{\hat x} + \dfrac{xy}{r^2} \, \mathbf{\hat y} + \dfrac{xz}{r^2} \, \mathbf{\hat z} \Bigg ] \; \; &\textrm{for} \; \; y,z \not \ll x \\
	\; & \; \\
	\dfrac{ik m}{2 \pi x^2} e^{-ikx} \mathbf{\hat x} &\textrm{for} \; \; y,z \ll x
	\end{cases}

Vamos agora considerar a aproximação de campo distante de :math:`\mathbf{E}_m` dentro de um meio uniforme.
Desde :math:`1 \ll |kr|`, podemos simplificar a expressão analítica completa da mesma maneira e mostrar que:

.. math::
	\mathbf{E_m} \approx \frac{-k \omega \mu m}{4\pi r} e^{-ikr} \left ( -\frac{z}{r}\mathbf{\hat y} + \frac{y}{r}\mathbf{\hat z} \right )




