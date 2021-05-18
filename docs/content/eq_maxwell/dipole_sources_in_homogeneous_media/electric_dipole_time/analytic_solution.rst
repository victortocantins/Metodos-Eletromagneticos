.. _time_domain_electric_dipole_analytic_solution:

Solução Analítica
=================

.. purpose::

    Aqui, apresentamos uma formulação para prever os campos elétricos e magnéticos gerados por um transiente da fonte dipolo de corrente elétrica. 
    Isso é realizado aplicando a transformada de Laplace inversa a soluções no domínio da frequência para o dipolo de corrente elétrica harmônica.
    Expressões analíticas para o campo elétrico, o campo magnético e o potencial vetor correspondente são fornecidas.
    Devido às dificuldades que surgem em derivar as expressões finais, não incluiremos os efeitos da permissividade dielétrica 
    (:math:`\varepsilon`); isso é conhecido como aproximação quase estática.



**Obtendo a Resposta Transiente de Uma Solução Harmônica**

Para um sistema causal, a respsota ao degrau uintário (:math:`g_+`) em :math:`t \geq 0` é dado por:

.. math::
	g_+(t) = \int_{-\infty}^\infty f(\tau) u(t - \tau) d\tau = \int_0^t f(\tau) d\tau \; \; \; \textrm{for} \; \; \; t\geq 0
	:label: causal_step


onde :math:`f(t)` é a resposta impulsiva do sistema.
Para a maioria dos problemas geofísicos, no entanto, estamos interessados resposta ao desligamento da função degrau (step-off) ou transitória 
(:math:`g_-`).
A resposta step-off para um sistema causal pode ser dada por:

.. math::
	\begin{split}
	g_-(t) = \int_{-\infty}^\infty f(\tau) \big [ 1 & - u(t - \tau) \big ] d\tau = \; ... \\
	&\int_0^\infty f(\tau) d\tau - \int_0^t f(\tau) d\tau = g_+ (\infty) - g_+(t) \; \; \; \textrm{for} \; \; \; t\geq 0
	\end{split}
	:label: causal_step_off

onde :math:`g_+ (\infty )` representa  a respsota ao degrau para :math:`t = \infty`.
Portanto, se a resposta do degrau for conhecida por :math:`t \geq 0`, ela pode ser usada para obter a resposta do degrau em :math:`t \geq 0`.

De Ward e Hohmann :cite:`ward1988`, a resposta ao degrau pode ser obtida por meio da seguinte transformação inversa de Laplace:

.. math::
	g_+(t) = L^{-1} \Bigg [ \frac{F(s)}{s} \Bigg ]
	:label: step_Laplace_transform

onde :math:`F(s)` é obtido substituindo :math:`s= i\omega` na função de resposta harmônica do sistema.
Para o campo elétrico, campo magnético e potencial vetor decorrente de um dipolo de corrente elétrica harmônica na direção :math:`\mathbf{\hat x}`, estes :ref:`já foram derivados<frequency_domain_electric_dipole_analytic_solution>`.



**Soluções Harmônicas para um Dipolo de Corrente Elétrica**

Como acabamos de mencionar, as soluções harmônicas para o campo elétrico, campo magnético e potencial vetor :ref:`já foram derivadas <frequency_domain_electric_dipole_analytic_solution>` para um termo fonte :math:`\mathbf{J_e^s}= \mathbf{\hat x}Ids \delta (x) \delta (y) \delta (z)`.

Para o potencial vetor:


.. math::
	{\bf A} = \frac{Ids}{4\pi r}e^{-ikr} \mathbf{\hat x} 
	:label: A_frequency_response


Para o campo elétrico:

.. math::
	{\bf E_e}(i\omega ) = \frac{Ids}{4\pi (\sigma + i\omega \varepsilon )r^3} e^{-ikr} \Bigg [ \bigg ( \frac{x^2}{r^2}\mathbf{\hat x} + & \frac{xy}{r^2}\mathbf{\hat y} + \frac{xz}{r^2} \mathbf{\hat z} \Bigg ) \; ... \\
	&\big ( -k^2 r^2 + 3ikr +3 \big ) + \big ( k^2 r^2 -ikr -1 \big ) \mathbf{\hat x} \Bigg ].
	:label: E_frequency_response


E para o campo magnético:

.. math::
	{\bf H_e}(i\omega ) = \frac{Ids}{4\pi r^2} (ikr +1) e^{-ikr} \Bigg ( - \frac{z}{r}\mathbf{\hat y} + \frac{y}{r}\mathbf{\hat z}  \Bigg )
	:label: H_frequency_response

onde o número de onda :math:`k` é dado por:

.. math::
	k = \big ( \omega^2\mu\varepsilon - i \omega \mu \sigma \big )^{1/2}
	:label: wave_number



**Soluções Analíticas para a Resposta Transiente (quase estática)**

Devido às dificuldades que surgem em derivar as expressões finais, não incluiremos os efeitos da permissividade dielétrica (:math:`\varepsilon`); 
isso é conhecido como aproximação quase estática. No regime quase estático (ou seja, quando :math:`| \omega \varepsilon \ll \sigma |`), o número de onda é dado por:

.. math::
	k = \big (- i \omega \mu \sigma \big )^{1/2}
	:label: wave_number_quasi_static


Substituindo :math:`s = i\omega` nas Equações :eq:`A_frequency_response`, :eq:`E_frequency_response` e :eq:`H_frequency_response`, obtemos:


.. math::
	\frac{{\bf A}(s)}{s} = \frac{Ids}{4 \pi r} \frac{e^{- \sqrt{s \mu\sigma r^2}}}{s} \mathbf{\hat x} \; ,
	:label: A_frequency_response_s



.. math::
	\begin{split}
	\frac{{\bf E_e}(s)}{s} = \frac{Ids}{4\pi \sigma r^3} e^{- \sqrt{s\mu\sigma r^2 } } \Bigg [ \bigg ( \frac{x^2}{r^2}\mathbf{\hat x} + & \frac{xy}{r^2}\mathbf{\hat y} + \frac{xz}{r^2} \mathbf{\hat z} \bigg ) ... \\
	\bigg ( & \mu\sigma r^2 + 3 \sqrt{\dfrac{\mu \sigma}{s} } r + \frac{3}{s} \bigg ) - \bigg ( \mu\sigma r^2 + \sqrt{\frac{\mu\sigma}{s}r} + \frac{1}{s} \bigg ) \mathbf{\hat x} \Bigg ],
	\end{split}
	:label: E_frequency_response_s

e

.. math::
	\frac{{\bf H_e}(s)}{s} = \frac{Ids}{4\pi r^2} e^{- \sqrt{s\mu\sigma r^2 } } \bigg ( \sqrt{\frac{\mu\sigma}{s}r} + \frac{1}{s} \bigg )  \bigg ( - \frac{z}{r}\mathbf{\hat y} + \frac{y}{r}\mathbf{\hat z}  \bigg ),
	:label: H_frequency_response_s

A transformação inversa de Laplace das três expressões anteriores e, portanto, a resposta ao degrau, pode ser derivada usando as seguintes identidades
(:cite:`abramowitz1965handbook`)	

.. math::
	L^{-1} \Big [ e^{-\alpha \sqrt{s}} \Big ] = \frac{\alpha}{2\sqrt{\pi t^3}} e^{-\alpha^2/4t} \;\;\; \textrm{for} \; \; \; \alpha > 0
	:label: Laplace_identity_1

.. math::
	L^{-1} \Bigg [ \frac{1}{\sqrt{s}} e^{-\alpha \sqrt{s}} \Bigg ] = \frac{1}{\sqrt{\pi t}} e^{-\alpha^2/4t} \;\;\; \textrm{for} \; \; \; \alpha \geq 0
	:label: Laplace_identity_2

.. math::
	L^{-1} \Bigg [ \frac{1}{s} e^{-\alpha \sqrt{s}} \Bigg ] = \textrm{erfc}\Bigg ( \frac{\alpha}{2\sqrt{t}} \Bigg )\;\;\; \textrm{for} \; \; \; \alpha \geq 0
	:label: Laplace_identity_3

onde :math:`\mathrm{erfc}(x)` é a função erro complementar.
Assim:


.. math::
	L^{-1} \Bigg [ \frac{{\bf A}(s)}{s} \Bigg ] = \frac{Ids}{4 \pi r} \textrm{erfc} (\theta r) \mathbf{\hat x} \; ,
	:label: a_step_response


.. math::
	\begin{split}
	L^{-1}\Bigg [ \frac{{\bf E_e}(s)}{s} \Bigg ] = \frac{Ids}{4\pi \sigma r^3} &\Bigg [ \Bigg ( \frac{x^2}{r^2}\mathbf{\hat x} + \frac{xy}{r^2}\mathbf{\hat y} + \frac{xz}{r^2}\mathbf{\hat z} \Bigg ) \Bigg ( \bigg ( \frac{4}{\sqrt{\pi}}\theta^3 r^3 +  \frac{6}{\sqrt{\pi}} \theta r \bigg ) e^{-\theta^2 r^2} \; ... \\ 
	&+ 3 \, \textrm{erfc}(\theta r) \Bigg ) - \Bigg ( \bigg ( \frac{4}{\sqrt{\pi}} \theta^3 r^3 + \frac{2}{\sqrt{\pi}} \theta r \bigg ) e^{-\theta^2 r^2} + \textrm{erfc}(\theta r) \Bigg ) \mathbf{\hat x} \Bigg ]
	\end{split}
	:label: e_step_response

e

.. math::
	L^{-1}\Bigg [ \frac{{\bf H_e}(s)}{s} \Bigg ] = \frac{Ids}{4 \pi r^3} \bigg ( \frac{2}{\sqrt{\pi}} \theta r \, e^{-\theta^2 r^2} + \textrm{erfc}(\theta r) \bigg ) \big ( - z \, \mathbf{\hat y} + y \, \mathbf{\hat z}  \big )
	:label: h_step_response


onde

.. math::
	\theta = \Bigg ( \frac{\mu\sigma}{4t} \Bigg )^{1/2}
	:label: theta


Usando as quatro expressões anteriores, podemos determinar o transiente do potencial e dos campos magnéticos e elétricos de acordo com a Equação 
:eq:`causal_step_off`.
Para o potencial vetor, a resposta transiente é dada por:


.. math::
	{\bf a}(t) = \frac{Ids}{4 \pi r} \textrm{erf} (\theta r) \mathbf{\hat x}
	:label: a_transient
	

onde :math:`\mathrm{erf}(x)` é a função erro.
Para o campo elétrico, a resposta transiente é dada por:

.. math::
	\begin{split}
	{\bf e_e}(t) = \frac{Ids}{4\pi \sigma r^3} & \Bigg [ \Bigg ( \frac{x^2}{r^2}\mathbf{\hat x} + \frac{xy}{r^2}\mathbf{\hat y} + \frac{xz}{r^2}\mathbf{\hat z} \Bigg ) \Bigg ( 3 \, \textrm{erf}(\theta r) - \bigg ( \frac{4}{\sqrt{\pi}}\theta^3 r^3 \; ... \\
	& + \frac{6}{\sqrt{\pi}} \theta r \bigg ) e^{-\theta^2 r^2}  \Bigg ) - \Bigg ( \textrm{erf}(\theta r) - \bigg ( \frac{4}{\sqrt{\pi}} \theta^3 r^3 + \frac{2}{\sqrt{\pi}} \theta r \bigg ) e^{-\theta^2 r^2} \Bigg ) \mathbf{\hat x} \Bigg ]
	\end{split}.
	:label: e_transient


E para o campo magnético, a resposta transeinet é dada por:

.. math::
	{\bf h_e}(t) = \frac{Ids}{4 \pi r^3} \bigg ( \textrm{erf}(\theta r) - \frac{2}{\sqrt{\pi}} \theta r \, e^{-\theta^2 r^2}  \bigg ) \big ( - z \, \mathbf{\hat y} + y \, \mathbf{\hat z}  \big )
	:label: h_transient

Para aplicações geofísicas, geralmente medimos a força eletromotriz induzida dentro de uma bobina receptora.
Como resultado, estamos interessados na taxa de decaimento do campo magnético no tempo.
Tirando a derivada da Equação :eq:`h_transient`, obtemos:

.. math::
	\frac{\partial{ \bf h_e}}{\partial t} = - \frac{2 \, \theta^5 Ids}{\pi^{3/2} \mu \sigma} e^{-\theta^2 r^2} \big ( - z \, \mathbf{\hat y} + y \, \mathbf{\hat z}  \big )
	:label: dhdt_transient
