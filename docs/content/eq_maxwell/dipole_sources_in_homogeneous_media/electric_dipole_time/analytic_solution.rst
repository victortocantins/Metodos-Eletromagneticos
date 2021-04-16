.. _time_domain_electric_dipole_analytic_solution:

Analytic Solution
=================

.. purpose::

    Here, we present a formulation for predicting the electric and magnetic fields generated by a transient electrical current dipole source.
    This is accomplished by applying the inverse Laplace transform to frequency domain solutions for the harmonic electrical current dipole.
    Analytic expressions for the electric field, the magnetic field and the corresponding vector potential are provided.
    Due to the difficulties which arise in deriving the final expressions, we will not include the effects of dielectric permittivity (:math:`\varepsilon`); this is known as the quasi-static approximation.
    




**Obtaining the Transient Response from a Harmonic Solution**


For a causal system, the unit step-response (:math:`g_+`) at :math:`t \geq 0` is given by:

.. math::
	g_+(t) = \int_{-\infty}^\infty f(\tau) u(t - \tau) d\tau = \int_0^t f(\tau) d\tau \; \; \; \textrm{for} \; \; \; t\geq 0
	:label: causal_step


where :math:`f(t)` is the system's impulse response.
For most geophysical problems however, we are interested in the step-off or transient response (:math:`g_-`).
The step-off response for a causal system may be given by:

.. math::
	\begin{split}
	g_-(t) = \int_{-\infty}^\infty f(\tau) \big [ 1 & - u(t - \tau) \big ] d\tau = \; ... \\
	&\int_0^\infty f(\tau) d\tau - \int_0^t f(\tau) d\tau = g_+ (\infty) - g_+(t) \; \; \; \textrm{for} \; \; \; t\geq 0
	\end{split}
	:label: causal_step_off

where :math:`g_+ (\infty )` represents the step-response at :math:`t = \infty`.
Therefore, if the step-response is known for :math:`t \geq 0`, it can be used to obtain the step-off response at :math:`t \geq 0`.

From Ward and Hohmann :cite:`ward1988`, the step-response can be obtained via the following inverse Laplace transform:

.. math::
	g_+(t) = L^{-1} \Bigg [ \frac{F(s)}{s} \Bigg ]
	:label: step_Laplace_transform

where :math:`F(s)` is obtained by replacing :math:`s=i\omega` in the system's harmonic response function.
For the electric field, magnetic field and vector potential arising from a harmonic electrical current dipole in the :math:`\mathbf{\hat x}` direction, these have :ref:`already been derived<frequency_domain_electric_dipole_analytic_solution>`.



**Harmonic Solutions for an Electrical Current Dipole**

As we just mentionned, harmonic solutions for the electric field, magnetic field and vector potential have :ref:`already been derived<frequency_domain_electric_dipole_analytic_solution>` for a source term :math:`\mathbf{J_e^s} = \mathbf{\hat x} Ids \delta (x) \delta (y) \delta (z)`. 

For the vector potential:


.. math::
	{\bf A} = \frac{Ids}{4\pi r}e^{-ikr} \mathbf{\hat x} 
	:label: A_frequency_response


For the electric field:

.. math::
	{\bf E_e}(i\omega ) = \frac{Ids}{4\pi (\sigma + i\omega \varepsilon )r^3} e^{-ikr} \Bigg [ \bigg ( \frac{x^2}{r^2}\mathbf{\hat x} + & \frac{xy}{r^2}\mathbf{\hat y} + \frac{xz}{r^2} \mathbf{\hat z} \Bigg ) \; ... \\
	&\big ( -k^2 r^2 + 3ikr +3 \big ) + \big ( k^2 r^2 -ikr -1 \big ) \mathbf{\hat x} \Bigg ] 
	:label: E_frequency_response


And for the magnetic field:

.. math::
	{\bf H_e}(i\omega ) = \frac{Ids}{4\pi r^2} (ikr +1) e^{-ikr} \Bigg ( - \frac{z}{r}\mathbf{\hat y} + \frac{y}{r}\mathbf{\hat z}  \Bigg )
	:label: H_frequency_response

where the wavenumber :math:`k` is given by:

.. math::
	k = \big ( \omega^2\mu\varepsilon - i \omega \mu \sigma \big )^{1/2}
	:label: wave_number




**Analytic Solutions for the Transient Response (Quasi-Static)**

Due to the difficulties which arise in deriving the final expressions, we will not include the effects of dielectric permittivity (:math:`\varepsilon`); this is known as the quasi-static approximation. In the quasi-static regime (i.e. when :math:`|\omega\varepsilon \ll \sigma |`), the wavenumber is given by:

.. math::
	k = \big (- i \omega \mu \sigma \big )^{1/2}
	:label: wave_number_quasi_static


Substituting :math:`s = i\omega` into Eqs. :eq:`A_frequency_response`, :eq:`E_frequency_response` and :eq:`H_frequency_response`, we obtain:


.. math::
	\frac{{\bf A}(s)}{s} = \frac{Ids}{4 \pi r} \frac{e^{- \sqrt{s \mu\sigma r^2}}}{s} \mathbf{\hat x} \; ,
	:label: A_frequency_response_s



.. math::
	\begin{split}
	\frac{{\bf E_e}(s)}{s} = \frac{Ids}{4\pi \sigma r^3} e^{- \sqrt{s\mu\sigma r^2 } } \Bigg [ \bigg ( \frac{x^2}{r^2}\mathbf{\hat x} + & \frac{xy}{r^2}\mathbf{\hat y} + \frac{xz}{r^2} \mathbf{\hat z} \bigg ) ... \\
	\bigg ( & \mu\sigma r^2 + 3 \sqrt{\dfrac{\mu \sigma}{s} } r + \frac{3}{s} \bigg ) - \bigg ( \mu\sigma r^2 + \sqrt{\frac{\mu\sigma}{s}r} + \frac{1}{s} \bigg ) \mathbf{\hat x} \Bigg ],
	\end{split}
	:label: E_frequency_response_s

and

.. math::
	\frac{{\bf H_e}(s)}{s} = \frac{Ids}{4\pi r^2} e^{- \sqrt{s\mu\sigma r^2 } } \bigg ( \sqrt{\frac{\mu\sigma}{s}r} + \frac{1}{s} \bigg )  \bigg ( - \frac{z}{r}\mathbf{\hat y} + \frac{y}{r}\mathbf{\hat z}  \bigg ),
	:label: H_frequency_response_s

The inverse Laplace transform of the previous three expressions, and thus the step-response, can be derived by using the following identities (Abramowitz and Stegun, 1964):

.. math::
	L^{-1} \Big [ e^{-\alpha \sqrt{s}} \Big ] = \frac{\alpha}{2\sqrt{\pi t^3}} e^{-\alpha^2/4t} \;\;\; \textrm{for} \; \; \; \alpha > 0
	:label: Laplace_identity_1

.. math::
	L^{-1} \Bigg [ \frac{1}{\sqrt{s}} e^{-\alpha \sqrt{s}} \Bigg ] = \frac{1}{\sqrt{\pi t}} e^{-\alpha^2/4t} \;\;\; \textrm{for} \; \; \; \alpha \geq 0
	:label: Laplace_identity_2

.. math::
	L^{-1} \Bigg [ \frac{1}{s} e^{-\alpha \sqrt{s}} \Bigg ] = \textrm{erfc}\Bigg ( \frac{\alpha}{2\sqrt{t}} \Bigg )\;\;\; \textrm{for} \; \; \; \alpha \geq 0
	:label: Laplace_identity_3

where erfc(x) is the complimentary error function.
Thus:


.. math::
	L^{-1} \Bigg [ \frac{{\bf A}(s)}{s} \Bigg ] = \frac{Ids}{4 \pi r} \textrm{erfc} (\theta r) \mathbf{\hat x} \; ,
	:label: a_step_response


.. math::
	\begin{split}
	L^{-1}\Bigg [ \frac{{\bf E_e}(s)}{s} \Bigg ] = \frac{Ids}{4\pi \sigma r^3} &\Bigg [ \Bigg ( \frac{x^2}{r^2}\mathbf{\hat x} + \frac{xy}{r^2}\mathbf{\hat y} + \frac{xz}{r^2}\mathbf{\hat z} \Bigg ) \Bigg ( \bigg ( \frac{4}{\sqrt{\pi}}\theta^3 r^3 +  \frac{6}{\sqrt{\pi}} \theta r \bigg ) e^{-\theta^2 r^2} \; ... \\ 
	&+ 3 \, \textrm{erfc}(\theta r) \Bigg ) - \Bigg ( \bigg ( \frac{4}{\sqrt{\pi}} \theta^3 r^3 + \frac{2}{\sqrt{\pi}} \theta r \bigg ) e^{-\theta^2 r^2} + \textrm{erfc}(\theta r) \Bigg ) \mathbf{\hat x} \Bigg ]
	\end{split}
	:label: e_step_response

and

.. math::
	L^{-1}\Bigg [ \frac{{\bf H_e}(s)}{s} \Bigg ] = \frac{Ids}{4 \pi r^3} \bigg ( \frac{2}{\sqrt{\pi}} \theta r \, e^{-\theta^2 r^2} + \textrm{erfc}(\theta r) \bigg ) \big ( - z \, \mathbf{\hat y} + y \, \mathbf{\hat z}  \big )
	:label: h_step_response


where

.. math::
	\theta = \Bigg ( \frac{\mu\sigma}{4t} \Bigg )^{1/2}
	:label: theta


Using the previous four expressions, we can determine the transient vector potential, electric field magnetic fields according to Eq. :eq:`causal_step_off`.
For the vector potential, the transient response is given by:


.. math::
	{\bf a}(t) = \frac{Ids}{4 \pi r} \textrm{erf} (\theta r) \mathbf{\hat x}
	:label: a_transient
	

where erf(:math:`x`) is the error function.
For the electric field, the transient response is given by:

.. math::
	\begin{split}
	{\bf e_e}(t) = \frac{Ids}{4\pi \sigma r^3} & \Bigg [ \Bigg ( \frac{x^2}{r^2}\mathbf{\hat x} + \frac{xy}{r^2}\mathbf{\hat y} + \frac{xz}{r^2}\mathbf{\hat z} \Bigg ) \Bigg ( 3 \, \textrm{erf}(\theta r) - \bigg ( \frac{4}{\sqrt{\pi}}\theta^3 r^3 \; ... \\
	& + \frac{6}{\sqrt{\pi}} \theta r \bigg ) e^{-\theta^2 r^2}  \Bigg ) - \Bigg ( \textrm{erf}(\theta r) - \bigg ( \frac{4}{\sqrt{\pi}} \theta^3 r^3 + \frac{2}{\sqrt{\pi}} \theta r \bigg ) e^{-\theta^2 r^2} \Bigg ) \mathbf{\hat x} \Bigg ]
	\end{split}
	:label: e_transient


And for the magnetic field, the transient response is given by:

.. math::
	{\bf h_e}(t) = \frac{Ids}{4 \pi r^3} \bigg ( \textrm{erf}(\theta r) - \frac{2}{\sqrt{\pi}} \theta r \, e^{-\theta^2 r^2}  \bigg ) \big ( - z \, \mathbf{\hat y} + y \, \mathbf{\hat z}  \big )
	:label: h_transient


For geophysical applications, we generally measure the electromotive force induced within a receiver coil.
As a result, we are interested in the time-rate of decay of the magnetic field.
By taking the derivative of Eq. :eq:`h_transient`, we obtain:

.. math::
	\frac{\partial{ \bf h_e}}{\partial t} = - \frac{2 \, \theta^5 Ids}{\pi^{3/2} \mu \sigma} e^{-\theta^2 r^2} \big ( - z \, \mathbf{\hat y} + y \, \mathbf{\hat z}  \big )
	:label: dhdt_transient