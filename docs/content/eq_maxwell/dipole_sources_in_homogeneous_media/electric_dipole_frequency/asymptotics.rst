.. _frequency_domain_electric_dipole_asymptotics:

Aproximações Assintóticas
=========================

.. purpose::

    Aqui, expressões simplificadas para os campos elétricos e magnéticos são apresentadas para vários casos.
    Examinando expressões simplificadas, podemos ver mais facilmente como os campos dependem de certos parâmetros.


.. _frequency_domain_electric_dipole_asymptotics_DC:

Aproximação para o Campo DC
---------------------------

Os campos elétricos e magnéticos DC de uma fonte de dipolo elétrico podem ser obtidos a partir de soluções analíticas completas, tomando o limite como 
:math:`\omega \rightarrow 0`.
Neste caso, o número da onda :math:`k \rightarrow 0`.
Para uma fonte de dipolo elétrico :math:`\mathbf{\hat x} I ds`, o campo elétrico DC dentro de um meio homogêneo é dado por:

.. math::
	\lim_{\omega \rightarrow 0} \mathbf{E_e} = \frac{I ds}{4 \pi \sigma  r^3} \left[ \left(\frac{3x^2}{r^2} - 1 \right) \mathbf{\hat x} + \frac{3xy}{r^2} \mathbf{\hat y} + \frac{3xz}{r^2} \mathbf{\hat z} \right]
	:label: eq_Edip_Edc

De acordo com a Equação :eq:`eq_Edip_Edc`, o campo elétrico DC depende unicamente da localização de observação e da condutividade do meio.
A fonte e o campo elétrico também estão completamente em fase.
Da mesma forma, o campo magnético DC correspondente dentro do meio é dado por:

.. math::
	\lim_{\omega \rightarrow 0} \mathbf{H_e} = \frac{I ds}{4 \pi r^2} \left( -\frac{z}{r} \mathbf{\hat y} + \frac{y}{r} \mathbf{\hat z} \right)
	:label: eq_Edip_Hdc

De acordo com a Equação :eq:`eq_Edip_Hdc`, o campo magnético DC é independente de quaisquer propriedades físicas.
Além disso, os campos elétrico e magnético DC estão em fase um com o outro.


.. _frequency_domain_electric_dipole_asymptotics_near:

Aproximação Campo Próximo
-------------------------

Para campos que estão suficientemente próximos da fonte de dipolo elétrico, podemos assumir que :math:`|kr| \ll 1`.
Neste caso, o termo exponencial em :math:`\mathbf{E}_e` e :math:`\mathbf{H}_e` pode ser aproximado usando a expansão de Taylor:

.. math::
	e^{-ikr} \approx 1 - ikr + O \left ( k^2 r^2 \right )
	:label: eq_exp_TaylorO2

A aproximação de campo próximo para :math:`\mathbf{E}_e` pode ser obtida substituindo o termo exponencial na solução analítica completa pela aproximação da série de Taylor da Equação :eq:`eq_exp_TaylorO2`.
Desse modo:


.. math::
	\begin{split}
	\mathbf{E_e} \approx \frac{I ds}{4 \pi (\sigma + i \omega \varepsilon) r^3} \bigg ( 1 - ikr + & O \big ( k^2 r^2 \big ) \bigg ) \Bigg [ \Bigg ( \frac{x^2}{r^2} \mathbf{\hat x} + \frac{xy}{r^2} \mathbf{\hat y} + \frac{xz}{r^2} \mathbf{\hat z} \Bigg ) ... \\
	&\big ( -k^2 r^2 + 3ikr +3 \big ) + \big ( k^2 r^2 - ikr -1 \big ) \mathbf{\hat x} \Bigg ]
	\end{split}
	:label: eq_Edip_Enear1
	
A Equação :eq:`eq_Edip_Enear1` pode ser simplificado negligenciando os termos polinomiais que são :math:`O(k^2 r^2)` ou superior.
Supondo que estejamos no regime quase estático (:math:`| \omega\varepsilon | \ll \sigma`), o campo elétrico próximo a um momento de dipolo elétrico 
:math:`\mathbf{\hat x} I ds` é dado por:

.. math::
	\mathbf{E_e} \approx \frac{I ds}{4 \pi \sigma r^3} \left[ \left(\frac{3x^2}{r^2} - 1 \right) \mathbf{\hat x} + \frac{3xy}{r^2} \mathbf{\hat y} + \frac{3xz}{r^2} \mathbf{\hat z} \right] + O(k^2 r^2 )
	:label: eq_Edip_Enear2

De acordo com a Equação :eq:`eq_Edip_Enear2`, o campo elétrico próximo depende apenas do local de observação e da condutividade do meio.
Além disso, a fonte e o campo elétrico estão completamente em fase.

A aproximação de campo próximo para :math:`\mathbf{H}_e` pode ser obtida substituindo o termo exponencial na solução analítica completa pela aproximação da série de Taylor da Equação :eq:`eq_exp_TaylorO2`.
Desse modo:

.. math::
	\mathbf{H_e} \approx \frac{I ds}{4 \pi r^2} \left( ikr + 1 \right ) \bigg ( 1 - ikr + O \big ( k^2 r^2 \big ) \bigg ) \left( -\frac{z}{r} \mathbf{\hat y} + \frac{y}{r} \mathbf{\hat z} \right)
	:label: eq_Edip_Hnear1

A Equação :eq:`eq_Edip_Hnear1` pode ser ainda mais simplificado negligenciando os termos polinomiais que são :math:`O k^2 r^2)` ou superior.
Portanto, o campo magnético próximo ao momento de dipolo elétrico :math:`\mathbf{\hat x} I ds` é aproximadamente igual a:

.. math::
	\mathbf{H_e} \approx \frac{I ds}{4 \pi r^2} \left( -\frac{z}{r} \mathbf{\hat y} + \frac{y}{r} \mathbf{\hat z} \right) + O(k^2 r^2 )
	:label: eq_Edip_Hnear2

De acordo com a Equação :eq:`eq_Edip_Hnear2`, :math:`\mathbf{H}_e` não depende das propriedades físicas do meio de background.
Além disso, a Equação :eq:`eq_Edip_Hnear2` indica que :math:`\mathbf{E}_e` e :math:`\mathbf{H} _e` estão em fase.


.. _frequency_domain_electric_dipole_asymptotics_far:

Aproximação de Campo Distante
-----------------------------

Para campos suficientemente distantes da fonte de dipolo elétrico, podemos assumir que :math:`1 \ll | kr |`.
Nesse caso, a expansão de Taylor não pode ser usada para simplificar os termos exponenciais em soluções analíticas completas para os campos.
As expressões ainda podem ser simplificadas, no entanto, considerando os termos de maior ordem em cada equação.

Vamos primeiro considerar a aproximação de campo distante de :math:`\mathbf{E}_e` dentro de um meio uniforme.
Para localizações fora do eixo (:math:`y, z \not \ll x`), apenas termos :math:`O (k^2r^2)` são necessários para aproximar com precisão o campo elétrico de uma fonte de dipolo elétrico.
No entanto, no caso em que (:math:`y, z \ll x`), os termos de segunda ordem na direção :math:`\mathbf{\hat x}` cancelam, e ambos os 
:math:`\mathbf{ \hat y}` e :math:`\mathbf{\hat z}` são insignificantes devido à geometria. Supondo que estejamos no regime quase estático 
(:math:`| \omega \varepsilon| \ll \sigma`), e dado que :math:`k^2 = - i \omega \mu \sigma`, o distante a aproximação de campo de :math:`\mathbf{E}_e` é representada pelos dois casos a seguir:


.. math::
	\mathbf{E_e} \approx
	\begin{cases}
	\dfrac{i\omega \mu I ds}{4 \pi r} e^{-ikr} \Bigg [ \left ( \dfrac{x^2}{r^2} - 1 \right ) \mathbf{\hat x} + \dfrac{xy}{r^2} \, \mathbf{\hat y} + \dfrac{xz}{r^2} \, \mathbf{\hat z} \Bigg ] \; \; &\textrm{for} \; \; y,z \not \ll x \\
	\; & \; \\
	\dfrac{ik Ids}{2\pi \sigma x^2} e^{-ikx} \mathbf{\hat x} &\textrm{for} \; \; y,z \ll x
	\end{cases}

Vamos agora considerar a aproximação de campo distante de :math:`\mathbf{H}_e` dentro de um meio uniforme.
Desde que :math:`1 \ll | kr |`, podemos simplificar a expressão analítica completa da mesma maneira e mostrar que:

.. math::
	\mathbf{H_e} \approx \frac{ik I ds}{4\pi r} e^{-ikr} \left ( -\frac{z}{r} \mathbf{\hat y} + \frac{y}{r}\mathbf{\hat z} \right )




