.. _time_domain_magnetic_dipole_analytic_solution:

Solução Analítica
=================

.. purpose::

    Aqui, apresentamos uma formulação para prever os campos elétricos e magnéticos gerados pelo transiente de uma fonte dipolar magnética.
    Isso é realizado aplicando a transformada de Laplace inversa às soluções no domínio da frequência para o dipolo magnético harmônico.
    Expressões analíticas para o campo elétrico, o campo magnético e o potencial vetorial correspondente são fornecidas.
    Devido às dificuldades que surgem em derivar as expressões finais, não incluiremos os efeitos da permissividade dielétrica (:math:`\varepsilon`); isso é conhecido como aproximação quase estática.
 


**Obtendo a Resposta Transiente de uma Solução Harmônica**


Para um sistema causal, a resposta ao degrau unitário (:math:`g_+`) em :math:`t \geq 0` é dado por:

.. math::
	g_+(t) = \int_{-\infty}^\infty f(\tau) u(t - \tau) d\tau = \int_0^t f(\tau) d\tau \; \; \; \textrm{for} \; \; \; t\geq 0
	:label: causal_step_mag

onde :math:`f(t)` é a resposta do sistema ao impulso.
Para a maioria dos problemas geofísicos, no entanto, estamos interessados na resposta intermediária ou transiente (:math:`g_-`).
A resposta step-off (desligammento da fonte) para um sistema causal pode ser dada por:

.. math::
	\begin{split}
	g_-(t) = \int_{-\infty}^\infty f(\tau) \big [ 1 - &u(t - \tau) \big ] d\tau = \; ... \\
	& \int_0^\infty f(\tau) d\tau - \int_0^t f(\tau) d\tau = g_+ (\infty) - g_+(t) \; \; \; \textrm{for} \; \; \; t\geq 0
	\end{split}
	:label: causal_step_mag_off

onde :math:`g_+ (\infty )` representa  a resposta ao degrau em :math:`t = \infty`.
Portanto, se a resposta do degrau for conhecida por :math:`t \geq 0`, ela pode ser usada para obter a resposta do degrau em :math:`t \geq 0`.

De Ward e Hohmann :cite:`ward1988`, a resposta ao degrau pode ser obtida via a seguinte transformada inversa de Laplace:

.. math::
	g_+(t) = L^{-1} \Bigg [ \frac{F(s)}{s} \Bigg ]
	:label: step_Laplace_transform_mag

onde :math:`F(s)` é obtido substituindo :math:`s = i\omega` na função de resposta harmônica do sistema.
Para o campo elétrico, campo magnético e potencial vetor decorrente de um dipolo magnético harmônico na direção :math:`\mathbf{\hat x}`, estes 
:ref:`já foram derivados<frequency_domain_magnetic_dipole_analytic_solution>`.


**Soluções Harmônicas para um Dipolo Magnético**

Como acabamos de mencionar, as soluções harmônicas para o campo elétrico, campo magnético e potencial vetor :ref:`já foram derivadas <frequency_domain_magnetic_dipole_analytic_solution>` para um termo fonte :math:`\mathbf{J_m^s} = -i\omega IS \delta (x) \delta (y) \delta (z) \mathbf{\hat x}`.


Para o potencial vetor:

.. math::
	{\bf F}(i\omega ) = \frac{i\omega \mu m}{4\pi r} e^{-ikr} \mathbf{\hat x}
	:label: F_harmonic_response


Para o campo elétrico:

.. math::
	{\bf E_m}(i\omega ) = \frac{i\omega \mu m}{4\pi r^2} (ikr +1) e^{-ikr} \Bigg ( \frac{z}{r}\mathbf{\hat y} - \frac{y}{r}\mathbf{\hat z}  \Bigg )
	:label: E_harmonic_response

E para o campo magnético:

.. math::
	{\bf H_m}(i\omega ) = \frac{m}{4\pi r^3} e^{-ikr} \Bigg [ \Bigg ( \frac{x^2}{r^2}\mathbf{\hat x} + \frac{xy}{r^2}\mathbf{\hat y} + \frac{xz}{r^2} \mathbf{\hat z} \Bigg ) \big ( -k^2 r^2 + 3ikr +3 \big ) + \big ( k^2 r^2 -ikr -1 \big ) \mathbf{\hat x} \Bigg ]
	:label: H_harmonic_response

onde o número de onda :math:`k` é dado por:

.. math::
	k = \big ( \omega^2\mu\varepsilon - i \omega \mu \sigma \big )^{1/2}
	:label: wave_number_mag



**Soluções Analíticas para a Resposta Transiente (Quase-Estático)**


Devido às dificuldades que surgem em derivar as expressões finais, não incluiremos os efeitos da permissividade dielétrica (:math:`\varepsilon`); isso é conhecido como aproximação quase estática. No regime quase estático (ou seja, quando :math:`|\omega \varepsilon \ll \sigma|`), o número de onda é dado por:

.. math::
	k = \big (- i \omega \mu \sigma \big )^{1/2}
	:label: wave_number_mag_quasi_static

Se nós substituirmos :math:`s = i\omega` nas Equações :eq:`F_harmonic_response`, :eq:`E_harmonic_response` e :eq:`H_harmonic_response` e dividida por :math:`s` então:


.. math::
	\frac{{\bf F}(s)}{s} = \frac{\mu m}{4 \pi r} e^{- \sqrt{s \mu\sigma r^2}} \mathbf{\hat x} \; ,
	:label: A_frac_inverse_Laplace



.. math::
	\frac{{\bf E_m}(s)}{s} = s \Bigg [ \frac{\mu m}{4\pi r^3} \bigg ( \sqrt{\frac{ \mu \sigma}{s}} r + \frac{1}{s} \bigg ) e^{-\sqrt{s \mu \sigma r^2}} \big ( z \, \mathbf{\hat y} - y\, \mathbf{\hat z}  \big ) \Bigg ]
	:label: E_frac_inverse_Laplace

e

.. math::
	\begin{split}
	\frac{{\bf H_m}(s)}{s} = \frac{m}{4\pi r^3} & e^{-\sqrt{s\mu \sigma r^2}} \Bigg [ \Bigg ( \frac{x^2}{r^2}\mathbf{\hat x} +  \frac{xy}{r^2}\mathbf{\hat y} + \frac{xz}{r^2} \mathbf{\hat z} \Bigg ) \; ... \\
	& \Bigg ( -\mu\sigma r^2 + 3 \sqrt{\frac{\mu \sigma}{s}}r + \frac{3}{s} \Bigg ) + \Bigg ( -\mu\sigma r^2 - \sqrt{\frac{\mu \sigma}{s}} r - \frac{1}{s} \Bigg ) \mathbf{\hat x} \Bigg ]
	\end{split}
	:label: H_frac_inverse_Laplace


A transformação inversa de Laplace das três expressões anteriores e, portanto, a resposta ao degrau, pode ser derivada usando as seguintes identidades (Abramowitz e Stegun, 1964):


.. math::
	L^{-1} \Big [ s F(s) \Big ] = \frac{d}{dt} f(t)

.. math::
	L^{-1} \Big [ e^{-\alpha \sqrt{s}} \Big ] = \frac{\alpha}{2\sqrt{\pi t^3}} e^{-\alpha^2/4t} \;\;\; \textrm{for} \; \; \; \alpha > 0 \\
	:label: inverse_Laplace_identity_2

.. math::
	L^{-1} \Bigg [ \frac{1}{\sqrt{s}} e^{-\alpha \sqrt{s}} \Bigg ] = \frac{1}{\sqrt{\pi t}} e^{-\alpha^2/4t} \;\;\; \textrm{for} \; \; \; \alpha \geq 0 \\
	:label: inverse_Laplace_identity_3

.. math::
	L^{-1} \Bigg [ \frac{1}{s} e^{-\alpha \sqrt{s}} \Bigg ] = \textrm{erfc}\Bigg ( \frac{\alpha}{2\sqrt{t}} \Bigg )\;\;\; \textrm{for} \; \; \; \alpha \geq 0
	:label: inverse_Laplace_identity_4


onde erfc(x) é a função erro complementar.
Assim:

.. math::
	L^{-1} \Bigg [ \frac{{\bf F}(s)}{s} \Bigg ] = \frac{m\theta^3}{\pi^{3/2} \sigma} e^{-\theta^2 r^2} \mathbf{\hat x} \; ,
	:label: a_step_response_mag



.. math::
	L^{-1}\Bigg [ \frac{{\bf E_m}(s)}{s} \Bigg ] = \frac{2 m \theta^5 }{\pi^{3/2} \sigma} e^{-\theta^2 r^2} \big ( z \, \mathbf{\hat y} - y \, \mathbf{\hat z} \big )
	:label: e_step_response_mag

e

.. math::
	\begin{split}
	L^{-1}\Bigg [ \frac{{\bf H_m}(s)}{s} \Bigg ] = \frac{m}{4\pi r^3} \Bigg [ & \Bigg ( \frac{x^2}{r^2}\mathbf{\hat x} + \frac{xy}{r^2}\mathbf{\hat y} + \frac{xz}{r^2}\mathbf{\hat z} \Bigg ) \Bigg ( \bigg ( \frac{4}{\sqrt{\pi}} \theta^3 r^3 + \frac{6}{\sqrt{\pi}} \theta r \bigg ) e^{-\theta^2 r^2}  \, ...  \\
	& + 3\, \textrm{erfc} (\theta r) \Bigg ) - \Bigg ( \bigg ( \frac{4}{\sqrt{\pi}} \theta^3 r^3 + \frac{2}{\sqrt{\pi}} \theta r \bigg ) e^{-\theta^2 r^2} +  \textrm{erfc} (\theta r) \Bigg ) \mathbf{\hat x} \Bigg ]
	\end{split}
	:label: h_step_response_mag

onde

.. math::
	\theta = \Bigg ( \frac{\mu\sigma}{4t} \Bigg )^{1/2}
	:label: theta_quasi_static


Usando as três expressões anteriores, podemos determinar o potencial vetor transiente, os campos magnéticos do campo elétrico de acordo com a Equação 
:eq:`causal_step_mag_off`.
Para o potencial vetor, a resposta transiente é dada por:


.. math::
	{\bf f}(t) = -\frac{m \theta^3}{\pi^{3/2} \sigma} e^{-\theta^2 r^2} \mathbf{\hat x}
	:label: vector_potential_step_off


Para o campo elétrico, a resposta transiente é dada por:


.. math::
	{\bf e_m}(t) = \frac{2 m \theta^5 }{\pi^{3/2} \sigma} e^{-\theta^2 r^2} \big ( -z \, \mathbf{\hat y} + y \, \mathbf{\hat z} \big )
	:label: e_step_off_response

onde erf(:math:`x`) é a função erro.
E para o campo magnético, a resposta transiente é dado por:

.. math::
	\begin{split}
	{\bf h_m}(t) = \frac{m}{4\pi r^3} \Bigg [ & \Bigg ( \frac{x^2}{r^2} \mathbf{\hat x} + \frac{xy}{r^2}\mathbf{\hat y} + \frac{xz}{r^2} \mathbf{\hat z} \Bigg ) \Bigg ( 3 \, \textrm{erf}(\theta r) - \bigg ( \frac{4}{\sqrt{\pi}}\theta^3 r^3  \; ... \\
	&+ \frac{6}{\sqrt{\pi}}\theta r \bigg ) e^{-\theta^2 r^2} \Bigg ) - \Bigg (\textrm{erf}(\theta r) - \bigg ( \frac{4}{\sqrt{\pi}}\theta^3 r^3 + \frac{2}{\sqrt{\pi}}\theta r \bigg ) e^{-\theta^2 r^2} \Bigg ) \mathbf{\hat x}  \Bigg ]
	\end{split}
	:label: h_step_off_response


Para aplicações geofísicas, geralmente medimos a força eletromotriz induzida dentro de uma bobina receptora.
Como resultado, estamos interessados na taxa de decaimento do campo magnético no tempo.
Tomando a derivada da Equação :eq:`h_step_off_response`, isso é dado por:

.. math::
	\frac{\partial{ \bf h_m}}{\partial t} = - \frac{4m \theta^5}{\pi^{3/2} \mu\sigma} e^{-\theta^2 r^2} \Bigg [ \Bigg ( \frac{x^2}{r^2}\mathbf{\hat x} + \frac{xy}{r^2} \mathbf{\hat y} + \frac{xz}{r^2} \mathbf{\hat z} \Bigg ) \theta^2 r^2  + \big (1 -\theta^2 r^2 \big ) \mathbf{\hat x} \Bigg ]
	:label: dhdt_step_off_quasi_static
